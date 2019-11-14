let aantalGetallen = parseInt(prompt("Geef aantal getallen in:"));
let som = 0;

for (let i = 1; i < aantalGetallen + 1; i++) {
    let getal = parseInt(prompt(`Geef getal${i} in:`));
    som += getal;
}

console.log(`De totale som van ${aantalGetallen} getallen is ${som}.`);