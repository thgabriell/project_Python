import sqlite3
import os

def init_db(db_path='/home/ubuntu/faculdade_vicente_sousa/faculdade.db'):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Ler o esquema SQL
    schema_path = '/home/ubuntu/faculdade_vicente_sousa/src/database/schema.sql'
    with open(schema_path, 'r') as f:
        sql_script = f.read()
    
    # Executar o script
    cursor.executescript(sql_script)
    
    # Inserir alguns dados de exemplo (opcional)
    cursor.execute("INSERT OR IGNORE INTO cursos (nome, duracao_semestres) VALUES ('Engenharia de Software', 8)")
    cursor.execute("INSERT OR IGNORE INTO cursos (nome, duracao_semestres) VALUES ('Administração', 8)")
    cursor.execute("INSERT OR IGNORE INTO cursos (nome, duracao_semestres) VALUES ('Direito', 10)")
    
    conn.commit()
    conn.close()
    print("Banco de dados inicializado com sucesso!")

if __name__ == "__main__":
    init_db()
