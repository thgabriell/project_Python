import tkinter as tk
from tkinter import ttk, messagebox

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Gestão - Faculdade Vicente de Sousa")
        self.geometry("1024x768")
        
        # Configuração de cores
        self.colors = {
            "primary": "#2c3e50",
            "secondary": "#34495e",
            "accent": "#3498db",
            "text": "#ecf0f1",
            "bg": "#f5f6fa"
        }
        
        self.configure(bg=self.colors["bg"])
        self.setup_ui()

    def setup_ui(self):
        # Frame do Menu Lateral
        self.side_menu = tk.Frame(self, bg=self.colors["primary"], width=200)
        self.side_menu.pack(side="left", fill="y")
        self.side_menu.pack_propagate(False)
        
        # Título no Menu
        lbl_titulo = tk.Label(self.side_menu, text="FVS", font=("Arial", 24, "bold"), 
                              bg=self.colors["primary"], fg=self.colors["text"], pady=20)
        lbl_titulo.pack()
        
        lbl_subtitulo = tk.Label(self.side_menu, text="Faculdade Vicente de Sousa", font=("Arial", 8), 
                                 bg=self.colors["primary"], fg=self.colors["text"], pady=5)
        lbl_subtitulo.pack()

        # Botões do Menu
        menus = [
            ("Início", self.show_home),
            ("Cursos", self.show_cursos),
            ("Professores", self.show_professores),
            ("Estudantes", self.show_estudantes),
            ("Turmas", self.show_turmas),
            ("Notas e Frequência", self.show_pedagogico),
            ("Relatórios", self.show_relatorios),
            ("Sair", self.quit)
        ]
        
        for text, command in menus:
            btn = tk.Button(self.side_menu, text=text, command=command, 
                            bg=self.colors["secondary"], fg=self.colors["text"], 
                            relief="flat", pady=10, font=("Arial", 10))
            btn.pack(fill="x", padx=5, pady=2)
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg=self.colors["accent"]))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg=self.colors["secondary"]))

        # Área de Conteúdo Principal
        self.content_frame = tk.Frame(self, bg=self.colors["bg"])
        self.content_frame.pack(side="right", fill="both", expand=True)
        
        self.show_home()

    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def show_home(self):
        self.clear_content()
        lbl = tk.Label(self.content_frame, text="Bem-vindo à Faculdade Vicente de Sousa", 
                       font=("Arial", 20, "bold"), bg=self.colors["bg"], pady=50)
        lbl.pack()
        
        info = tk.Label(self.content_frame, text="Selecione uma opção no menu à esquerda para começar.", 
                        font=("Arial", 12), bg=self.colors["bg"])
        info.pack()

    def show_cursos(self):
        self.clear_content()
        tk.Label(self.content_frame, text="Gestão de Cursos", font=("Arial", 18), bg=self.colors["bg"]).pack(pady=20)
        # Aqui viria a implementação da tabela e formulário de cursos

    def show_professores(self):
        self.clear_content()
        tk.Label(self.content_frame, text="Gestão de Professores", font=("Arial", 18), bg=self.colors["bg"]).pack(pady=20)

    def show_estudantes(self):
        self.clear_content()
        tk.Label(self.content_frame, text="Gestão de Estudantes", font=("Arial", 18), bg=self.colors["bg"]).pack(pady=20)

    def show_turmas(self):
        self.clear_content()
        tk.Label(self.content_frame, text="Gestão de Turmas", font=("Arial", 18), bg=self.colors["bg"]).pack(pady=20)

    def show_pedagogico(self):
        self.clear_content()
        tk.Label(self.content_frame, text="Gestão Pedagógica (Notas e Frequência)", font=("Arial", 18), bg=self.colors["bg"]).pack(pady=20)

    def show_relatorios(self):
        self.clear_content()
        tk.Label(self.content_frame, text="Emissão de Relatórios", font=("Arial", 18), bg=self.colors["bg"]).pack(pady=20)

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
