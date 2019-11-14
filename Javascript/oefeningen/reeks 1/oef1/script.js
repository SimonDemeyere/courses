let age = prompt("Geef leeftijd in:");

function checkLeeftijd(leeftijd) {
    if(leeftijd < 18) {
        return "Om deel te nemen aan de spelen van de Nationale Loterij moet je minimum 18 jaar oud zijn.";
    } else {
        return `Je bent ${leeftijd} jaar oud. Je mag deelnemen aan de spelen van de Nationale Loterij.`;
    }
}

console.log(checkLeeftijd(age));