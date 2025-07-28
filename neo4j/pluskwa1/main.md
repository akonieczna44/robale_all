
1. wygenerowanie przykładowego grafu wiedzy z wpisu o pluskwach (https://www.odstraszanie.pl/a1,zwalczanie-pluskiew-jak-sie-pozbyc-pluskwy.html) do zaimportowania go do neo4j
  - plik główny zawiera podstawowe kategorie
  - plik drugi zawiera relacje (typu: pluskwa --> występuje --> materace)


2. stworzenie zgodnie z tutorialem przykładowego grafu, stworzenie grafu dla pluskiew

<img width="613" height="454" alt="image" src="https://github.com/user-attachments/assets/24925f40-7b8c-445a-aa71-ab8dcce42e5f" />
   
3. pomysł rozszerzenia gałęzi o kategorie produktów i produkty w konwencji...

Pluskwa domowa
 ├─ POWODUJE → Ugryzienia
 ├─ WYSTĘPUJE_W → Materace, meble
 ├─ ZWALCZANA_PRZEZ → Spraye, fumigatory
 │      ├─ ZAWIERA → Spray A
 │      ├─ ZAWIERA → Spray B
 │      └─ ZAWIERA → Spray C
 ├─ ZWALCZANA_PRZEZ → Pułapki
 │      └─ ZAWIERA → Pułapka Lepowa
 └─ ZWALCZANA_PRZEZ → Myjka parowa



  - wyexportowanie do csv listy 42 produktów na pluskwy (tytuł, cena, kategoria, producent, link)
  - dwa rozszerzone csv stworzone we współpracy z chatem
  - ponowne łączenia, filtrowania grafów
  - analiza problemów z etykietami i wizualizacją, czyszczenie starych labeli (Order, Product), wstępna optymalizacja filtrów i eksploracji grafu
<img width="787" height="482" alt="image" src="https://github.com/user-attachments/assets/37c20d85-b4ce-4b5c-97b7-32768eb3b905" />




wynik: prototyp grafu do dalszej pracy (lepsza kategoryzacja, czystsze CSV, układ wizualny) i podstawa do topical map

to do: uzupełnienie csv głównego o produkty (nie tylko 3, ale 42)
