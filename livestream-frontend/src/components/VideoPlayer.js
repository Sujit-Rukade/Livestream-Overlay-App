import Hls from 'hls.js';
import React from 'react';
import './VideoPlayer.css';

const VideoPlayer = ({ overlays, hlsUrl }) => {
  const videoRef = React.useRef(null);

  React.useEffect(() => {
    if (Hls.isSupported()) {
      const hls = new Hls();
      hls.loadSource(hlsUrl);
      hls.attachMedia(videoRef.current);
      hls.on(Hls.Events.MANIFEST_PARSED, () => {
        videoRef.current.play();
      });
    } else if (videoRef.current.canPlayType('application/vnd.apple.mpegurl')) {
      videoRef.current.src = hlsUrl;
      videoRef.current.addEventListener('loadedmetadata', () => {
        videoRef.current.play();
      });
    }
  }, [hlsUrl]);

  return (
    <div className="video-container">
      <video ref={videoRef} controls className="video-player">
        Your browser does not support the video tag.
      </video>
      {overlays.map((overlay) => (
        <div
          key={overlay._id}
          className="overlay"
          style={{
            top: overlay.data.position?.y || 0,
            left: overlay.data.position?.x || 0,
            fontSize: overlay.data.size || '16px',
            color: overlay.data.color || 'white',
            opacity: overlay.data.opacity || 1,
            border: overlay.data.border || 'none'
          }}
        >
          {overlay.data.text}
        </div>
      ))}
    </div>
  );
};

export default VideoPlayer;
