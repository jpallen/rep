import sys
import argparse
import rep
from rep import Environment

def run(argv):
	parser = argparse.ArgumentParser(description='Stop a running environment')
	parser.add_argument("environment",
	                    metavar="[host:]environment",
	                    help="The environment to stop")
	args = parser.parse_args(argv)
	env = Environment.findOne({"id": args.environment})

	if env.state != "running":
		print("%s is not running." % env.id)
		sys.exit(1)

	print("Stopping %s..." % env.id)
	env.stop()
	print("Done")

	sys.exit(0)
