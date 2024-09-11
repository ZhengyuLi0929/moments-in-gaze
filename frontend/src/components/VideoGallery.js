import React, { useState, useEffect } from 'react';
import VideoCard from './VideoCard';

const VideoGallery = () => {
  const [videos, setVideos] = useState([]);

  useEffect(() => {
    fetch('http://localhost:5000/api/videos')
      .then(response => response.json())
      .then(data => setVideos(data))
      .catch(error => console.error('Error:', error));
  }, []);

  return (
    <div className="video-gallery">
      {videos.map((video, index) => (
        <VideoCard 
          key={index} 
          videoUrl={`http://localhost:5000/static/uploads/${video.videoFile}`} 
          name={video.name} 
          social={video.social} 
        />
      ))}
    </div>
  );
};

export default VideoGallery;
