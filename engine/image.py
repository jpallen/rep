import subprocess
import db
import engine
from virtualization.images import import_tar_stream

class Image:
	@classmethod
	def create_from_tar_stream(cls, stream):
		docker_id = import_tar_stream(stream)
		image = Image(new=True, docker_id=docker_id)
		image.save()
		return image

	@classmethod
	def find(cls, options={}):
		images = db.images.find()
		return map(Image.build, images)

	@classmethod
	def build(cls, attributes):
		return Image(**attributes)

	def __init__(self, new=False, id=None, docker_id=None):
		self.id = id if id is not None else engine.random_id()
		self.docker_id = docker_id
		self.new = new

	def save(self):
		if self.new:
			self.new = False
			db.images.create(self.id, self.docker_id)
