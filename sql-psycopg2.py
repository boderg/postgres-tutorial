import psycopg2


# Connect to 'chinook' database
connection = psycopg2.connect(database="chinook")

# Build a cursor object of the database
cursor = connection.cursor()

# Query 1 - select all records from the "artist" table
# cursor.execute('SELECT * FROM "artist"')

# Query 2 - select only the "name" column from the "artist" table
# cursor.execute('SELECT "name" FROM "artist"')

# Query 3 - select only "Queen" from the "artist" table
# cursor.execute('SELECT * FROM "artist" WHERE "name" =%s', ["Queen"])

# Query 4 - select only the "artist_id" #51 from the "artist" table
# cursor.execute('SELECT * FROM "artist" WHERE "artist_id" =%s', [51])

# Query 5 - select only the albums with "artist_id" #51 from the "artist" table
# cursor.execute('SELECT * FROM "album" WHERE "artist_id" =%s', [51])

# Query 6 - select all tracks where the composer is "Queen" from the "track" table
# cursor.execute('SELECT * FROM "track" WHERE "composer" =%s', ["Queen"])

# Query 7 - select all albums where the name is "Metallica" from the "artist" table
cursor.execute('SELECT * FROM "album" WHERE "name" =%s', ["Metallica"])

# Fetch the results (multiple)
results = cursor.fetchall()

# Fetch the result (single)
# results = cursor.fetchone()

# Close the connection
connection.close()

# Print results
for result in results:
    print(result)
