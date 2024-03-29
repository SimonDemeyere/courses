let scores, activePlayer, roundScore, gamePlaying;

init();

function nextPlayer() {
    activePlayer === 0 ? activePlayer = 1 : activePlayer = 0;
    roundScore = 0;
    document.getElementById('current-0').textContent = '0';
    document.getElementById('current-1').textContent = '0';
    document.querySelector('.player-0-panel').classList.toggle('active');
    document.querySelector('.player-1-panel').classList.toggle('active');
    document.querySelector(`#dice`).style.display = "none";
}

document.querySelector('.btn-new').addEventListener('click', init);
document.querySelector('.btn-roll').addEventListener('click', function() {
    if (gamePlaying) {
        let dice = Math.floor(Math.random() * 6) + 1;

        let diceDOM = document.querySelector('.dice');
        diceDOM.style.display = 'block';
        diceDOM.src = `dice-${dice}.png`;

        if (dice !== 1) {
            roundScore += dice;
            document.querySelector(`#current-${activePlayer}`).textContent = roundScore;
        } else {
            roundScore = 0;
            document.querySelector(`#current-${activePlayer}`).textContent = 0;
            nextPlayer();
        }
    }
});
document.querySelector('.btn-hold').addEventListener('click', function() {
    if (gamePlaying) {
        scores[activePlayer] += roundScore;

        document.querySelector(`#score-${activePlayer}`).textContent = scores[activePlayer];

        if (scores[activePlayer] >= 100) {
            document.querySelector(`#name-${activePlayer}`).textContent = "Winner";
            document.querySelector(`#dice`).style.display = "none";
            document.querySelector(`#player-${activePlayer}-panel`).classList.add('winner');
            document.querySelector(`#player-${activePlayer}-panel`).classList.remove('active');
            gamePlaying = false;
        }
        nextPlayer();
    }
});

function init() {
    scores = [0, 0];
    activePlayer = 0;
    roundScore = 0;
    gamePlaying = true;

    document.querySelector('.dice').style.display = 'none';
    document.getElementById('score-0').textContent = '0';
    document.getElementById('score-1').textContent = '0';
    document.getElementById('current-0').textContent = '0';
    document.getElementById('current-1').textContent = '0';
    document.getElementById('name-0').textContent = 'LEEG';
    document.getElementById('name-1').textContent = 'LEEG';
    document.querySelector('.player-0-panel').classList.remove('winner');
    document.querySelector('.player-0-panel').classList.remove('active');
    document.querySelector('.player-1-panel').classList.remove('winner');
    document.querySelector('.player-1-panel').classList.remove('active');
    document.querySelector('.player-0-panel').classList.add('active');
}