## Descriere

Acest script Python utilizează Flask pentru a crea un backend care procesează fișiere CSV conținând date de preț pentru acțiuni. 
Scopul principal este de a identifica valorile aberante (outliers) din seturile de date. Scriptul oferă două funcționalități principale:

1. Selectarea aleatorie a 30 de puncte de date consecutive dintr-un fișier CSV.
2. Identificarea valorilor aberante din aceste 30 de puncte, definite ca fiind valorile care depășesc 2 deviații standard față de medie.

## Instalare

1. Asigurați-vă că aveți Python 3.6+ instalat pe sistemul dumneavoastră.

2. Instalați dependențele necesare folosind pip:

   ```
   pip install flask pandas numpy
   ```

3. Descărcați scriptul și salvați-l cu un nume relevant (de exemplu, `stock_outliers.py`).

## Utilizare

1. Plasați fișierele CSV cu datele acțiunilor în directorul `/mnt/data/` sau modificați variabila `input_directory` din script pentru a indica locația corectă.

2. Rulați scriptul folosind comanda:

   ```
   python stock_outliers.py
   ```

3. Scriptul va procesa fișierele CSV, va identifica valorile aberante și va salva rezultatele în directorul `./output/` (sau în directorul specificat în variabila `output_directory`).

4. Rezultatele vor fi salvate în fișiere CSV separate pentru fiecare fișier de intrare procesat, cu prefixul "outliers_".

## Buguri și Vulnerabilități

1. Scriptul nu verifică validitatea datelor din fișierele CSV. Fișierele cu formate neașteptate pot cauza erori.
2. Nu există o gestionare robustă a erorilor pentru situații precum lipsa permisiunilor de scriere în directorul de ieșire.
3. Scriptul nu gestionează eficient fișierele foarte mari, care ar putea depăși memoria disponibilă.
4. Nu există o verificare pentru a preveni suprascrierea fișierelor de ieșire existente.

## Îmbunătățiri viitoare

1. Implementarea unei validări mai robuste a datelor de intrare.
2. Adăugarea de opțiuni de linie de comandă pentru o mai mare flexibilitate (de exemplu, specificarea directorului de intrare/ieșire, numărul de fișiere de procesat).
3. Implementarea procesării în loturi pentru fișiere mari.
4. Adăugarea de logging pentru o mai bună urmărire a execuției și gestionare a erorilor.
5. Implementarea de teste unitare pentru a asigura fiabilitatea funcțiilor.
6. Adăugarea unei interfețe utilizator simple pentru o utilizare mai ușoară.
7. Implementarea unei funcționalități de raportare care să ofere statistici sumare despre valorile aberante identificate.
8. Optimizarea performanței pentru procesarea mai rapidă a seturilor mari de date.
9. Adăugarea suportului pentru formate de fișiere multiple (nu doar CSV).
10. Implementarea de măsuri de securitate suplimentare pentru utilizarea în medii de producție.
