# API Documentation

This document outlines the available API endpoints for the Livestreamer application. It details how to perform CRUD operations on overlays and fetch the RTSP stream URL.

## Base URL
http://localhost:5000/api



## Endpoints

### 1. Create Overlay

- **Endpoint:** `/overlays`
- **Method:** `POST`
- **Description:** Creates a new overlay.
- **Request Body:**
    ```json
    {
      "data": {
        "position": {
          "x": 0,
          "y": 0
        },
        "size": "16px",
        "color": "white",
        "text": "Overlay Text"
      }
    }
    ```
- **Response:**
  - **Status 201 Created**
    ```json
    {
      "_id": "overlay_id",
      "data": {
        "position": {
          "x": 0,
          "y": 0
        },
        "size": "16px",
        "color": "white",
        "text": "Overlay Text"
      }
    }
    ```

### 2. Get All Overlays

- **Endpoint:** `/overlays`
- **Method:** `GET`
- **Description:** Retrieves all overlays.
- **Response:**
  - **Status 200 OK**
    ```json
    [
      {
        "_id": "overlay_id",
        "data": {
          "position": {
            "x": 0,
            "y": 0
          },
          "size": "16px",
          "color": "white",
          "text": "Overlay Text"
        }
      }
    ]
    ```

### 3. Update Overlay

- **Endpoint:** `/overlays/:id`
- **Method:** `PUT`
- **Description:** Updates an existing overlay by ID.
- **Request Body:**
    ```json
    {
      "data": {
        "position": {
          "x": 10,
          "y": 20
        },
        "size": "20px",
        "color": "red",
        "text": "Updated Overlay Text"
      }
    }
    ```
- **Response:**
  - **Status 200 OK**
    ```json
    {
      "_id": "overlay_id",
      "data": {
        "position": {
          "x": 10,
          "y": 20
        },
        "size": "20px",
        "color": "red",
        "text": "Updated Overlay Text"
      }
    }
    ```

### 4. Delete Overlay

- **Endpoint:** `/overlays/:id`
- **Method:** `DELETE`
- **Description:** Deletes an overlay by ID.
- **Response:**
  - **Status 204 No Content**

### 5. Get RTSP Stream URL

- **Endpoint:** `/stream`
- **Method:** `GET`
- **Description:** Retrieves the RTSP stream URL.
- **Response:**
  - **Status 200 OK**
    ```json
    {
      "rtsp_url": "rtsp://example.com/stream"
    }
    ```

## Error Handling
Common error responses include:
- **400 Bad Request**: The request was invalid. Ensure all required fields are included.
- **404 Not Found**: The specified overlay ID was not found.
- **500 Internal Server Error**: An unexpected error occurred on the server.

## Example Usage
### Create Overlay Example (using `curl`):
```bash
curl -X POST http://localhost:5000/api/overlays \
-H "Content-Type: application/json" \
-d '{
  "data": {
    "position": {
      "x": 0,
      "y": 0
    },
    "size": "16px",
    "color": "white",
    "text": "Overlay Text"
  }
}'
