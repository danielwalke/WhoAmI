# --- Stage 1: Build ---
# Use the exact Node.js version you specified
FROM node:22.15.0-alpine AS builder

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json first
# This leverages Docker's layer caching. If these files don't change,
# Docker won't reinstall dependencies on every build.
COPY package*.json ./

# Install project dependencies
RUN npm install

# Copy all the remaining project files (src, public, vite.config.js, etc.)
COPY . .

# Run the build script (defined in your package.json)
# This creates the /app/dist directory with your static files.
RUN npm run build

# --- Stage 2: Production ---
# Use a lightweight Nginx image for serving the static content
FROM nginx:stable-alpine

# Copy the built assets from the 'builder' stage
COPY --from=builder /app/dist /usr/share/nginx/html

# Copy the custom Nginx configuration
# This file is necessary to handle Vue's client-side routing (SPA)
# It tells Nginx to redirect all 404s to index.html
COPY docker/nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80 to the outside world
EXPOSE 80

# Command to run Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]
