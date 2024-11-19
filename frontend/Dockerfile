# Frontend Dockerfile
FROM node:18

# Set working directory inside the container
WORKDIR /app

# Install frontend dependencies
COPY package.json /app/
COPY package-lock.json /app/
RUN npm install

# Copy the frontend application files
COPY . /app/

# Expose the port used by your frontend app
EXPOSE 3000

# Command to run the frontend app
CMD ["npm", "start"]
