import sqlite3
import db
conn = sqlite3.connect('rep.db')

def find(query={}):
	_init_image_table()
	return db.find.find("images", ["id", "docker_id"], query)

def create(image_sha, docker_id):
	_init_image_table()
	c = conn.cursor()
	c.execute("INSERT INTO images (id, docker_id) VALUES (?, ?);", [image_sha, docker_id])
	conn.commit()

def _init_image_table():
	c = conn.cursor()
	c.execute("CREATE TABLE IF NOT EXISTS images(id TEXT PRIMARY KEY, docker_id TEXT);")