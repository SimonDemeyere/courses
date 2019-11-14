let naam = "Simon";
let familieNaam = "Demeyere";
let geboorteJaar = 1997;
let functie = "Leerling";

let dag = "'s avonds";
let gehuwd = false;
let niets;
console.log(naam);
console.log(familieNaam);
console.log(geboorteJaar);
console.log(functie);
console.log(dag);
console.log(gehuwd);
console.log(niets);

niets = "niets is niet langer niets";
console.log(niets);

console.log(naam + ' ' + familieNaam);

console.log(naam.concat(' ', familieNaam));

document.write(naam.concat(' ', familieNaam));
document.write("<br>" + "Voornaam: " + naam + ' ' + "Familienaam: " + familieNaam);

//ES6
document.write(`<br>Voornaam: ${naam} Familienaam: ${familieNaam}`);

let ingave = prompt("Geef uw voornaam in:");
document.write(`<br>Uw voornaam: ${ingave} `);
document.write(typeof(ingave));

if (window.confirm("Ben je zeker dat je dit wilt verwijderen?")) {
    deleteIets(id);
}

let getal1 = parseInt(prompt("Geef getal 1 in:"));
let getal2 = parseInt(prompt("Geef getal 2 in:"));
let resultaat = getal1 + getal2;
document.write(resultaat + "<br>");
document.write(typeof(getal1) + "<br>");
document.write(typeof(getal2) + "<br>");
document.write(typeof(resultaat));

let naam = prompt("Geef uw naam in:");
let beroep = prompt("Geef een keuze: bediende, arbeider, werkloos");

if (beroep == "bediende") {
    document.write(`<h2 class="mijnclass">Het beroep van ${naam} is ${beroep}</h2>`);
} else if (beroep == "arbeider") {
    document.write(`Het beroep van ${naam} is ${beroep}`);
} else {
    document.write(`Het beroep van ${naam} is ${beroep}`);
}

let getal1 = 5;
let getal2 = 6;

if (getal1 < getal2) {
    document.write("getal1 is groter");
} else {
    document.write("getal2 is groter");
}

getal1 < getal2 ?
    document.write("getal1 is groter"):
    document.write("getal2 is groter");

let onderwijs = "vdab";
switch(onderwijs) {
    case "vdab":
        document.write("Curcus door de vdab");
        break;
    case "syntra":
        document.write("Curcus door de syntra");
        break;
    case "cvo":
        document.write("Curcus door de cvo");

let cursisten = ['Simon', 'Peter', 'Pan', 'Kletse'];

cursisten.forEach(function(arr) {
    console.log(arr);
})
        break;
    case "vives":
        document.write("Curcus door de vives");
        break;
    default:
        document.write("Gegeven door een andere instelling");
}

function berekenLeeftijd(huidigJaar, geboorteJaar) {
    return huidigJaar - geboorteJaar;
}

let today = new Date();
let hj = today.getFullYear()
let gj = parseInt(prompt("Geef geboorte jaar"));
let resultaat = berekenLeeftijd(hj, gj);

resultaat >= 0 ?
    document.write(`Het aantal jaren tussen ${hj} en ${gj} is: ${resultaat}`):
    document.write(`Uw geboortejaar kan niet groter zin dan het huidige jaar.`);

let cursisten = ['Simon', 'Peter', 'Pan', 'Kletse'];
let curcusJaar = new Array(2017,2018,2019,2020);

console.log(cursisten);
console.log(curcusJaar);

for(let i = 0; i <= 10; i++) {
    console.log(i);
}

let cursisten = ['Simon', 'Peter', 'Pan', 'Kletse'];

cursisten.forEach(function(arr) {
    console.log(arr);
})
