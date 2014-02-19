import sqlite3
import db
conn = sqlite3.connect('rep.db')

def create_image(image_sha, docker_id):
	c = conn.cursor()
	_init_image_table(c)
	c.execute("INSERT INTO images (id, docker_id) VALUES (?, ?);", [image_sha, docker_id])
	conn.commit()

def get_docker_image_id(image_id):
	c = conn.cursor()
	_init_image_table(c)
	c.execute("SELECT docker_id FROM images WHERE id=?", [image_id])
	row = c.fetchone()
	if row is None:
		raise db.NotFound("image with id '%s' does not exist" % image_id)
	return row[0]

def _init_image_table(c):
	c.execute("CREATE TABLE IF NOT EXISTS images(id TEXT PRIMARY KEY, docker_id TEXT);")