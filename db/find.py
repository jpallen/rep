import sqlite3

conn = sqlite3.connect('rep.db')

def find(table, columns, query):
	c = conn.cursor()

	query_str = "SELECT %s FROM %s" % (", ".join(columns), table)
	values = []

	if (len(query) > 0):
		query_str += " WHERE "
		conditions = []
		for key in query:
			if key in columns:
				conditions.append("%s=?" % key)
				values.append(query[key])
		query_str += " AND ".join(conditions)

	results = c.execute(query_str, values)

	return list(map(
		lambda i: dict(zip(columns, i)),
		results
	))