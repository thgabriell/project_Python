import tkinter as tk
from tkinter import ttk, messagebox
from src.models.database_manager import DatabaseManager, Aluno, Curso, Professor

class CRUDView:
    def __init__(self, parent, db_manager):
        self.parent = parent
        self.db = db_manager
        self.colors = {"bg": "#f5f6fa", "primary": "#2c3e50", "accent": "#3498db"}

    def setup_header(self, title):
        header = tk.Frame(self.parent, bg=self.colors["bg"])
        header.pack(fill="x", padx=20, pady=20)
        tk.Label(header, text=title, font=("Arial", 20, "bold"), bg=self.colors["bg"]).pack(side="left")

    def create_table(self, columns):
        table_frame = tk.Frame(self.parent, bg="white")
        table_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)
        
        self.tree.pack(side="left", fill="both", expand=True)
        
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

class EstudantesView(CRUDView):
    def render(self):
        self.setup_header("Gestão de Estudantes")
        
        # Botões de Ação
        btn_frame = tk.Frame(self.parent, bg=self.colors["bg"])
        btn_frame.pack(fill="x", padx=20)
        tk.Button(btn_frame, text="+ Novo Estudante", bg=self.colors["accent"], fg="white", 
                  command=self.novo_estudante).pack(side="left", padx=5)
        
        self.create_table(("ID", "Nome", "Matrícula", "Curso"))
        self.atualizar_lista()

    def atualizar_lista(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        aluno_model = Aluno(self.db)
        for row in aluno_model.listar():
            self.tree.insert("", "end", values=row)

    def novo_estudante(self):
        # Janela de Cadastro Simplificada
        win = tk.Toplevel(self.parent)
        win.title("Cadastrar Estudante")
        win.geometry("400x300")
        
        tk.Label(win, text="Nome:").pack(pady=5)
        ent_nome = tk.Entry(win)
        ent_nome.pack()
        
        tk.Label(win, text="Matrícula:").pack(pady=5)
        ent_mat = tk.Entry(win)
        ent_mat.pack()
        
        def salvar():
            if ent_nome.get() and ent_mat.get():
                aluno_model = Aluno(self.db)
                # CPF e Data fixos para simplificação do exemplo
                aluno_model.salvar(ent_nome.get(), ent_mat.get(), "000.000.000-00", "2000-01-01", 1)
                messagebox.showinfo("Sucesso", "Estudante cadastrado!")
                win.destroy()
                self.atualizar_lista()
            else:
                messagebox.showerror("Erro", "Preencha todos os campos")
        
        tk.Button(win, text="Salvar", command=salvar).pack(pady=20)

class CursosView(CRUDView):
    def render(self):
        self.setup_header("Gestão de Cursos")
        btn_frame = tk.Frame(self.parent, bg=self.colors["bg"])
        btn_frame.pack(fill="x", padx=20)
        tk.Button(btn_frame, text="+ Novo Curso", bg=self.colors["accent"], fg="white", 
                  command=self.novo_curso).pack(side="left", padx=5)
        
        self.create_table(("ID", "Nome", "Duração (Semestres)"))
        self.atualizar_lista()

    def atualizar_lista(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        curso_model = Curso(self.db)
        for row in curso_model.listar():
            self.tree.insert("", "end", values=row)

    def novo_curso(self):
        win = tk.Toplevel(self.parent)
        win.title("Cadastrar Curso")
        win.geometry("400x300")
        
        tk.Label(win, text="Nome do Curso:").pack(pady=5)
        ent_nome = tk.Entry(win)
        ent_nome.pack()
        
        tk.Label(win, text="Duração (Semestres):").pack(pady=5)
        ent_dur = tk.Entry(win)
        ent_dur.pack()
        
        def salvar():
            if ent_nome.get() and ent_dur.get():
                curso_model = Curso(self.db)
                curso_model.salvar(ent_nome.get(), int(ent_dur.get()))
                messagebox.showinfo("Sucesso", "Curso cadastrado!")
                win.destroy()
                self.atualizar_lista()
            else:
                messagebox.showerror("Erro", "Preencha todos os campos")
        
        tk.Button(win, text="Salvar", command=salvar).pack(pady=20)
