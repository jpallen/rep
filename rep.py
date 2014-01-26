import cli
import sys
import textwrap

if (len(sys.argv) >= 2):
	base = sys.argv.pop(0)
	if sys.argv[0:2] == ["image", "create"]:
		argv = sys.argv[2:]
		cli.image.create.run(argv)

help_text = textwrap.dedent("""
	Usage: rep.py COMMAND

	Available commands:

	rep image create DOCKER_IMAGE_ID
""")
print(help_text)
