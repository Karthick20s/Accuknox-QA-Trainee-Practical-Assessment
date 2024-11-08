# Use Node.js image with Bash support
FROM node:18-bullseye

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json files
COPY package*.json ./

# Install application dependencies
RUN npm install

# Copy the application code
COPY . .

# Expose the application port
EXPOSE 3000

# Ensure the Bash script is executable
RUN chmod +x wisecow.sh

# Start the application with the Bash script
CMD ["./wisecow.sh"]

RUN apt-get update && apt-get install -y curl bash git
