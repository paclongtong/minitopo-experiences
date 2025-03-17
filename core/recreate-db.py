import sqlite3
import os

# Define the database path (change this if needed)
db_path = "/home/paul/data_quiche/db_template/db_template.db"

# Connect to SQLite (creates the file if it doesn't exist)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create tables

# Table: Stores different network topologies as JSON
cursor.execute("""
CREATE TABLE IF NOT EXISTS topologies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    topology TEXT NOT NULL  -- JSON representation of topology
)
""")

# Table: Temporary data storage for experiment repetitions
cursor.execute("""
CREATE TABLE IF NOT EXISTS temp_repetition_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    topology_id INTEGER NOT NULL,
    cc_algorithm TEXT NOT NULL,
    transfer_time REAL NOT NULL,
    FOREIGN KEY (topology_id) REFERENCES topologies (id)
)
""")

# Table: Stores the median transfer time per topology and congestion control algorithm
cursor.execute("""
CREATE TABLE IF NOT EXISTS median_transfer_time (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    topology_id INTEGER NOT NULL,
    cc_algorithm TEXT NOT NULL,
    median_time REAL NOT NULL,
    FOREIGN KEY (topology_id) REFERENCES topologies (id)
)
""")

# Commit changes and close connection
conn.commit()
conn.close()

print("Database and tables successfully recreated!")
