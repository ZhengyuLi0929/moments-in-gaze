import React from 'react';

const VideoCard = ({ videoUrl, name, social }) => {
  return (
    <div className="video-card">
      <video src={videoUrl} autoPlay loop muted width="200" height="200"></video>
      <p>{name}</p>
      <p>{social}</p>
    </div>
  );
};

export default VideoCard;
