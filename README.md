### Konzolová aplikace pro evidenci pojištěných osob.

Aplikace obsahuje správu pojištěných (pojištěné osoby, např. "Jan Novák").
Každou osobu jednoznačně identifikuje jméno, příjmení a věk
(dvě osoby, které mají shodné jméno, příjmení i věk nemohou být zaevidovány).

Evidence nabízí:
1. Zobrazení seznamu všech pojištěných
2. Vyhledání pojištěného - podle jména a příjmení, v případě shody podle věku
3. Přidání pojištěného - eviduje se jméno, příjmení, věk a telefonní číslo
4. Odstranění pojištěného - podle jména a příjmení, v případě shody podle věku
5. Ukončení evidence

Podle volby uživatele jsou dané entity uloženy buď v databázi anebo v paměti v kolekci.
Aplikace uživateli nabízí vložení testovacích dat do evidence.
Defaultní nastavení je ukládání kolekce do paměti bez použití testovacích osob.

V případě použití databáze jsou data po skončení aplikace uložena v souboru "registry.db".
V případě ukládání entit do paměti aplikace uložení dat po skončení aplikace neřeší.

Aplikace se spustí shell skriptem run_app.sh.
