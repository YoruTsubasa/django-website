# Build Docker image with name my_website
docker build --no-cache -t my_website .

# Run Docker container from image named my_website and make the container listen on port 5000. Host port is also set to 5000
docker run -p 5000:8000 my_website