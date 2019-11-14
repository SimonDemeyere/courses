let geboorteJaar = prompt("Geef geboorte jaar in:");
let huidigDatum = new Date();
let huidigJaar = huidigDatum.getFullYear();

let verschilJaren = huidigJaar - geboorteJaar;

if (verschilJaren >= 18) {
    console.log(`Vanaf nu mag, kan en beslis ik alles binnen de wettelijke grenzen.`);
} else {
    console.log(`Gelukkig heb ik mijn ouders die alles voor me regelen.`);
}