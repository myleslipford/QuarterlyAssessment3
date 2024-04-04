import sqlite3

# Connect to the SQLite database (or create it if not exists)
conn = sqlite3.connect('QuestionsDatabase.db')
cursor = conn.cursor()

