// // Exercise 1

// var colorsAR = ['red', 'blue', 'white', 'green', 'silver', 'purple', 'orange'];

// var suffix = "";

// for (var i = 0; i < colorsAR.length; i = i+2) {
//     alert("My #" + (i + 1) + " choice is " + colorsAR[i]);
// };

// for (var i = 0; i < colorsAR.length; i++) {
//     switch (i) {
//         case 0:
//         suffix = "st";
//         break;
//         case 1:
//         suffix = "nd";
//         break;
//         case 2:
//         suffix = "rd";        
//         break;
//         default:
//         suffix = "th";
//         break;
//     }

//     alert("My " + (i + 1) + suffix + " choice is " + colorsAR[i]);
// };



// // --------------------------------------------------------

// // Exercise 2

// for (let i = 0; i <= 15; i++){
//     switch (true) {
//         case (i === 0):
//             alert(i + " is not actually a number, so it's not even nor odd. Sorry...");
//         break;
//         case (i % 2 === 0):
//             alert(i + " is an even number.");
//         break;
//         default:
//             alert(i + " is an odd number.");
//         break;
//     }
// };



// // --------------------------------------------------------

// // Exercise 3

var names= ["john", "sarah", 23, "Rudolf", 34];

function capitalizeFirstLetter(string) {
    return  string[0].toUpperCase() + string.slice(1);
};

for (let i = 0; i < names.length; i++) {
    if (typeof names[i] !== "string") {
        continue;
    } else {
        if (names[i][0] === names[i][0].toLowerCase()) {
            names[i] = capitalizeFirstLetter(names[i]);
            console.log(names[i]);
        };
    };
};