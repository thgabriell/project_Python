from fpdf import FPDF
from src.models.database_manager import DatabaseManager

class ReportGenerator:
    def __init__(self, db_manager):
        self.db = db_manager

    def gerar_diario_aula(self, turma_id, data_inicio, data_fim):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)
        pdf.cell(200, 10, "Faculdade Vicente de Sousa", ln=True, align="C")
        pdf.set_font("Arial", "B", 14)
        pdf.cell(200, 10, f"Diário de Aula - Turma ID: {turma_id}", ln=True, align="C")
        pdf.ln(10)
        
        pdf.set_font("Arial", "B", 12)
        pdf.cell(40, 10, "Data", border=1)
        pdf.cell(150, 10, "Conteúdo Ministrado", border=1)
        pdf.ln()
        
        query = "SELECT data_aula, conteudo FROM diario_aula WHERE id_turma = ? AND data_aula BETWEEN ? AND ?"
        aulas = self.db.fetch_all(query, (turma_id, data_inicio, data_fim))
        
        pdf.set_font("Arial", "", 12)
        for data, conteudo in aulas:
            pdf.cell(40, 10, str(data), border=1)
            pdf.cell(150, 10, str(conteudo), border=1)
            pdf.ln()
            
        output_path = f"/home/ubuntu/faculdade_vicente_sousa/relatorio_diario_{turma_id}.pdf"
        pdf.output(output_path)
        return output_path

    def gerar_notas_estudantes(self, turma_id):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)
        pdf.cell(200, 10, "Faculdade Vicente de Sousa", ln=True, align="C")
        pdf.set_font("Arial", "B", 14)
        pdf.cell(200, 10, "Relatório de Notas por Semestre", ln=True, align="C")
        pdf.ln(10)
        
        query = """
        SELECT e.nome, mt.nota_1, mt.nota_2, mt.media, mt.frequencia 
        FROM estudantes e 
        JOIN matriculas_turmas mt ON e.id = mt.id_estudante 
        WHERE mt.id_turma = ?
        """
        notas = self.db.fetch_all(query, (turma_id,))
        
        pdf.set_font("Arial", "B", 10)
        pdf.cell(80, 10, "Estudante", border=1)
        pdf.cell(25, 10, "Nota 1", border=1)
        pdf.cell(25, 10, "Nota 2", border=1)
        pdf.cell(25, 10, "Média", border=1)
        pdf.cell(25, 10, "Freq. (%)", border=1)
        pdf.ln()
        
        pdf.set_font("Arial", "", 10)
        for nome, n1, n2, media, freq in notas:
            pdf.cell(80, 10, str(nome), border=1)
            pdf.cell(25, 10, str(n1), border=1)
            pdf.cell(25, 10, str(n2), border=1)
            pdf.cell(25, 10, str(media), border=1)
            pdf.cell(25, 10, str(freq), border=1)
            pdf.ln()
            
        output_path = f"/home/ubuntu/faculdade_vicente_sousa/relatorio_notas_{turma_id}.pdf"
        pdf.output(output_path)
        return output_path
