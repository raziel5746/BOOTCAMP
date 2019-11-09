let letterHeight = 0;
let letterCenter = 0;
let rows = [];
let centerRow;


function drawLetterA() {
    letterHeight = parseInt(prompt("Define the letter's height by typing a number:"));
    rows = []
    letterCenter = letterHeight - 1;
    centerRow = Math.ceil(letterHeight / 2);

    for (let i = 0; i < letterHeight; i++) {
        rows[i] = [];
        for (let j = 0; j < letterHeight + i; j++) {
            rows[i].push(" ");
        }
    }

    for (let i = 0; i < letterHeight; i++) {
        rows[i].splice((letterCenter - i), 1, "*");
        rows[i].splice((letterCenter + i), 1, "*");
    }
    
    for (let i = 0; i < centerRow; i++) {
        rows[centerRow][letterCenter - i] = "*";
        rows[centerRow][letterCenter + i] = "*";
    }
    
    for (let i = 0; i < rows.length; i++) {
        console.log(rows[i].join(""));
    }
    
}
