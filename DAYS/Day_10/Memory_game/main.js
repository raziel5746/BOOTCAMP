function shuffle(array) {
    array.sort(() => Math.random() - 0.5);
};

var cardsArr = [1, 1, 2, 2, 3, 3];

console.log(cardsArr)

shuffle(cardsArr);

console.log(cardsArr)

var cardsObj = {
    0: [cardsArr[0], false],
    1: [cardsArr[1], false],
    2: [cardsArr[2], false],
    3: [cardsArr[3], false],
    4: [cardsArr[4], false],
    5: [cardsArr[5], false],
}

var firstGuess = 0;
var firstBtn = "";
var freeze = false;

function check(card) {
    if (!freeze) {
        // btnArr[card].innerHTML = cardsArr[card];
        // btnArr[card].innerHTML = "<img src='images/" + cardsArr[card] +".jpg'>"
        btnArr[card].style.backgroundImage = "url(images/" + cardsArr[card] + ".jpg)";
        if (!firstGuess) {
            firstGuess = cardsObj[card][0];
            firstBtn = card;
        } else {
            if (cardsObj[card][0] == firstGuess) {
                cardsObj[card][1] = true;
                cardsObj[firstBtn][1] = true;
                console.log ("MATCH!");
            } else {
                console.log ("NOPE");
                freeze = true;
            }
            firstGuess = 0;
            firstBtn = "";
        };
    };
};

btnArr = document.getElementsByClassName("btn");

console.log (btnArr[0]);

// btnArr[0].innerHTML = "HI!"

function reset(){
    for(i = 0; i < cardsArr.length; i++) {
        if (!cardsObj[i][1]) {
            btnArr[i].style.backgroundImage = "url(images/back.jpg)";
        }
    }
    freeze = false;
};

function flipCard() {
    
}