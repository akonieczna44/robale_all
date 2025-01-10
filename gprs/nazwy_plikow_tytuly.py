import os
import pandas as pd
from PyPDF2 import PdfReader


# Funkcja do odczytu zawartości PDF
def extract_relevant_text(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        first_page = reader.pages[0]
        text = first_page.extract_text()
        lines = text.splitlines()

        # Znalezienie linijek z odpowiednim tekstem,
        # bo potrzebuję nazw między "Karta Bezpieczeństwa.. ", a "1. podmiot odpowiedzialny"
        start_index = next((i for i, line in enumerate(lines) if line.startswith("Karta Bezpieczeństwa Produktu:")),
                           None)
        end_index = next((i for i, line in enumerate(lines) if "1. Podmiot odpowiedzialny" in line), None)

        if start_index is not None and end_index is not None and start_index < end_index:
            relevant_lines = lines[start_index:end_index]
            return " ".join(relevant_lines).strip()  # Połącz linie w jeden ciąg tekstowy
        return "Nie znaleziono odpowiedniego tekstu"
    except Exception as e:
        return f"Błąd: {e}"


# Funkcja do odczytu struktury folderów i filtrowania plików
# bo potrzebuję tych pdf'ów zaczynających się od "Karta Bezpieczeństwa.. "
def get_filtered_pdfs_with_text(base_path, relative_base, search_text):
    data = []
    relative_base_fixed = relative_base.replace("\\", "/")

    for root, dirs, files in os.walk(base_path):
        relative_root = os.path.relpath(root, base_path)
        relative_root_fixed = relative_root.replace("\\", "/")

        for file in files:
            if file.endswith('.pdf'):  # Tylko pliki PDF
                full_path = f"{root}/{file}".replace("\\", "/")  # Pełna ścieżka
                # Wyciąganie tekstu przed "1. Podmiot odpowiedzialny"
                relevant_text = extract_relevant_text(full_path)
                if relevant_text.startswith(search_text):  # Sprawdzenie warunku
                    main_folder = relative_base_fixed.split("/")[-1]
                    sub_folder = relative_root_fixed if relative_root_fixed != "." else ""
                    relative_path = f"/{relative_base_fixed}/{relative_root_fixed}/{file}".replace("//", "/")

                    # Wyciąganie tytułu produktu
                    product_title = relevant_text.replace(search_text, "").strip()

                    data.append([main_folder, sub_folder, relative_path, file, relevant_text, product_title])
    return data


# Ścieżka lokalna do folderu z plikami PDF
LOCAL_FOLDER = r"D:\ROBALE i NO PEST\2025_gprs\dokumenty_instrukcje"
RELATIVE_BASE = "dokumenty_instrukcje"
SEARCH_TEXT = "Karta Bezpieczeństwa Produktu:"

# Pobranie danych o strukturze folderów i plików
filtered_data = get_filtered_pdfs_with_text(LOCAL_FOLDER, RELATIVE_BASE, SEARCH_TEXT)

# Tworzenie DataFrame (tabeli danych)
df = pd.DataFrame(filtered_data,
                  columns=["Folder Główny", "Podfolder", "Ścieżka", "Nazwa Pliku PDF", "Karta: TYTUŁ",
                           "Tytuł Produktu"])

# Zapis do pliku Excel
output_excel = "filtered_gprs_with_titles.xlsx"
df.to_excel(output_excel, index=False, engine='openpyxl')

print(f"Plik Excel został zapisany jako: {output_excel}")
