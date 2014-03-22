#!/usr/bin/env python3

import cli
import sys
import textwrap

if (len(sys.argv) >= 2):
	[base, command] = sys.argv[0:2]
	if command == "import-image":
		cli.import_image.run(sys.argv[2:])
	elif command == "list-images":
		cli.list_images.run(sys.argv[2:])
	elif command == "create-environment":
		cli.create_environment.run(sys.argv[2:])

help_text = textwrap.dedent("""
	Usage: rep COMMAND

	Available commands:

	rep import-image < image.tar

	rep create-environment [--from-image IMAGE_ID]
""")
print(help_text)