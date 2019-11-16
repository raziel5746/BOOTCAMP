// let genres = document.getElementById("genres");


let classic = document.createElement("option");

genres.appendChild(classic);

classic.value = "classic";
classic.text = "Classic";

genres.value = "classic";



console.log("index: " + genres.selectedIndex);

console.log("value: " + genres.options[genres.selectedIndex].value);

console.log("text: " + genres.options[genres.selectedIndex].text);