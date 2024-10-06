import React, { useState } from 'react';
import axios from 'axios';
import './OverlayManager.css'; 

const OverlayManager = ({ onOverlaySubmit }) => {
  const [text, setText] = useState('');
  const [position, setPosition] = useState({ x: 0, y: 0 });
  const [size, setSize] = useState(16);
  const [color, setColor] = useState('white');

  const handleSubmit = () => {
    const newOverlay = {
      data: {
        position,
        size: `${size}px`,
        color,
        text,
      },
    };

    axios.post('http://localhost:5000/api/overlays', newOverlay)
      .then(response => {
        console.log(response.data);
        if (onOverlaySubmit) {
          onOverlaySubmit(newOverlay); 
        }
      })
      .catch(error => console.error(error));
  };

  return (
    <div className="overlay-manager">
      <h2 className="overlay-title">Overlay Manager</h2>
      <div className="overlay-form">
        <input
          type="text"
          placeholder="Overlay Text"
          value={text}
          onChange={e => setText(e.target.value)}
          className="overlay-input"
        />
        <input
          type="number"
          placeholder="X Position"
          value={position.x}
          onChange={e => setPosition({ ...position, x: Number(e.target.value) })}
          className="overlay-input"
        />
        <input
          type="number"
          placeholder="Y Position"
          value={position.y}
          onChange={e => setPosition({ ...position, y: Number(e.target.value) })}
          className="overlay-input"
        />
        <input
          type="number"
          placeholder="Size (px)"
          value={size}
          onChange={e => setSize(Number(e.target.value))}
          className="overlay-input"
        />
        <input
          type="text"
          placeholder="Color (e.g., red, #FFF)"
          value={color}
          onChange={e => setColor(e.target.value)}
          className="overlay-input"
        />
        <button onClick={handleSubmit} className="overlay-button">Add Overlay</button>
      </div>
    </div>
  );
};

export default OverlayManager;
