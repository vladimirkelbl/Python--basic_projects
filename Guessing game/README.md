# Hádání čísla
Vytvořil jsem konzolovou hru, kde uživatel zadá interval čísel (lze jít i do záporných čísel),
ze kterého poté hádá číslo, které systém náhodně vygeneroval. Pokud je interval menší nebo roven jak 20,
číslo je hádáno po jednom a systém vypisuje, která čísla z intervalu zbývají. Pokud je interval delší,
po zadání čísla systém nejen řekne, jestli je číslo správné, ale i jestli je větší nebo menší než číslo hledané.
Vypíše se interval, který je zmenšený o čísla, která jsou větší (resp. menší) než číslo zadané v předchozím kole.
Ke správnému číslu se dá tedy nejrychleji dojít metodou půlení intervalu.

Hlavní přínos tohoto projektu pro mě bylo používání knihovny numpy a práce s řetězci.

Myšlenku této aplikace jsem převzal z https://www.geeksforgeeks.org/number-guessing-game-in-python/.
