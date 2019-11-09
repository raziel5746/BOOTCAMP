var fruitsRA = ["Banana", "Apples", "Oranges", "Blueberries"];

var display = document.getElementById("display");

var btn = document.getElementById("btn");

var i = -1;

function fruitFunction() {
    i++;
    switch (i) {
        case 0:
            display.innerHTML = fruitsRA;
            btn.innerHTML = "Remove 'Banana'";
        break;
        case 1:
            fruitsRA.splice(fruitsRA.indexOf("Banana"), 1);
            display.innerHTML = fruitsRA;
            btn.innerHTML = "Order alphabetically"; 
        
        break;
        case 2:
            fruitsRA.sort();
            display.innerHTML = fruitsRA;
            btn.innerHTML = "Add 'Kiwi' at the end"; 
        
        break;
        case 3:
            fruitsRA.push("Kiwi");
            display.innerHTML = fruitsRA;
            btn.innerHTML = "Remove 'Apples'"; 
        
        break;
        case 4:
            fruitsRA.splice(fruitsRA.indexOf("Apples"),1);
            display.innerHTML = fruitsRA;
            btn.innerHTML = "Reverse"; 
        
        break;
        case 5:
        fruitsRA.reverse();
            display.innerHTML = fruitsRA;
            btn.innerHTML = "Start again";
            fruitsRA = ["Banana", "Apples", "Oranges", "Blueberries"];
            i = -1;
        break;
    };
};


//----------------------
// Part 2 of the challenge:

var array2 = ["Banana",["Apples",["Oranges"],"Blueberries"]];

console.log(array2);

console.log(array2[1][1][0]);