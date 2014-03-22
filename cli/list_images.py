import sys
from engine import Image
from tabulate import tabulate

def run(argv):
	images = Image.find()
	headers = ["ID", "Docker ID"]
	rows = []
	for image in images:
		rows.append([image.id, image.docker_id])
	print(tabulate(rows, headers))
	sys.exit(0)
