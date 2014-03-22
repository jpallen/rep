import sys
import argparse
from rep import Environment

def run(argv):
	parser = argparse.ArgumentParser(description='Create an environment from an existing image')
	parser.add_argument("--from-image", "-i",
	                    metavar="[host:]image_name",
	                    help="The location of the image",
	                    dest="image")
	args = parser.parse_args(argv)
	environment = Environment.create_from_image_id(args.image)
	print("ENVIRONMENT ID = %s" % environment.id)
	print("DOCKER ID = %s" % environment.docker_id)
	sys.exit(0)