// // Exercise 1:

// var addressNumber = 1234;
// var addressStreet = "Sumstrit St.";
// var country = "Switzerland";

// var global_address = "I live at " + addressNumber + " " + addressStreet + " in " + country + ".";

// function printAddress(my_address){
//     document.getElementById("mydiv").innerHTML = "<h1>" + my_address + "</h1>";
// };

// printAddress(global_address);

// console.log(global_address);

// -----------------------------------------------------------


// // Exercise 2:

// var age = parseInt(prompt("How old are you?"));
// var country = prompt("Where are you from?");

// // if (age >=21){
// //   alert("BEER!")
// // } else if (age >= 18 && country == "USA") {
// //     alert("BEER!")
// // } else {
// //     alert("Have a soda you kid");
// // }

// if (age >= 18 && country != "USA" || age >= 21 && country == "USA") {
//     alert("BEER!");
// } else {
//     alert("Go home kiddo");
// };

// // -----------------------------------------------------------


// var num1 = parseInt(prompt("Type a number:"));
// var num2 = parseInt(prompt("Type a number:"));


// function max(x, y){
//     if (x > y) {
//         alert(x + " is the greater number");
//     } else if (y > x) {
//         alert(y + " is the greater number");
//     };
// };

// max(num1, num2);

// // -----------------------------------------------------------

// // Exercise 2

// var pets = ['cat', 'dog', 'fish', 'rabbit', 'cow', 'horse'];

// var animal = prompt("Choose an animal from this list: " + pets);

// var index = pets.indexOf(animal);

// pets.splice(index, 1);

// alert("The list now is: " + pets + ". You killed the " + animal + "!!!");

// // -----------------------------------------------------------


// // Exercise 3

var newDog = "Chihuahua";

console.log(newDog.length);

console.log(newDog.toUpperCase());

console.log(newDog.toLowerCase());

