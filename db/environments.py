import sqlite3
import db
conn = sqlite3.connect('rep.db')

def find(query={}):
	_init_environment_table()
	return db.find.find("environments", ["id", "docker_id", "private_key", "public_key"], query)

def create(env):
	_init_environment_table()
	c = conn.cursor()
	values = [env.id, env.docker_id, env.private_key, env.public_key]
	print(values)
	c.execute(
		"INSERT INTO environments (id, docker_id, private_key, public_key) VALUES (?, ?, ?, ?);",
		values
	)
	conn.commit()

def _init_environment_table():
	c = conn.cursor()
	c.execute("CREATE TABLE IF NOT EXISTS environments(id TEXT PRIMARY KEY, docker_id TEXT, private_key TEXT, public_key TEXT);")