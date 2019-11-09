# Den komplette regnemaskine
I har nu alle dele til at lave jeres egen regnemaskine der kan:

- +
- -
- /
- *

I skal bruge variabler, funktioner, `if` sætninger og `try/except`

Den skal selvfølgelig også kontrollere at brugeren ikke taster noget forkert inden den forsøger at regne :)

## Opgaven
Her er et eksempel på, hvordan min regnemaskine virker:

```
vælg regnemetode (muligheder: +, -, * og /) eller skriv stop for at stoppe: +
skriv det første tal: 4
skriv det andet tal: 5
4 + 5 = 9
```

Det lyder måske som en kæmpestor opgave, men som altid når man skal lave et program er det en god ide at dele opgaven op i mindre opgaver.

Sæt jer ned, I må gerne arbejde sammen to og to, og prøv at tænk over, hvilke dele I skal have lavet.

Her er et foreslag til, hvordan I kunne dele opgaven op:

### 1. Vælg regnemetode
Skriv en besked til brugeren om at de skal starte med at vælge regnemetode.
Når brugeren har skrevet en regnemetode skal I kontrollere (det kalder vi som regel validere), at brugeren har tastet noget I kan bruge til noget.

Altså, har de tastet `+`, `-`, `*` eller `/` så er alt godt, og ellers skal I vise dem en fejlbesked.

### 2. Indtast tal
Nu skal I så have brugeren til at taste to tal, det har I tidligere gjort mange gange, så kig på hvad I gjorde dengang.

### 3. Udregn
Nu skal I så have kombineret den regnemetode brugeren tastede, og de to tal de tastede.

I skal huske at kigge på hvilken regnemetode brugerne har valgt. Tænk over hvordan I kan gøre det.

### Bonus
Hvis det bare går derudaf og I er færdige efter 1 time kan I udvide jeres program så det bliver ved med at regne stykker ud, indtil I skriver "stop"
