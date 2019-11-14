let naam = prompt('Geef uw naam in:');
let weergave = "De naam die u invoerde was: " + naam;
// document.getElementById('resultaat').innerHTML = weergave;
for(let i = 1; i < 2; i++) {
    document.getElementsByClassName('.resultaat + i').textContent = "<p>" + weergave + "</p>";
}

console.log(2);