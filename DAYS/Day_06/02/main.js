// x = parseInt(prompt("Enter a number:"));

// function square(num){
//     // return num * num;
//     return Math.pow(num, 2);
// };

// alert(square(x));

// ------------------------------------------------------


// var x = parseInt(prompt("Type a number:"));
// var y = parseInt(prompt("Type another number:"));
// var z = parseInt(prompt("Aaaand, the last number:"));


// function my_calc(num1, num2, num3){
//     return num1 * num2 - num3;
// }

// alert("So, " + x + " times " + y + " minus " + z + " equals " + my_calc(x, y, z));

// -------------------------------------------------------

// var countries = [
//     "USA",
//     "Israel",
//     "South Africa",
//     "England",
//     "France",
//     "Italy",
// ];

// console.log(countries[5]);

// -------------------------------------------------------


// var text = "This is just some dummy text";

// alert(text.indexOf("some"));

// -------------------------------------------------------


// var text = "This is just some dummy text";

// console.log(text.substring(40, 45)); //returns "some"

// -------------------------------------------------------



// function addHeading(text, div_id){
//     var the_div_we_want = document.getElementById(div_id);
//     the_div_we_want.innerHTML = "<h1>" + text + "</h1>";
// };

// -------------------------------------------------------



function changeColor(my_color, div_id){
    document.getElementById(div_id).style.backgroundColor = my_color;
};

