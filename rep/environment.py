import virtualization
import db
import rep
import subprocess
import os
import rep

class Environment:
	@classmethod
	def create_from_image_id(cls, image_id, name=None):
		env = Environment(new=True)
		env._generate_ssh_keys()
		docker_image_id = db.images.get_docker_image_id(image_id)
		env.docker_id = virtualization.environments.create(docker_image_id, public_key=env.public_key)
		env.save()
		return env

	@classmethod
	def find(cls):
		envs = db.environments.find()
		return map(Environment.build, envs)

	@classmethod
	def build(cls, attributes):
		return Environment(**attributes)

	def __init__(self, new=False, id=None, docker_id=None, private_key=None, public_key=None):
		self.id = id if id is not None else rep.random_id()
		self.docker_id = docker_id
		self.private_key = private_key
		self.public_key = public_key
		self.new = new

	@property
	def ip_address(self):
		return virtualization.environments.get_ip_address(self.docker_id)

	@property
	def state(self):
		return virtualization.environments.get_state(self.docker_id)

	def save(self):
		if self.new:
			self.new = False
			db.environments.create(self)

	def _generate_ssh_keys(self):
		keys_dir = os.path.join(rep.TMP_DIR, "keys")
		key_path = os.path.join(keys_dir, self.id)
		public_key_path = key_path + ".pub"
		subprocess.check_call(["mkdir", "-p", keys_dir])
		subprocess.check_call(["ssh-keygen", "-f", key_path, "-P", "", "-C", self.id])

		with open(key_path, 'r') as private_key:
			self.private_key = private_key.read()
		with open(public_key_path, 'r') as public_key:
			self.public_key = public_key.read()
