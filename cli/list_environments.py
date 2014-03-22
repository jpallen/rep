import sys
from rep import Environment
from tabulate import tabulate

def run(argv):
	envs = Environment.find()
	headers = ["ID", "Docker ID", "State", "IP Address"]
	rows = []
	for env in envs:
		rows.append([env.id, env.docker_id, env.state, env.ip_address])
	print(tabulate(rows, headers))
	sys.exit(0)
