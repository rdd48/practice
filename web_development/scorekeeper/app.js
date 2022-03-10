const p1 = {
    score: 0,
    button: document.querySelector('.b-p1'),
    display: document.querySelector('#pl1')
}

const p2 = {
    score: 0,
    button: document.querySelector('.b-p2'),
    display: document.querySelector('#pl2')
}

let gameOver = false;
let playTo = 5;
const select = document.querySelector('select')
select.addEventListener('change', () => {
    playTo = parseInt(select.value);
    console.log(playTo)
    resetScore();
})

function updateScore(player, opp) {
    if (!gameOver) {
        player.score += 1;

        if (player.score === playTo) {
            player.display.classList.add('color-win')
            opp.display.classList.add('color-lose')
            gameOver = true;
        }

        player.display.textContent = player.score;
    }
}

function resetScore() {
    for (let player of [p1, p2]) {
        player.score = 0;
        player.display.textContent = player.score;
        player.display.classList.remove('color-win')
        player.display.classList.remove('color-lose')
    }
    gameOver = false;
}

p1.button.addEventListener('click', () => updateScore(p1, p2));
p2.button.addEventListener('click', () => updateScore(p2, p1));

const reset = document.querySelector('.b-reset');
reset.addEventListener('click', resetScore)

