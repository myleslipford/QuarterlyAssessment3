import sqlite3

# Connect to the SQLite database (or create it if not exists)
conn = sqlite3.connect('QuestionsDatabase.db')
cursor = conn.cursor()

# Create tables for different categories
categories = [
    'Business Statistics',
    'Business Database mgmt Science',
    'General Biology II',
    'Mgmt organization Behavior',
    'Business Applications'
]

for category in categories:
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {category.replace(" ", "_")} (
            id INTEGER PRIMARY KEY,
            question TEXT,
            option1 TEXT, 
            option2 TEXT, 
            option3 TEXT, 
            option4 TEXT,
            answer TEXT
        )
    ''')
