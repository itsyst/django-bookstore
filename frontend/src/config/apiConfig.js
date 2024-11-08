// Define the base API URL
const BASE_URL = 'http://127.0.0.1:8000'; // Your backend base URL

export const getBookImageUploadUrl = (bookId) => {
    // Construct the API URL based on the book ID
    return `${BASE_URL}/books/${bookId}/images/`;
};

export const getDynamicApiUrl = () => {
    // This function constructs the dynamic API URL from the current frontend URL
    const currentUrl = window.location.href; // e.g., http://127.0.0.1:3000/books/1/images
    const bookId = currentUrl.split('/').slice(-2, -1)[0]; // Extract book ID from the URL
    return getBookImageUploadUrl(bookId); // Use the extracted book ID
};

export const getEmailApiUrl = () => `${BASE_URL}/messages`;