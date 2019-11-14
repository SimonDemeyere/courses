let getal = parseInt(prompt("Geet een getal in:"));
let optelling = 1;

for (let i = 1; i < getal + 1; i++) {
    optelling *= 2;
    if (optelling <= getal) {
        console.log(optelling);
    }
}