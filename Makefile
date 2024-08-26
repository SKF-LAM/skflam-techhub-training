# Build and start the Docker Compose services
up:
	docker-compose up --build

# Stop the Docker Compose services
down:
	docker-compose down

# Rebuild the Docker Compose services without cache
rebuild:
	docker-compose up --build --force-recreate

# View logs from the running services
logs:
	docker-compose logs -f

# Stop and remove containers, networks, volumes, and images
clean:
	docker-compose down -v --rmi all

.PHONY: up down rebuild logs clean