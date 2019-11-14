let tafel = parseInt(prompt("Geef tafel in:"));
let eindGetal = parseInt(prompt("Geef eindgetal in:"));

let str = '';

for (let i = 1; i < eindGetal + 1; i++) {
    if (i % 3 == 0) {
        str += `${tafel} x ${i} = ${tafel * i} \n`;
    } else {
        str += `${tafel} x ${i} = ${tafel * i}, `;
    }
}

console.log(str);