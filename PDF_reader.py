from PyPDF2 import PdfFileReader

from pathlib import Path
pdf_path = ('C:\\Users\\18411029\\Documents\\PythonCourses\\Parser\\export.pdf')

pdf = PdfFileReader(str(pdf_path))
# Вывод количества страниц
# print(pdf.getNumPages())

text = pdf.getPage(1)
print(text.extractText())
