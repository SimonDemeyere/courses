let getal = parseInt(prompt("Geef een getal:"));
let faculteit = 1;

for (let i = 1; i < getal + 1; i++) {
    faculteit *= i;
    console.log(faculteit);
}