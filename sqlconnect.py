import sqlite3

try:
	
	# Connect to DB and create a cursor
	sqliteConnection = sqlite3.connect("C:\Users\HP\Documents\dB browser\Pawan.sqlite3")
	cursor = sqliteConnection.cursor()
	print('DB Init')

	# Write a query and execute it with cursor
	query = 'select sqlite_version()'
	cursor.execute(query)

	# Fetch and output result
	result = cursor.fetchall()
	print('data is is {}'.format(result))

	# Close the cursor
	cursor.close()

# Handle errors
except sqlite3.Error as error:
	print('Error occured - ', error)

# Close DB Connection irrespective of success
# or failure
finally:
	
	if sqliteConnection:
		sqliteConnection.close()
		print('SQLite Connection closed')
