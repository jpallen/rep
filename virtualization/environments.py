import docker
import subprocess
import os
import rep

docker_host = os.getenv("DOCKER_HOST", "http://localhost:4243")
c = docker.Client(base_url=docker_host, version="1.9")

def create(base_image_id, public_key=""):
	# Create a new image with unique public key credentials
	# to create the container from.
	image_id = rep.random_id()
	image_dir = os.path.join(rep.TMP_DIR, "images", image_id)
	subprocess.check_call(["mkdir", "-p", image_dir])

	dockerfile_path = os.path.join(image_dir, "Dockerfile")
	public_key_path = os.path.join(image_dir, "id_rsa.pub")
	with open(dockerfile_path, "w") as dockerfile:
		dockerfile.write("""
			FROM %s

			ADD id_rsa.pub /tmp/id_rsa.pub
			RUN cat /tmp/id_rsa.pub >> /root/.ssh/authorized_keys && rm -f /tmp/id_rsa.pub
		""" % base_image_id)
	with open(public_key_path, "w") as public_key_file:
		public_key_file.write(public_key)

	subprocess.check_call(
		["docker", "build", "-t", image_id, image_dir]
	)
	container_id = subprocess.check_output([
		"docker", "run", "-d", "-t", image_id, "/sbin/my_init"
	])
	container_id = container_id.decode("ascii").rstrip()

	return container_id

