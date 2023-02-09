# Use the official MongoDB image as the base image
FROM mongo:latest

# Set the working directory to /app
WORKDIR /app

# Copy the data files to the container
COPY data/db /data/db

# Expose port 27017
EXPOSE 27017

# Start the MongoDB service
CMD ["mongod"]
