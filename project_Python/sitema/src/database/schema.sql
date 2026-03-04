-- Tabela de Cursos
CREATE TABLE IF NOT EXISTS cursos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    duracao_semestres INTEGER NOT NULL
);

-- Tabela de Professores
CREATE TABLE IF NOT EXISTS professores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf TEXT UNIQUE NOT NULL,
    email TEXT,
    especialidade TEXT
);

-- Tabela de Estudantes
CREATE TABLE IF NOT EXISTS estudantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    matricula TEXT UNIQUE NOT NULL,
    cpf TEXT UNIQUE NOT NULL,
    data_nascimento DATE,
    id_curso INTEGER,
    FOREIGN KEY (id_curso) REFERENCES cursos(id)
);

-- Tabela de Disciplinas
CREATE TABLE IF NOT EXISTS disciplinas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    carga_horaria INTEGER NOT NULL,
    id_curso INTEGER,
    FOREIGN KEY (id_curso) REFERENCES cursos(id)
);

-- Tabela de Turmas
CREATE TABLE IF NOT EXISTS turmas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo TEXT UNIQUE NOT NULL,
    id_disciplina INTEGER,
    id_professor INTEGER,
    semestre_ano TEXT NOT NULL, -- Ex: 2024.1
    FOREIGN KEY (id_disciplina) REFERENCES disciplinas(id),
    FOREIGN KEY (id_professor) REFERENCES professores(id)
);

-- Tabela de Matrículas em Turmas
CREATE TABLE IF NOT EXISTS matriculas_turmas (
    id_estudante INTEGER,
    id_turma INTEGER,
    nota_1 REAL DEFAULT 0,
    nota_2 REAL DEFAULT 0,
    media REAL DEFAULT 0,
    frequencia REAL DEFAULT 100,
    PRIMARY KEY (id_estudante, id_turma),
    FOREIGN KEY (id_estudante) REFERENCES estudantes(id),
    FOREIGN KEY (id_turma) REFERENCES turmas(id)
);

-- Tabela de Diário de Aula
CREATE TABLE IF NOT EXISTS diario_aula (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_turma INTEGER,
    data_aula DATE NOT NULL,
    conteudo TEXT,
    FOREIGN KEY (id_turma) REFERENCES turmas(id)
);
