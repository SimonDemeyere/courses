let aantalSterren = parseInt(prompt("Geef aantal sterren in: "));
let rij = '';

for (let i = 0; i < aantalSterren; i++) {
    rij += '*';
    console.log(rij);
}