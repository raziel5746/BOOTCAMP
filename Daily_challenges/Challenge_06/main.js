var calcString = "";
var calcDislpay = document.getElementById("calcDisplay");

function myFunction(btn){
    calcString += btn;
    calcDisplay.innerHTML =  calcString;
    console.log(calcString);
}


function result(){
    var calcResult = eval(calcString);
    calcDisplay.innerHTML = calcResult.toFixed(9);
    console.log(calcString + "=" + calcResult);
    calcString = calcResult;
}

function calcClear(){
    calcString = "";
    calcDisplay.innerHTML =  0;
}