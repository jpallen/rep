import sys
from rep import Image

def run(argv):
	image = Image.create_from_tar_stream(sys.stdin.buffer)
	print("IMAGE ID = %s" % image.id)
	print("DOCKER ID = %s" % image.docker_id)
	sys.exit(0)
