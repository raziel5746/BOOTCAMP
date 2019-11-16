let table = document.body.firstElementChild;
let rows = document.querySelectorAll("tr");

console.log(rows.length)

for (let i = 0; i < rows.length; i++) {
    rows[i].children[i].style.background = "red";
}

for (let i = rows.length; i < )