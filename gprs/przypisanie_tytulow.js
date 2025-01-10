function syncDataBetweenSheets() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  
  // Podarkusz "z_pythona"
  const zPythonSheet = ss.getSheetByName("z_pythona");
  const zPythonData = zPythonSheet.getRange(2, 1, zPythonSheet.getLastRow() - 1, 3).getValues(); // Kolumny A (nazwa pliku), B (tekst), C (tytuł)
  
  // 1. Usuń wartości "Nie znaleziono odpowiedniego tekstu" i "Nie znaleziono tytułu"
  zPythonData.forEach((row, index) => {
    const rowIndex = index + 2; // Numer wiersza w arkuszu (zaczynając od 2)
    if (row[1] === "Nie znaleziono odpowiedniego tekstu") {
      zPythonSheet.getRange(rowIndex, 2).setValue(""); // Usuń z kolumny B
    }
    if (row[2] === "Nie znaleziono tytułu") {
      zPythonSheet.getRange(rowIndex, 3).setValue(""); // Usuń z kolumny C
    }
  });

  // Odśwież dane po usunięciu wartości
  const cleanedData = zPythonSheet.getRange(2, 1, zPythonSheet.getLastRow() - 1, 3).getValues();

  // 2. Podarkusz "all"
  const allSheet = ss.getSheetByName("all");
  const allData = allSheet.getRange(2, 3, allSheet.getLastRow() - 1, 2).getValues(); // Kolumny C (nazwa pliku) i E (tytuł)
  
  // Mapowanie nazw plików w podarkuszu "all" na ich indeksy
  const allFileMap = {};
  allData.forEach((row, index) => {
    const fileName = row[0]; // Kolumna C w "all"
    if (fileName) {
      allFileMap[fileName] = index + 2; // Zachowujemy numer wiersza (od 2)
    }
  });

  // 3. Synchronizacja danych (pierwsze przejście)
  cleanedData.forEach((row, index) => {
    const fileName = row[0]; // Nazwa pliku (kolumna A)
    const title = row[2];    // Tytuł produktu (kolumna C)
    const rowIndex = index + 2; // Numer wiersza w "z_pythona"

    if (allFileMap[fileName]) {
      // Podświetlenie w "z_pythona" (kolumna A)
      zPythonSheet.getRange(rowIndex, 1).setBackground("lightgreen");

      // Przypisanie tytułu do odpowiedniego wiersza w "all" (kolumna E)
      const targetRow = allFileMap[fileName];
      allSheet.getRange(targetRow, 5).setValue(title);
    }
  });

  // 4. Druga iteracja weryfikująca
  cleanedData.forEach((row) => {
    const fileName = row[0]; // Nazwa pliku (kolumna A)
    const title = row[2];    // Tytuł produktu (kolumna C)

    if (allFileMap[fileName]) {
      const targetRow = allFileMap[fileName];
      const existingTitle = allSheet.getRange(targetRow, 5).getValue(); // Sprawdź, czy tytuł jest już przypisany
      if (!existingTitle && title) {
        // Jeśli brak tytułu, przypisz ponownie
        allSheet.getRange(targetRow, 5).setValue(title);
      }
    }
  });
}
