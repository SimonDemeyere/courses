let age = prompt("Geef leeftijd in:");

function checkLeeftijd(leeftijd) {
    if(leeftijd < 18) {
        return "Om deel te nemen aan de spelen van de Nationale Loterij moet je minimum 18 jaar oud zijn.";
    } else {
        return `Je bent ${leeftijd} jaar oud. Je mag deelnemen aan de spelen van de Nationale Loterij.`;
    }
}

function askBulletin() {
    let aantalVakjes = parseInt(prompt("Geef aantal bulletin vakjes: 2, 4, 6, 8, 10, 12"));
    switch(aantalVakjes) {
        case 2:
            return `Kostprijs van ${aantalVakjes} bedraagt 4euro.`;
        case 4:
            return `Kostprijs van ${aantalVakjes} bedraagt 8euro.`;
        case 6:
            return `Kostprijs van ${aantalVakjes} bedraagt 12euro.`;
        case 8:
            return `Kostprijs van ${aantalVakjes} bedraagt 16euro.`;
        case 10:
            return `Kostprijs van ${aantalVakjes} bedraagt 18euro.`;
        case 12:
            return `Kostprijs van ${aantalVakjes} bedraagt 20euro.`;
        default:
            return `Geen optie.`;
    }
}

console.log(checkLeeftijd(age));
if (age >= 18) {
    console.log(askBulletin());
}
