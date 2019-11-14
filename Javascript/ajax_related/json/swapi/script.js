function getName() {
    let data = null;

    const xhr = new XMLHttpRequest();
    xhr.withCredentials = true;

    xhr.onload = onLoad;

    let id = 1;
    for (let i = 0; i < 20; i++) {
        console.log("https://rawg-video-games-database.p.rapidapi.com/developers/" + id);
        xhr.open("GET", "https://rawg-video-games-database.p.rapidapi.com/developers/" + id);
        xhr.setRequestHeader("x-rapidapi-host", "rawg-video-games-database.p.rapidapi.com");
        xhr.setRequestHeader("x-rapidapi-key", "dfd5de5d8bmshe010cb47fd4ee39p10a149jsn90fc5140d645");
        id += 1

    }

    xhr.send(data);
}

function onLoad() {
    let id = 0;
    const city = document.getElementById("div");
    // city.options.length = 0;
    const data = JSON.parse(this.responseText);

    console.log(data);
    console.log(data.name);

    for (let i = 1; i < 20 + 1; i++) {
        id = i;
        const p = document.getElementById('p');
        // p.textContent += `${data.results[i].name}`;
        console.log(data.name);
    }
}

function init() {
    getName();
}

window.addEventListener("load", init);
