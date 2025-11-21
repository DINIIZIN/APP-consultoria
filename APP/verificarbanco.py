import sqlite3

conn = sqlite3.connect("Consultoria.db")
cursor = conn.cursor()

# Ver estrutura da tabela
cursor.execute("PRAGMA table_info(usuarios)")
print("📋 Estrutura da tabela:")
for col in cursor.fetchall():
    print(col)

# Ver dados existentes
cursor.execute("SELECT * FROM usuarios")
print("\n📦 Dados existentes:")
print(cursor.fetchall())

conn.close()