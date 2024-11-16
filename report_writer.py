from fpdf import FPDF
import pandas as pd
from tabulate import tabulate
import sys
from io import StringIO
import contextlib

class ReportWriter:
    def __init__(self, filename='report.pdf'):
        self.pdf = FPDF()
        self.pdf.add_page()
        self.pdf.set_auto_page_break(auto=True, margin=15)
        self.pdf.set_font("Arial", size=11)
        self.filename = filename
        self.line_height = 5
        
    def add_title(self, text):
        """Add a title to both console and PDF"""
        print(text)
        self.pdf.set_font("Arial", 'B', 14)
        self.pdf.cell(0, 10, txt=text, ln=True)
        self.pdf.set_font("Arial", size=11)
        
    def add_text(self, text):
        """Add text to both console and PDF"""
        print(text)
        # Split text into lines that fit the page width
        lines = self.pdf.multi_cell(0, self.line_height, txt=text, split_only=True)
        for line in lines:
            self.pdf.cell(0, self.line_height, txt=line, ln=True)
            
    def add_space(self):
        """Add spacing to both console and PDF"""
        print('\n')
        self.pdf.ln(self.line_height)
        
    def add_break(self):
        """Add break line to both console and PDF"""
        print('\n' + '---' * 40 + '\n')
        self.pdf.ln(self.line_height)
        self.pdf.cell(0, self.line_height, txt='─' * 90, ln=True)
        self.pdf.ln(self.line_height)
        
    def add_part_break(self):
        """Add part break to both console and PDF"""
        print('\n' + '===' * 40)
        print('===' * 40 + '\n')
        self.pdf.ln(self.line_height)
        self.pdf.cell(0, self.line_height, txt='═' * 90, ln=True)
        self.pdf.cell(0, self.line_height, txt='═' * 90, ln=True)
        self.pdf.ln(self.line_height)
        
    def add_dataframe(self, df, max_rows=None):
        """Add dataframe to both console and PDF"""
        # Print to console
        print(df)
        
        # Convert to string table for PDF
        if max_rows:
            df_display = df.head(max_rows)
        else:
            df_display = df
            
        table_string = tabulate(
            df_display, 
            headers='keys', 
            tablefmt='grid', 
            showindex=True,
            floatfmt='.3f'
        )
        
        # Add to PDF with smaller font
        self.pdf.set_font("Courier", size=8)
        for line in table_string.split('\n'):
            self.pdf.cell(0, 4, txt=line, ln=True)
        self.pdf.set_font("Arial", size=11)
        
    def add_info(self, df):
        """Capture and add DataFrame info to both console and PDF"""
        # Capture the info output
        buffer = StringIO()
        df.info(buf=buffer)
        info_text = buffer.getvalue()
        
        # Print to console
        print(info_text)
        
        # Add to PDF
        self.pdf.set_font("Courier", size=8)
        for line in info_text.split('\n'):
            self.pdf.cell(0, 4, txt=line, ln=True)
        self.pdf.set_font("Arial", size=11)
        
    def save(self):
        """Save the PDF file"""
        self.pdf.output(self.filename)

@contextlib.contextmanager
def report_section():
    """Context manager to capture printed output and add it to PDF"""
    old_stdout = sys.stdout
    string_io = StringIO()
    sys.stdout = string_io
    try:
        yield string_io
    finally:
        sys.stdout = old_stdout