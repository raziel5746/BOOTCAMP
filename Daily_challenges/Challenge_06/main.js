var calcString = "";

function myFunction(btn){
    calcString += btn;
    calcDisplay.innerHTML =  calcString;
    console.log(calcString);
}

var calcDislpay = document.getElementById("calcDisplay");

function result(){
    var calcResult = eval(calcString);
    calcDisplay.innerHTML = calcResult;
    console.log(calcString + "=" + calcResult);
    calcString = calcResult;
}

function calcClear(){
    calcString = "";
    calcDisplay.innerHTML =  0;
}