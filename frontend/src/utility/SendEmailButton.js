import React from 'react';
import axios from 'axios';
import Cookies from 'js-cookie';
import { getEmailApiUrl } from '../config/apiConfig';

const SendEmailButton = ({ className }) => {
    const handleSendEmail = async () => {
        // Use the dynamic API URL from apiConfig
        const apiUrl = getEmailApiUrl(); // Get the dynamic API URL
        try {
            const csrfToken = Cookies.get('csrftoken');
            console.log('CSRF Token:', csrfToken);
            console.log('API URL:', apiUrl);

            const response = await axios.post(`${apiUrl}/send_email/`, {}, {
                headers: {
                    'X-CSRFToken': csrfToken,
                    'Content-Type': 'application/json',
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
        <button className={`btn btn-success ${className}`} onClick={handleSendEmail}>
            Send Email
        </button>
    );
};

export default SendEmailButton;
