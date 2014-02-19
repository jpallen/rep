import sqlite3
import db
conn = sqlite3.connect('rep.db')

def create_environment(environment_sha, docker_id):
	c = conn.cursor()
	_init_environment_table(c)
	c.execute("INSERT INTO environments (id, docker_id) VALUES (?, ?);", [environment_sha, docker_id])
	conn.commit()

def get_docker_environment_id(environment_id):
	c = conn.cursor()
	_init_environment_table(c)
	c.execute("SELECT docker_id FROM environments WHERE id=?", [environment_id])
	row = c.fetchone()
	if row is None:
		raise db.NotFound("environment with id '%s' does not exist" % environment_id)
	return row[0]

def _init_environment_table(c):
	c.execute("CREATE TABLE IF NOT EXISTS environment(id TEXT PRIMARY KEY, docker_id TEXT);")