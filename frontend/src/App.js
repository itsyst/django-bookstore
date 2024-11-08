import React, { useState } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import { getDynamicApiUrl } from './config/apiConfig';
import SendEmailButton from './utility/SendEmailButton';

const App = () => {
  const [file, setFile] = useState(null);
  const [progress, setProgress] = useState(0);
  const [alertMessage, setAlertMessage] = useState(null);
  const [alertType, setAlertType] = useState(null);

  // Function to show alert messages
  const showAlert = (message, type) => {
    setAlertMessage(message);
    setAlertType(type);
    setTimeout(() => {
      setAlertMessage(null);
      setAlertType(null);
    }, 3000); // Hide alert after 3 seconds
  };

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (!file) return;

    setProgress(0);

    // Use the dynamic API URL from apiConfig
    const apiUrl = getDynamicApiUrl(); // Get the dynamic API URL

    const formData = new FormData();
    formData.append('image', file);

    try {
      await axios.post(apiUrl, formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
        onUploadProgress: (progressEvent) => {
          const { loaded, total } = progressEvent;
          const targetProgress = Math.round((loaded / total) * 100);

          // Gradually increase progress
          const increaseProgress = (currentProgress) => {
            if (currentProgress < targetProgress) {
              setProgress(currentProgress);
              setTimeout(() => increaseProgress(currentProgress + 1), 50); // Slow down progress update to 50ms
            } else {
              setProgress(targetProgress);
              // Show alert after progress is fully completed
              if (targetProgress === 100) {
                showAlert('Image successfully uploaded!', 'success');
                // Hide progress bar after 1 second
                setTimeout(() => {
                  setProgress(0); // Reset progress to hide the bar
                }, 1000); // 1 second delay before hiding
              }
            }
          };

          increaseProgress(progress);
        },
      });
    } catch (err) {
      if (err.response && err.response.data && err.response.data.image) {
        showAlert(err.response.data.image[0], 'danger');
      } else if (err.request) {
        showAlert('Could not reach the server!', 'danger');
      } else {
        showAlert('An unexpected error occurred!', 'danger');
      }
    } finally {
      setFile(null); // Reset file input after upload
    }
  };

  return (
    <div className="container">
      {/* Alert */}
      {alertMessage && (
        <div className={`alert alert-${alertType}`} role="alert">
          {alertMessage}
        </div>
      )}

      {/* Progress Bar */}
      <div className={`progress ${progress > 0 ? '' : 'd-none'}`}>
        <div
          className="progress-bar"
          role="progressbar"
          style={{ width: `${progress}%` }}
          aria-valuenow={progress}
          aria-valuemin="0"
          aria-valuemax="100"
        ></div>
      </div>

      {/* File Upload Form */}
      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <label htmlFor="image" className="form-label">
            Select an image:
          </label>
          <input
            id="image"
            type="file"
            className="form-control"
            accept="image/png, image/jpeg"
            onChange={handleFileChange}
          />
        </div>
        <button className="btn btn-primary me-3" type="submit" disabled={!file}>
          Upload
        </button>
        <SendEmailButton />
      </form>
    </div>
  );
};

export default App;
