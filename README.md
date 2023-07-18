# README #


docker rm -vf $(docker ps -aq)
docker rmi -f $(docker images -aq)
docker system prune -a --volumes


# Run in Local #
docker build -t website662:987 -f infra-v4/local/Dockerfile.webapp.local .
docker run --publish 7050:7050 website662:987 

docker-compose -f infra-v4/local/docker-compose.yml up


# Run in production #
docker-compose -f infra-v5/local/docker-compose.yml up

#### docker-nginx-biolerplate
https://github.com/mgnisia/Boilerplate-Docker-Django-Gunicorn-Nginx


