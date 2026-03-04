import sys
import os

# Adicionar o diretório atual ao path para importação
sys.path.append(os.getcwd())

import tkinter as tk
from tkinter import ttk, messagebox
from src.ui.main_window import MainWindow
from src.ui.crud_views import EstudantesView, CursosView
from src.models.database_manager import DatabaseManager, Professor, Turma
from src.reports.report_generator import ReportGenerator

class FaculdadeApp(MainWindow):
    def __init__(self):
        self.db = DatabaseManager()
        self.report_gen = ReportGenerator(self.db)
        super().__init__()

    def show_estudantes(self):
        self.clear_content()
        view = EstudantesView(self.content_frame, self.db)
        view.render()

    def show_cursos(self):
        self.clear_content()
        view = CursosView(self.content_frame, self.db)
        view.render()

    def show_professores(self):
        self.clear_content()
        tk.Label(self.content_frame, text="Gestão de Professores", font=("Arial", 18), bg=self.colors["bg"]).pack(pady=20)
        
        # Listagem rápida de professores
        prof_model = Professor(self.db)
        professores = prof_model.listar()
        
        cols = ("ID", "Nome", "CPF", "Especialidade")
        tree = ttk.Treeview(self.content_frame, columns=cols, show="headings")
        for col in cols:
            tree.heading(col, text=col)
            tree.column(col, width=150)
        tree.pack(padx=20, pady=10, fill="both", expand=True)
        
        for p in professores:
            tree.insert("", "end", values=p)

    def show_relatorios(self):
        self.clear_content()
        tk.Label(self.content_frame, text="Emissão de Relatórios", font=("Arial", 18), bg=self.colors["bg"]).pack(pady=20)
        
        rel_frame = tk.Frame(self.content_frame, bg=self.colors["bg"])
        rel_frame.pack(pady=20)
        
        tk.Button(rel_frame, text="Gerar Diário de Aula (PDF)", 
                  command=lambda: self.gerar_relatorio("diario")).pack(pady=10)
        tk.Button(rel_frame, text="Gerar Notas por Semestre (PDF)", 
                  command=lambda: self.gerar_relatorio("notas")).pack(pady=10)

    def gerar_relatorio(self, tipo):
        try:
            # Para o exemplo, usaremos ID 1 (ajustar conforme necessário no sistema real)
            if tipo == "diario":
                path = self.report_gen.gerar_diario_aula(1, "2024-01-01", "2024-12-31")
            else:
                path = self.report_gen.gerar_notas_estudantes(1)
            messagebox.showinfo("Sucesso", f"Relatório gerado em: {path}")
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao gerar relatório: {str(e)}")

if __name__ == "__main__":
    app = FaculdadeApp()
    app.mainloop()
