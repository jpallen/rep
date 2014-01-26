import subprocess

def import_tar_stream(stream, chunk_size=1024):
	proc = subprocess.Popen(["docker", "import", "-"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	while True:
		chunk = stream.read(chunk_size)
		if not chunk:
			break
		proc.stdin.write(chunk)
	proc.stdin.close()
	proc.wait()
	docker_id = proc.stdout.read().decode("ascii").rstrip()
	return docker_id
