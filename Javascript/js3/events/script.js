let numClicks = 0;

window.onload = function () {
    console.log('page loaded');
    let resultaat = document.querySelector('#resultaat');
    let btn = document.querySelector('#btn');
    btn.addEventListener('click', function () {
        numClicks++;
        resultaat.innerHTML = `${numClicks} keer geklikt.`;
    }, false);
};