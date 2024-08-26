# Variables
APP_NAME=skf-tech-training-app
IMAGE_NAME=skf-tech-training-app

# Build the Docker image
build:
	docker build -t $(IMAGE_NAME) .

# Run the Docker container
run:
	docker run -d -p 5000:5000 --name $(APP_NAME) $(IMAGE_NAME)

# Stop the Docker container
stop:
	docker stop $(APP_NAME)

# Remove the Docker container
rm:
	docker rm $(APP_NAME)

# Rebuild the Docker image without using cache
rebuild:
	docker build --no-cache -t $(IMAGE_NAME) .

# View Docker logs
logs:
	docker logs -f $(APP_NAME)

# Clean up Docker images
clean:
	docker rmi $(IMAGE_NAME)