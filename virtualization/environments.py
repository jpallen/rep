import docker
import os

docker_host = os.getenv("DOCKER_HOST", 'http://localhost:4243')

c = docker.Client(base_url=docker_host, version="1.9")

def create(docker_environment_id):
	result = c.create_container(docker_environment_id, command=["/sbin/my_init"])
	return result['Id']

