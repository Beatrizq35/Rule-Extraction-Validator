"""Converte um PDF para Markdown usando Docling."""

from docling.document_converter import DocumentConverter

class PdfExtractor:
    def __init__(self):
        
        self.converter = DocumentConverter()

    def to_markdown(self, pdf_path):
        
        result = self.converter.convert(pdf_path)
        return result.document.export_to_markdown()