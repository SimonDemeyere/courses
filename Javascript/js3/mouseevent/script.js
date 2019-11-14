window.onload = function() {
    let binnen = document.getElementById('binnen');
    let buiten = document.querySelector('#buiten');

    let x = 0;
    let y = 0;

    binnen.onmousemove = function () {
        binnen.innerHTML = x += 1;
    };

    binnen.onmouseover = function () {
        binnen.style.backgroundColor = 'pink';
    }
    binnen.onmouseout = function () {
        binnen.style.backgroundColor = 'rgb(255,255,0)';
    }
};