import sqlite3
import db
conn = sqlite3.connect('rep.db')

def find():
	c = conn.cursor()
	_init_environment_table(c)
	images = c.execute("SELECT id, docker_id, private_key, public_key FROM environments")

	return list(map(
		lambda i: dict(
			id=i[0], docker_id=i[1], private_key=i[2], public_key=i[3]
		),
		images
	))

def create(env):
	c = conn.cursor()
	_init_environment_table(c)
	values = [env.id, env.docker_id, env.private_key, env.public_key]
	print(values)
	c.execute(
		"INSERT INTO environments (id, docker_id, private_key, public_key) VALUES (?, ?, ?, ?);",
		values
	)
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
	c.execute("CREATE TABLE IF NOT EXISTS environments(id TEXT PRIMARY KEY, docker_id TEXT, private_key TEXT, public_key TEXT);")