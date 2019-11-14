let rij = '';

for (let i = 0; i < 100; i++) {
    if (i < 10){
        rij += `0${i},`;
    } else {
        rij += `${i},`
    }
}

console.log(rij.slice(0, -1));