import React, { useState } from 'react';

const UploadForm = () => {
  const [file, setFile] = useState(null);
  const [name, setName] = useState('');
  const [social, setSocial] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('file', file);
    formData.append('name', name);
    formData.append('social', social);

    fetch('http://localhost:5000/api/upload', {
      method: 'POST',
      body: formData,
    })
      .then(response => response.json())
      .then(data => console.log(data))
      .catch(error => console.error('Error:', error));
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <input type="text" placeholder="Your Name" onChange={(e) => setName(e.target.value)} />
      <input type="text" placeholder="Your Social Media" onChange={(e) => setSocial(e.target.value)} />
      <button type="submit">Upload</button>
    </form>
  );
};

export default UploadForm;
