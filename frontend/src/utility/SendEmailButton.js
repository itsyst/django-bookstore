import React, { useState } from 'react';
import axios from 'axios';
import Cookies from 'js-cookie';
import { getEmailApiUrl } from '../config/apiConfig';

const SendEmailButton = ({ className }) => {
    const [file, setFile] = useState(null);

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
                alert('Please select a file to attach');
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
                alert('Email sent successfully!');
            } else {
                alert('Failed to send email.');
            }
        } catch (error) {
            console.error('Error sending email:', error);
            alert('An error occurred while sending the email.');
        }
    };

    return (
        <div className='mt-3'>
            <input type="file" onChange={handleFileChange} className='mb-3 form-control' />
            <button className={`btn btn-success ${className}`} onClick={handleSendEmail}>
                Send Email
            </button>
        </div>
    );
};

export default SendEmailButton;
