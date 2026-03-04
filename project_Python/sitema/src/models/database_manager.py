import sqlite3

class DatabaseManager:
    def __init__(self, db_path='/home/ubuntu/faculdade_vicente_sousa/faculdade.db'):
        self.db_path = db_path

    def get_connection(self):
        return sqlite3.connect(self.db_path)

    def execute_query(self, query, params=()):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return cursor.lastrowid

    def fetch_all(self, query, params=()):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()

    def fetch_one(self, query, params=()):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchone()

# Funções auxiliares para cada entidade
class Aluno:
    def __init__(self, db_manager):
        self.db = db_manager

    def listar(self):
        return self.db.fetch_all("SELECT e.id, e.nome, e.matricula, c.nome FROM estudantes e LEFT JOIN cursos c ON e.id_curso = c.id")

    def salvar(self, nome, matricula, cpf, data_nascimento, id_curso):
        query = "INSERT INTO estudantes (nome, matricula, cpf, data_nascimento, id_curso) VALUES (?, ?, ?, ?, ?)"
        return self.db.execute_query(query, (nome, matricula, cpf, data_nascimento, id_curso))

class Professor:
    def __init__(self, db_manager):
        self.db = db_manager

    def listar(self):
        return self.db.fetch_all("SELECT id, nome, cpf, email, especialidade FROM professores")

    def salvar(self, nome, cpf, email, especialidade):
        query = "INSERT INTO professores (nome, cpf, email, especialidade) VALUES (?, ?, ?, ?)"
        return self.db.execute_query(query, (nome, cpf, email, especialidade))

class Curso:
    def __init__(self, db_manager):
        self.db = db_manager

    def listar(self):
        return self.db.fetch_all("SELECT id, nome, duracao_semestres FROM cursos")

    def salvar(self, nome, duracao):
        query = "INSERT INTO cursos (nome, duracao_semestres) VALUES (?, ?)"
        return self.db.execute_query(query, (nome, duracao))

class Turma:
    def __init__(self, db_manager):
        self.db = db_manager

    def listar(self):
        query = """
        SELECT t.id, t.codigo, d.nome, p.nome, t.semestre_ano 
        FROM turmas t 
        JOIN disciplinas d ON t.id_disciplina = d.id 
        JOIN professores p ON t.id_professor = p.id
        """
        return self.db.fetch_all(query)
