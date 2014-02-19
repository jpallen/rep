import virtualization
import db
import engine

class Environment:
	@classmethod
	def create_from_image_id(self, image_id, name=None):
		docker_image_id = db.images.get_docker_image_id(image_id)
		docker_container_id = virtualization.environments.create(docker_image_id)
		env = Environment(new=True, docker_id=docker_container_id)
		return env

	def __init__(self, new=False, id=None, docker_id=None):
		self.id = id if id is not None else engine.random_id()
		self.docker_id = docker_id
		self.new = new

	def save(self):
		if self.new:
			self.new = False
			db.environments.create_environment(self.id, self.docker_id)