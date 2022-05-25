#SonarLint Statikus analízis

A kód statikus elemzéséhez a SonarLint eszközt használtuk melyet a fejelsztő környezetbe 
telepítettünk.
A teljes projekten való futtatás után a teljes projekten több mint 200 hibát talált a SonarLint

A SonarLint által felismert hibák többnyire code smellek, a talált több száz hibából javítottunk.
Ilyen módosítás például a kikommentezett kódrészletek törlése vagy nem használt változók megszüntetése.
Ezen kívül javítottunk hibákat ahol az osztályok lokális változója az osztály nevével van ellátva,
beépített függvény nevét használja vagy az operátor használat nem megfelelő volt.

A hibákat a bfs, graph linkedlist, maths, matrix, string, sort valamint a stack packagekben lévő osztályokban javítottuk.