let aantalSterren = parseInt(prompt("Geef aantal sterren in: "));
let rij = '';
let secondRij = '';

for (let i = 0; i < aantalSterren; i++) {
    rij += '*';
    console.log(rij);
}

for (let i = 0; i < aantalSterren; i++) {
    console.log(rij);
    rij = rij.slice(0, -1);
}