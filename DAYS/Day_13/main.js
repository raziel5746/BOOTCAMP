let body = document.querySelector("body")

let drum1 = document.querySelector("#drum1");
let drum2 = document.querySelector("#drum2");
let drum3 = document.querySelector("#drum3");
let drum4 = document.querySelector("#drum4");
let drum5 = document.querySelector("#drum5");
let drum6 = document.querySelector("#drum6");
let drum7 = document.querySelector("#drum7");
let drum8 = document.querySelector("#drum8");
let drum9 = document.querySelector("#drum9");

// let sound1 = document.getElementById("sound1");

function playSound() {
    switch (key) {
        case 65:
            sound1.currentTime = 0;
            sound1.play();
        break;
        case 83:
            sound2.currentTime = 0;
            sound2.play();
        break;
        case 68:
            sound3.currentTime = 0;
            sound3.play();
        break;
        case 70:
            sound4.currentTime = 0;
            sound4.play();
        break;
        case 72:
            sound4.currentTime = 0;
            sound5.play();
        break;
        case 74:
            sound6.currentTime = 0;
            sound6.play();
        break;
        case 75:
            sound7.currentTime = 0;
            sound7.play();
        break;
        case 76:
            sound8.currentTime = 0;
            sound8.play();
        break;
        case 32:
            sound9.currentTime = 0;
            sound9.play();
        break;
        default:
        break;
    }
}
var key = "";
// drum2.addEventListener("click", playSound)
body.addEventListener("keydown", function(e){
    key = e.keyCode;
    playSound();
})