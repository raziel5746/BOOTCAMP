// var calcArray = [];
var calcString = "";

function myFunction(btn){
    // calcArray.push(btn);
    // console.log(calcArray);
    calcString += btn;
    calcDisplay.innerHTML =  calcString;
    console.log(calcString);
}

var calcDislpay = document.getElementById("calcDisplay");

function result(){
    calcDisplay.innerHTML =  eval(calcString);
    calcString = eval(calcString);
}

function calcClear(){
    calcString = "";
    calcDisplay.innerHTML =  0;
}