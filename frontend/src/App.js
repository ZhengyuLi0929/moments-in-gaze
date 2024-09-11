import React from 'react';
import VideoGallery from './components/VideoGallery';
import UploadForm from './components/UploadForm';
import './App.css';

function App() {
  return (
    <div className="App">
      <h1>Moments in Gaze</h1>
      <UploadForm />
      <VideoGallery />
    </div>
  );
}

export default App;
