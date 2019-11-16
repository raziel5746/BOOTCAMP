// BODY
let body = document.querySelector("body");

let rootDiv = document.querySelector("#root");

// H1
let h1 = document.createElement("h1");
rootDiv.appendChild(h1);
h1.innerText = "Shopping List";

// TEXT INPUT
let input = document.createElement("input");
input.innerText = "Add item";
rootDiv.appendChild(input);

// BUTTON 1 (addBtn)
let btnAdd = document.createElement("button");
btnAdd.innerText = "Add";
rootDiv.appendChild(btnAdd);

// BUTTON 2 (btnClearAll)
let btnClearAll = document.createElement("button");
btnClearAll.innerText = "Clear all";
rootDiv.appendChild(btnClearAll);

// UL
let myList = document.createElement("ul");
rootDiv.appendChild(myList);

let itemText = "";

function toggle() {
    this.classList.toggle("toggle");
}

function addItem() {
    if (input.value !== "") {
        let newItem = document.createElement("li");
        newItem.innerText = input.value;
        myList.appendChild(newItem);
        input.value = "";
        newItem.addEventListener("click", toggle);
        let newDeleteButton = document.createElement("button");
        newDeleteButton.innerText = "x";
        newItem.appendChild(newDeleteButton);
        newDeleteButton.addEventListener("click", deleteListItem);
    }
}

function deleteListItem() {
    this.parentElement.remove();
}

function clearAll() {
    let allListItems = document.querySelectorAll("li");
    for (let i = 0; i < allListItems.length; i++) {
        allListItems[i].remove();
    }
}

btnAdd.addEventListener("click", addItem);
btnClearAll.addEventListener("click", clearAll);

input.addEventListener("keypress", function(e) {
    if (e.key === "Enter") {
        addItem();
    }
});

