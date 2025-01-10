function syncDataBetweenSheets() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  
  // Podarkusz "z_pythona"
  const zPythonSheet = ss.getSheetByName("z_pythona");
  const zPythonData = zPythonSheet.getRange(2, 4, zPythonSheet.getLastRow() - 1, 3).getValues(); // Kolumny D (nazwa pliku) i F (tytuł)
  
  // Podarkusz "all"
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

  // Synchronizacja danych
  zPythonData.forEach((row, index) => {
    const fileName = row[0]; // Nazwa pliku (kolumna D)
    const title = row[2];    // Tytuł produktu (kolumna F)
    const rowIndex = index + 2; // Numer wiersza w "z_pythona"

    if (allFileMap[fileName]) {
      // Podświetlenie w "z_pythona" (kolumna D)
      zPythonSheet.getRange(rowIndex, 4).setBackground("lightgreen");

      // Przypisanie tytułu do odpowiedniego wiersza w "all" (kolumna E)
      const targetRow = allFileMap[fileName];
      allSheet.getRange(targetRow, 5).setValue(title);
    }
  });
}
