import docker

c = docker.Client(base_url='http://localhost:4243', version="1.9")

def create(docker_environment_id):
	result = c.create_container(docker_environment_id, command=["/sbin/my_init"])
	return result['Id']

