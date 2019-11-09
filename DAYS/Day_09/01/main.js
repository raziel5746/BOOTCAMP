// // Exercise 1

// let family = {
//     lastName: "Perez",
//     familyMembers: 5,
//     address: "345 HaAlia St."
// };

// console.log("These are the PROPERTIES of the object: " + Object.getOwnPropertyNames(family));

// console.log("These are the VALUES of the object: " + Object.values(family));

// // OOOOOOOOOOOOR:

// let family = {
//     lastName: "Perez",
//     familyMembers: 5,
//     address: "345 HaAlia St."
// };

// console.log("These are the PROPERTIES of the object:")
// for (x in family) {
//     console.log(x);
// };

// console.log("\nThese are the VALUES of the object:")
// for (x in family) {
//     console.log(family[x])
// };



// // ----------------------------------------------------------

// // Exercise 2

// var building = {
//     number_levels : 4,
//     number_of_apt_by_level : {
//         "1": 3,
//         "2": 4,
//         "3": 9,
//         "4": 2
//     },
//     name_of_tenants : ["Sarah", "Dan", "David"],
//     number_of_rooms_and_rent:  {
//         "Sarah": [3, 2000],
//         "Dan": [4, 1000],
//         "David": [1, 10]
//     },
// };
// let aptsInLevel1 = building.number_of_apt_by_level["1"];
// let aptsInLevel3 = building.number_of_apt_by_level["3"];
// let sumApts = aptsInLevel1 +aptsInLevel3;
// let secondTenant = building.name_of_tenants[1];
// let secondTenantRooms = building.number_of_rooms_and_rent.Dan[0];
// let roomsAndRent = building.number_of_rooms_and_rent;


// console.log(building.number_levels)
// console.log(aptsInLevel1);
// console.log(aptsInLevel3);
// console.log(sumApts);
// console.log(secondTenant);
// console.log(secondTenantRooms);
//                         if (roomsAndRent.Sarah[1] + roomsAndRent.David[1] > roomsAndRent.Dan[1]){
//                             alert("You have to increase DAN's rent.");
//                             roomsAndRent.Dan[1] = roomsAndRent.Sarah[1] + roomsAndRent["David"][1];
//                             console.log("Now DAN's rent is " + roomsAndRent.Dan[1]);
//                         };
// console.log(building.number_of_rooms_and_rent.Dan[1])



// building[number_of_apt_by_level][1]


// for ((x % 2 !== 0) in building) {
//     console.log(x)
// }



// // ----------------------------------------------------------

// // Exercise 3

// let stock = {
//     'banana': 6,
//     'apple': 0,
//     'orange': 32,
// };

// let prices = {
//     'banana': 4,
//     'apple': 2,
//     'orange': 1.5,
// };

// let myGroceries = {
//     'banana': 0,
//     'apple': 0,
//     'orange': 0,
// };

// let myFruit = "";
// let fruitQuant = 0;
// let myBill = 0;


// function addFruit() {
//     myFruit = prompt("What fruit do you want?");
//     if (stock[myFruit] === 0) {
//         alert("Oh, sorry. We are out of stock.")
//     } else {
//         fruitQuant = parseInt(prompt("How many " + myFruit + "s do you want?"));
//         if (fruitQuant > stock[myFruit]) {
//             if (confirm("Oups, we only have " + stock[myFruit] + "\nDo you want " + stock[myFruit] + "?")) {
//                 myGroceries[myFruit] += stock[myFruit];
//                 stock[myFruit] -= 0;
//                 console.log(myFruit +"s: " + myGroceries[myFruit]);
//             };
//         } else {
//             myGroceries[myFruit] += fruitQuant;
//         };
//         stock[myFruit] -= fruitQuant;
//         console.log(myFruit +": " + myGroceries[myFruit]);
//     };
// };

// function calcBill() {
//     for (fruit in myGroceries) {
//         myBill += myGroceries[fruit] * prices[fruit];
//     }
//     alert("Your total bill is " + myBill);
// };



// // ----------------------------------------------------------

// // Exercise 4

// let contestant1 = {
//     fullName: "Master Yoda",
//     mass: 30,
//     height: 0.8,
//     bmi : function() {
//         return this.mass / this.height **2
//     },
// };

// let contestant2 = {
//     fullName: "Piccolo",
//     mass: 90,
//     height: 1.9,
//     bmi(){
//         return this.mass + this.height **2
//     },
// };

// var bmis = [];

// var contestants = [contestant1, contestant2];

// var indexOfMax = 0;

// var maxBmi = 0;

// let contestantsDiv = document.getElementById("contestantsDiv");

// function listBmis() {
//     for (let i = 0; i < contestants.length; i++){
//         bmis[i] = contestants[i].bmi();
//     };
// };

// function getMaxBmi() {
//     maxBmi = Math.max(...bmis);
//     indexOfMax = bmis.indexOf(maxBmi);
//     alert(contestants[indexOfMax].fullName + " has the highest BMI: " + contestants[indexOfMax].bmi());
// };

// function addContestant() {
//     contestants.push({
//         fullName: prompt("What's the FULLNAME of the new contestant?"),
//         mass: prompt("Tell us his/her MASS"),
//         height: prompt("Lastly, what's the contestant's HEIGHT?"),
//         bmi : function() {
//             return this.mass / this.height **2
//         },
//     });
//     contestantsDiv.innerHTML = "";
//     for (let i in contestants) {
//         contestantsDiv.innerHTML += contestants[i].fullName + "<br>";
//     };
// }

// for (let i in contestants) {
//     contestantsDiv.innerHTML += contestants[i].fullName + "<br>";
// };

// function startContest() {
//     listBmis();
//     getMaxBmi();
// };