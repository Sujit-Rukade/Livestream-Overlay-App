import React, { useEffect, useState } from 'react';
import OverlayManager from './components/OverlayManager';
import VideoPlayer from './components/VideoPlayer';
import axios from 'axios';
import './App.css';

const App = () => {
  const [overlays, setOverlays] = useState([]);
  const [rtspUrl, setRtspUrl] = useState('');

  useEffect(() => {
    const fetchOverlays = async () => {
      try {
        const response = await axios.get('http://localhost:5000/api/overlays');
        setOverlays(response.data);
      } catch (error) {
        console.error('Error fetching overlays:', error);
      }
    };

    const fetchStreamUrl = async () => {
      try {
        const response = await axios.get('http://localhost:5000/api/stream');
        setRtspUrl(response.data.rtsp_url);
      } catch (error) {
        console.error('Error fetching RTSP URL:', error);
      }
    };

    fetchOverlays();
    fetchStreamUrl();
  }, []);

  return (
    <div className="app">
      <h1 className="app-title">Video Overlay Manager</h1>
      <div className="app-content">
        <OverlayManager setOverlays={setOverlays} />
        <VideoPlayer overlays={overlays} hlsUrl={rtspUrl} />
      </div>
    </div>
  );
};

export default App;
