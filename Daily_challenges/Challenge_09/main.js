
function start() {
    let mySentence = prompt("Write a sentence:");
    let wordArray = mySentence.split(" ");
    let longestWord = 0;
    let framed = document.getElementById("framed");
    let newWordArray = [];
    let finalString = "";
    
    for (let i = 0; i < wordArray.length; i++) {
        if (wordArray[i].length > longestWord) {
            longestWord = wordArray[i].length;
        };
    };
    
    for (let i = 0; i < wordArray.length; i++) {
        newWordArray[i] = "*" + "x" + wordArray[i];
        while (newWordArray[i].length <= (longestWord + 2)) {
            newWordArray[i] += "x";
        };
    
        newWordArray[i] += "*<br>";
    };
    
    for (let i = 0; i < newWordArray.length; i++) {
        finalString += newWordArray[i];
    };
    
    while (finalString.indexOf("x") > 0) {
        finalString = finalString.replace("x", "&nbsp");
    };

    console.log(finalString)
    
    let starsLine = "";
    
    for (i = 0; i <= longestWord + 3; i++) {
        starsLine += "*";
    };
    
    starsLine += "<br>";
    
    finalString = starsLine + finalString + starsLine;
    
    framed.innerHTML = finalString;
};