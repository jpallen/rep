import sqlite3
conn = sqlite3.connect('rep.db')

def create_image(image_sha, docker_id):
	c = conn.cursor()
	_init_image_table(c)
	c.execute("INSERT INTO images (id, docker_id) VALUES (?, ?);", [image_sha, docker_id])
	conn.commit()

def _init_image_table(c):
	c.execute("CREATE TABLE IF NOT EXISTS images(id TEXT PRIMARY KEY, docker_id TEXT);")