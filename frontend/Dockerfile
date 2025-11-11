# --- Stage 1: Build ---
# ... (This part is unchanged)
FROM node:22.15.0-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# --- Stage 2: Production (This is the UPDATED part) ---
FROM nginx:stable-alpine

# Set this to your 'base' path, (e.g., 'my-app' if base is '/my-app/')
# Make sure there are NO slashes here.
ENV APP_BASE=whoisit

# Create the subdirectory inside Nginx's html root
RUN mkdir -p /usr/share/nginx/html/${APP_BASE}

# Copy the built assets INTO that new subdirectory
COPY --from=builder /app/dist /usr/share/nginx/html/${APP_BASE}

# Copy the updated Nginx configuration
COPY docker/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]