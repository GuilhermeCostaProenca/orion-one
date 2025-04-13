import sqlite3
from datetime import datetime

def criar_banco():
    conn = sqlite3.connect('orion.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS comandos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            texto TEXT,
            data TEXT
        )
    ''')
    conn.commit()
    conn.close()

def inserir_comando(texto):
    conn = sqlite3.connect('orion.db')
    cursor = conn.cursor()
    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('INSERT INTO comandos (texto, data) VALUES (?, ?)', (texto, data))
    conn.commit()
    conn.close()

def buscar_comandos():
    conn = sqlite3.connect('orion.db')
    cursor = conn.cursor()
    cursor.execute('SELECT texto, data FROM comandos ORDER BY id DESC LIMIT 10')
    comandos = cursor.fetchall()
    conn.close()
    return comandos
