# User Documentation for Livestream Application

## Table of Contents
- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Managing Overlays](#managing-overlays)
- [Inputting the RTSP URL](#inputting-the-rtsp-url)

## Introduction
This documentation provides a comprehensive guide on setting up and using the Livestream Application. The application allows users to manage video overlays and stream content using an RTSP URL.

## Requirements
- Python 3.x
- Node.js
- npm
- A web browser

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Sujit-Rukade/Livestream-Overlay-App.git
   cd livestreamer
   ```

2. Set up the backend:

- Navigate to the livestream-backend directory:
```bash
cd livestream-backend
```

- Create a virtual environment and activate it:
```bash
python -m venv venv
.\venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Mac/Linux
```

- Install the required packages:
```bash
pip install -r requirements.txt
```

3. Set up the frontend:

- Navigate to the livestream-frontend directory:
```bash
cd ../livestream-frontend
```

- Install the required npm packages:
```bash
npm install
```

4. Start the backend server:

```bash
python app.py
```

5. Start the frontend application:

```bash
npm start
```

## Configuration
Before using the application, ensure that you have the correct RTSP URL. The URL should point to a valid stream that the application can access.

## Usage
Open your web browser and navigate to http://localhost:3000 to access the frontend.
Input your RTSP URL in the designated input field.
## Managing Overlays
1. Use the overlay management form to create new overlays:

- Enter the overlay text, position (X and Y coordinates), size, and color.
- Click the "Add Overlay" button to submit the overlay.
2. The overlays will appear on the video player based on the specified coordinates.

## Inputting the RTSP URL
To input the RTSP URL:

1. Locate the input field labeled "RTSP URL" on the application interface.
2. Enter the URL in the format rtsp://example.com/stream.
3. Click the "Submit" button to apply the RTSP URL.