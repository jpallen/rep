import sys
import subprocess
import argparse
import rep
from rep import Environment

def run(argv):
	parser = argparse.ArgumentParser(description='Connect to a running environment')
	parser.add_argument("environment",
	                    metavar="[host:]environment",
	                    help="The environment to connect to")
	args = parser.parse_args(argv)
	env = Environment.findOne({"id": args.environment})

	if env is None:
		print("No environment found: %s", args.environment)
		sys.exit(1)

	ip_address = env.ip_address
	print("Connecting to %s at %s" % (env.id, ip_address))

	subprocess.check_call(["ssh-add", env.private_key_path])

	ssh_command = rep.SSH_PROXY + ["ssh", "-o", "StrictHostKeyChecking=no", "root@%s" % ip_address]
	subprocess.check_call(ssh_command)

	sys.exit(0)
