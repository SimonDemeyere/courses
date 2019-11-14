let test;
let test2 = [];

/*let Simon = {
    naam: 'Simon',
    geboortedatum: 1997,
    geslacht: 'M'
};*/

let Persoon = function (naam, geboortedatum, geslacht) {
    this.naam = naam;
    this.geboortedatum = geboortedatum;
    this.geslacht = geslacht;

};

Persoon.prototype.berekenLeeftijd = function () {
    console.log(2019 - this.geboortedatum);
};

let simon = new Persoon('Simon', 1997, 'M');
let louise = new Persoon('Louise', 1998, 'V');

simon.berekenLeeftijd();
louise.berekenLeeftijd();