import sys
import argparse
import rep
from rep import Environment

def run(argv):
	parser = argparse.ArgumentParser(description='Start a running environment')
	parser.add_argument("environment",
	                    metavar="[host:]environment",
	                    help="The environment to start")
	args = parser.parse_args(argv)
	env = Environment.findOne({"id": args.environment})

	if env.state == "running":
		print("%s is already running." % env.id)
		sys.exit(1)

	print("Starting %s..." % env.id)
	env.start()
	print("Done")

	sys.exit(0)
