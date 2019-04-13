import sqlite3

def db_execute(query, tuple_of_values):
	conn = sqlite3.connect(DB_NAME)
	c = conn.cursor()
	c.execute(query, tuple_of_values)
	last_row_id = c.lastrowid
	conn.commit()
	conn.close()
	return last_row_id

def db_select(query, tuple_of_values, only_one=False):
	conn = sqlite3.connect(DB_NAME)
	c = conn.cursor()
	if only_one:
		result = c.execute(query, tuple_of_values).fetchone()
	else:
		result = c.execute(query, tuple_of_values).fetchall()
	conn.close()

return result