from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import cv2

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Directory for uploaded videos
UPLOAD_FOLDER = 'static/uploads/'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Store user info in a simple text file for now
USER_DATA_FILE = os.path.join(app.config['UPLOAD_FOLDER'], 'user_data.txt')


@app.route('/api/upload', methods=['POST'])
def upload_video():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        # Save the uploaded file
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Process the video to crop it (placeholder, OpenCV for eye cropping)
        cropped_filepath = crop_to_eyes(filepath)

        # Save user information (name and social)
        name = request.form['name']
        social = request.form['social']
        save_user_data(name, social, os.path.basename(cropped_filepath))

        return jsonify({'message': 'Upload successful', 'video': cropped_filepath}), 200


@app.route('/api/videos', methods=['GET'])
def get_videos():
    users = []
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'r') as f:
            for line in f:
                name, social, video_file = line.strip().split(', ')
                users.append({'name': name, 'social': social, 'videoFile': video_file})
    return jsonify(users)


def crop_to_eyes(video_path):
    # Placeholder: Basic implementation to "process" the video (adjust for real eye cropping)
    output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'cropped_' + os.path.basename(video_path))
    cap = cv2.VideoCapture(video_path)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, 20.0, (640, 480))  # Adjust as necessary

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            # Placeholder: Apply face/eye detection and crop to eyes here
            cropped_frame = frame  # No actual cropping implemented yet
            out.write(cropped_frame)
        else:
            break

    cap.release()
    out.release()
    return output_path


def save_user_data(name, social, video_file):
    with open(USER_DATA_FILE, 'a') as f:
        f.write(f'{name}, {social}, {video_file}\n')


# Serve uploaded video files
@app.route('/static/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    app.run(debug=True)
