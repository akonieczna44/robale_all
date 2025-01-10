import os
import csv
from PyPDF2 import PdfReader

# Funkcja do odczytu zawartości PDF
def extract_relevant_text(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        first_page = reader.pages[0]
        text = first_page.extract_text()
        lines = text.splitlines()

        # Znalezienie linijek z odpowiednim tekstem
        start_index = next((i for i, line in enumerate(lines) if "karta bezpieczeństwa produktu:" in line.lower()), None)
        end_index = next((i for i, line in enumerate(lines) if "1. podmiot odpowiedzialny" in line.lower()), None)

        if start_index is not None and end_index is not None and start_index < end_index:
            relevant_lines = lines[start_index:end_index]
            return " ".join(relevant_lines).strip()  # Połącz linie w jeden ciąg tekstowy
        return "Nie znaleziono odpowiedniego tekstu"
    except Exception as e:
        return f"Błąd: {e}"

# Ścieżka lokalna do folderu z plikami PDF
LOCAL_FOLDER = r"D:\ROBALE i NO PEST\2025_gprs\dokumenty_instrukcje"

# Lista wyników
results = []

# Przechodzenie po wszystkich plikach w folderze
for root, dirs, files in os.walk(LOCAL_FOLDER):
    for file in files:
        if file.endswith('.pdf'):  # Tylko pliki PDF
            full_path = os.path.join(root, file)
            relevant_text = extract_relevant_text(full_path)
            # Dodaj nazwę pliku i znaleziony tekst do wyników
            results.append([file, relevant_text])

# Zapis wyników do pliku CSV
output_csv = "debug_output.csv"
with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Nazwa Pliku PDF", "Znaleziony Tekst"])
    writer.writerows(results)

print(f"Wyniki zapisano do pliku: {output_csv}")
