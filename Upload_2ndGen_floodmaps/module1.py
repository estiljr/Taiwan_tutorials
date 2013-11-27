import psycopg2
import pprint

conn_string = "host=UKSD2F0W3J dbname=taiwan user=taiwan_user password=taiwan"
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()
cursor.execute("SELECT * FROM bg_gi.second_gen_flood_maps")
rows = cursor.fetchall()
pprint.pprint(rows)