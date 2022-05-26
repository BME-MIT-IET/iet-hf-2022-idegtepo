| Tesztelő      | Smuk András |
| ----------- | ----------- |
| Cél      | String package kiválasztott függvényeinek Manual and Exploratory tesztje |
| Teszt kezdete   | 2022.05.25. 23:30 |
| Időablak | |

# Tesztek

## Általános hibalehetőségek

1. Nem működik megfelelően a függvény
2. Nem tudja a függvény a különleges karaktereket kezelni
3. Nem tudja a függvény az ékezetes karaktereket kezelni

## reverse_string.py:

### Tesztelési szempontok:

Összehasonlítunk manuálisan egy mondatot a fordítottját és a fordított-fordítottját.
1. Általános teszt
   1. Egy angol mondattal teszteljük 
2. Különleges karakteres teszt
   1. Egy speciális karakterekből álló stringgel teszteljük
3. Ékezetes karakteres teszt
   1. Egy ékezetes magyar mondattal teszteljük

### Konklúzió:

1. recursive(s)
   1. Általános teszt: *Megfelelt*
   2. Különleges karakteres teszt: *Megfelelt*
   3. Ékezetes karakteres teszt: *Megfelelt*
2. iterative(s)
   1. Általános teszt: *Megfelelt*
   2. Különleges karakteres teszt: *Megfelelt*
   3. Ékezetes karakteres teszt: *Megfelelt*
3. pythonic(s)
   1. Általános teszt: *Megfelelt*
   2. Különleges karakteres teszt: *Megfelelt*
   3. Ékezetes karakteres teszt: *Megfelelt*
4. ultra_pythonic(s)
   1. Általános teszt: *Megfelelt*
   2. Különleges karakteres teszt: *Megfelelt*
   3. Ékezetes karakteres teszt: *Megfelelt*

A manuális tesztek alapján a függvények megfelelően működnek.

## make_sentence.py:

### Tesztelési szempontok:

Megnézzük, hogy egy szót, hány másik szóból tudunk összerakni.
1. Általános teszt
   1. Angol szóval tesztelünk
   2. Angol összetettebb szavakkal tesztelünk

### Konklúzió:

1. Általános teszt
   1. Angol szó teszt: *Nem felelt meg*
   2. Angol összetett szó teszt: *Nem felelt meg*

A manuális tesztek alapján a függvény nem működik megfelelően. Mivel whitebox tesztelést végeztem észleltem, hogy a függvény van hibásan implementálva.

## caesar_cipher_test.py:

### Tesztelési szempontok:

1. Általános teszt
   1. Egy angol szóval teszteljük. Pozitív rotationra.
   1. Egy angol szóval teszteljük. Nulla rotationra.
   2. Egy angol szóval teszteljük. Negatív rotationra.
2. Különleges karakteres teszt
   1. Egy különleges karakterekből, számokból és az angol abc betűiből álló szóra teszteljük.
3. Ékezetes karakteres teszt
   1. Egy magyar abc betűiből álló szóra teszteljük.
4. Nem szám rotation teszt
   1. A rotation értékének egy stringet adunk meg. Egy angol szóval teszteljük.

### Konklúzió:

1. Általános teszt
   1. Az általános teszt mindhárom paraméterezéssel lefutott, nagy számokkal is. *Megfelelt*
2. Különleges karakteres teszt
   1. Ehhez a teszthez a specifikációban nem szerepelt kiszámolási mód így nem volt várható érték. A számokat és a 
   különleges értékeket helyben hagyta, az angol abc betűit kódolta az algoritmus. 
   2. Az algoritmus célja a kódolás. Mivel az algoritmus nem tudja kódolni a különleges karaktereket és számokat, 
   ezért *Nem felelt meg*
3. Ékezetes karakteres teszt
   1. Ehhez a teszthez a specifikációban nem szerepelt kiszámolási mód így nem volt várható érték. Az ékezetes 
   karaktereket helyben hagyta, az angol abc betűit kódolta az algoritmus. 
   2. Az algoritmus célja a kódolás. Mivel az algoritmus nem tudja kódolni az ékezetes karaktereket, 
   ezért *Nem felelt meg*
4. Nem szám rotation teszt
   1. Ehhez a teszthez a specifikációban nem szerepelt kiszámolási mód így nem volt várható érték. A tesztet a kompliner 
   szintaxis ellenőrzője nem engedte lefutni. Amennyiben ezt a hibát kiküszöböltem, az algoritmus hibát dobott, 
   úgyhogy a bemenet nincsen ellenőrizve és nincsen exceptionkezelés. *Nem felelt meg*

Amennyiben az algoritmust az angol abc karaktereiből álló szövegen kívüli szöveggel is szeretnénk használni, ki kell 
bővíteni a benne lévő abc-t. A felhasználói hibák kiküszöbölése végett célszerű a bemeneteket ellenőrizni.