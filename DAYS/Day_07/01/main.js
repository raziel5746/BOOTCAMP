// var myYear = prompt("What year were you born in?");

// var futureYear = prompt("Choose a year in the future:");

// var futureAge = futureYear - myYear;

// alert("In " + futureYear + " you will be " + futureAge + " years old.");


// -------------------------------------------------------------------

// // Exercises: Conditionals

// // Exercise 1

// var number = prompt("Type a number:");

// var result = number % 2;

// if (isNaN(number)) {
//     alert("I said a NUMBER!");
// } else if (result == 0){
//     alert("Your number is even.");
// } else {
//     alert("Your number is not even.");
// };


// // -------------------------------------------------------------------

// // Exercise 3

// var myLang = prompt("Hello! Tell me, what language do you speak?");

// myLang = myLang.toLowerCase();

// myImage = document.getElementById("image");

// if (myLang == "french") {
//     alert("Bounjour!");
// } else if (myLang == "english") {
//     alert("Hello!");
// } else if (myLang == "hebrew") {
//     alert("Shalom!");
// } else if (myLang == "spanish") {
//     alert("Hola!");
// } else {
//     myImage.src = "http://www.myiconfinder.com/uploads/iconsets/256-256-49dafa57cbe8d8f78001848b36639ebc-emoticon.png";
//     alert("I'm sorry, I don't speak that language.")
// };




// // -------------------------------------------------------------------

// // // Exercise 4

// var lastGrade;
// var lastCoefficient;
// var userGrades = [];
// var userCoefficients = [];
// var average = 0;

// function gradeFunction(){
//     lastGrade = prompt("Type a grade:");
//     userGrades.push(lastGrade);
//     console.log("Current grades: " + userGrades);
//     lastCoefficient = prompt("Type the coefficient:");
//     userCoefficients.push(lastCoefficient);
//     console.log("Current coefficients: " + userCoefficients);
// };

// function averageFunction(){
//     if (!userGrades.length || !userCoefficients.length){
//         alert("There are no grades or coefficients loaded.");
//     } else {
//         for (var i = 0; i < userGrades.length; i++) {
//             average += userGrades[i]*userCoefficients[i];
//         };
//         average = average/userGrades.length;
//         alert("The average is " + average);
//     };
// };

// function resetFunction() {
//     userCoefficients = [];
//     userGrades = [];
//     };


// // -------------------------------------------------------------------

// // Exercise 5

// var grade = prompt("Input a GRADE please:");

// switch(true) {
//     case (grade >= 90):
//     alert("A");
//     break;
//     case (grade >= 80):
//     alert("B");
//     break;
//     case (grade >= 70):
//     alert("C");
//     break;case (grade >= 0):
//     alert("D");
//     break;
// };


// -------------------------------------------------------------------
// -------------------------------------------------------------------

// // Exercises: DataTypes

// // Exercise 1

var people = ["Greg", "Mary", "Devon", "James"];

for (let i = 0; i < people.length; i++) {
    console.log(people[i]);
};

people