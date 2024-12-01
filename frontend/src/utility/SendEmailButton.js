import React, { useState } from 'react';
import axios from 'axios';
import Cookies from 'js-cookie';
import { getEmailApiUrl } from '../config/apiConfig';

const SendEmailButton = ({ className }) => {
    const [file, setFile] = useState(null);
    const [statusMessage, setStatusMessage] = useState(null);
    const [statusType, setStatusType] = useState(null);

    const handleFileChange = (event) => {
        setFile(event.target.files[0]);
    };

    const handleSendEmail = async () => {
        // Use the dynamic API URL from apiConfig
        const apiUrl = getEmailApiUrl(); // Get the dynamic API URL
        try {
            const csrfToken = Cookies.get('csrftoken');
            console.log('CSRF Token:', csrfToken);
            console.log('API URL:', apiUrl);

            if (!file) {
                setStatusMessage('Please select a file to attach.');
                setStatusType('warning');
                return
            }

            // Create form data to include the file
            const formData = new FormData();
            formData.append('attachment', file);  // Add the file to the form data

            const response = await axios.post(`${apiUrl}/send_email/`, formData, {
                headers: {
                    'X-CSRFToken': csrfToken,
                    // 'Content-Type': 'application/json',
                },
                withCredentials: true, // This allows sending cookies with requests
            });

            if (response.status === 200) {
                const { data } = response.data;
                setStatusMessage(`Email sent successfully! Message: ${data.message}.`);
                (data.is_cached) ? setStatusType('success') : setStatusType('info');
            } else {
                setStatusMessage('Failed to send email. Please try again.');
                setStatusType('danger');
            }

        } catch (error) {
            console.error('Error sending email:', error);

            // Handle specific error cases
            if (error.response) {
                setStatusMessage(error.response.data.message || 'Failed to send email.');
            } else if (error.request) {
                setStatusMessage('Could not reach the server. Please try again later.');
            } else {
                setStatusMessage('An unexpected error occurred.');
            }

            setStatusType('danger');
        }
    };

    return (
        <div className='mt-3'>
            <input type="file" onChange={handleFileChange} className='mb-3 form-control' />
            <button className={`mb-3 btn btn-success ${className}`} onClick={handleSendEmail}>
                Send Email
            </button>

            {/* Status Message */}
            {statusMessage && (
                <div className={`alert alert-${statusType}`} role="alert">
                    {statusMessage}
                </div>
            )}
        </div>
    );
};

export default SendEmailButton;
