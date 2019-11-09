// // Exercise 1

// var myAge = parseInt(prompt("How old are you?"));
// var momAge = 0;
// var dadAge = 0;

// function ageCalc(age){
//     momAge = age * 2;
//     dadAge = momAge * 1.2;
//     alert("Your mom is " + momAge + " years old.");
//     alert("And your dad is " + dadAge + " years old.");
// };

// ageCalc(myAge);



// // ----------------------------------------------------------------------------------

// // Exercise 2

var myCity = undefined;
var myNights = 0;
var myDays = 0;

function plane_ride_cost(city) {
    switch (city) {
        case "london":
            return 183;
        case "paris":
            return 220;
        default:
            return 300;
    };
};

function hotel_cost(nights) {
    var price = 140;
    return price * nights;
};

function rental_car_cost(days) {
    if (days >= 7) {
        return (days * 40 - 50);
    } else if (days >= 3) {
        return (days * 40 - 20);
    } else {
        return days * 40;
    };
};

function trip_cost(city, nights, days) {
    var finalPrice = plane_ride_cost(city) + hotel_cost(nights) + rental_car_cost(days);
    return finalPrice;
};


myCity = prompt("WHAT CITY are you flying to?");

while (myCity === "") {
    myCity = prompt("WHAT CITY are you flying to?").toLowerCase();
};

myNights = prompt("HOW MANY NIGHTS are you planning to stay?");
while (myNights === "") {
    myNights = prompt("HOW MANY NIGHTS are you planning to stay?");
};

myDays = prompt("Lastly, for HOW MANY DAYS do you want to rent a car?");
while (myDays === "") {
    myDays = prompt("Lastly, for HOW MANY DAYS do you want to rent a car?");
};

alert("Your trip is going tu cost a TOTAL of " + trip_cost(myCity, myNights, myDays) + "\nHere is the detail:" + "\nPlane ticket: $" + plane_ride_cost(myCity) + "\nHotel: $" + hotel_cost(myNights) + "\nRental car: $" + rental_car_cost(myDays) + "\nHave a nice trip!");