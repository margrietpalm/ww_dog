Met deze tool kun je berekenen wat de kans is op een bepaalde uitkomst van de dorpsgek.


#### Definitie en aannames

> De dorpsgek mag elke nacht 3 namen doorgeven, van die 3 worden door de vertellers 2 willekeurig geselecteerd en daarvan krijgt de dorpsgek de alliantie te horen, hij krijgt echter alleen de alliantie terug, niet de rol. Bijvoorbeeld: dorpsgek geeft door A, B en C, krijgt terug: burgerkamp, wolvenkamp. De dorpsgek mag niet zichzelf of dode spelers doorgeven.

Deze 3 namen noemen we de *check*. 

Hieruit volgen een aantal aannames:

* Het aantal spelers is het totale aantal spelers inclusief de dorpsget.
* Het aantal wolven is het aantal wolven dat door zienende rollen gezien wordt.
* De dorpsgek kiest 3 willekeurige spelers maar neemt *nooit* zichzelf mee.


#### Methode

Het berekenen van de kans is een 2 staps proces:

1. Bereken de kans voor 0, 1, 2, of 3 wolven in de check.
2. Vermenigvuldig de kans voor elke mogelijke uitslag van de check bij dat aantal wolven met de kans berekend in stap 1.


##### Kans op $w$ aantal wolven in de check

We gaan uit van een populatie van $N$ spelers, exclusief de dorpsgek, met daarin $W$ wolven en $B$ burgers. 
Om de kans op $w$ wolven in de check te bepalden moeten we 3 dingen berekenen:

1. $N_w$: het aantal manieren om $w$ wolven uit $W$ wolven te trekken;
2. $N_b$: het aantal manieren om $b=3-w$ burgers uit $B$ wolven te trekken;
3. $N_\\text{total}$: het aantal manieren om 3 spelers uit $N$ spelers te trekken.

Het aantal sets van $k$ uit een verzameling van $n$ items wordt berekend: $\\frac{n!}{k! \cdot (n - k)!}$; 
dit staat bekend als de binomial coefficient.

Dus, we kunnen de bovengenoemde waardes berekenen met:

1. $N_w = \\frac{W!}{w! \cdot (W-w)!}$
2. $N_b = \\frac{B!}{b! \cdot (B-b)!}$
3. $N_\\text{total} = \\frac{N!}{3! \cdot (N-3)!}$


##### Kans op bepaalde uitslag gegeven samenstelling van de check

De kans op iedere uitslag, gegeven de verdeling in de check is als volgt:
* Check met 3 burgers: de enige mogelijke uitslag is burger-burger (met een kans van 1).
* Check met 0 burgers: de enige mogelijke uitslag is wolf-wolf (met een kans van 1).
* Check met 2 bugers en 1 wolf: 
    * kans 2/3 voor burger-wolf
    * kans 1/3 voor burger-burger
* Check met 1 burger en 2 wolven:
    * kans 1/3 voor burger-wolf
    * kans 2/3 voor wolf-wolf