let body = document.querySelector("body");
let myForm = document.createElement("form");
let student_first_name = document.createElement("input");
let student_last_name = document.createElement("input");
let submitBtn = document.createElement("button");
let howManyStudentsBtn = document.createElement("button");

let howManyStudents = 0;

body.appendChild(myForm);
myForm.appendChild(student_first_name);
myForm.appendChild(student_last_name);
myForm.appendChild(submitBtn);
myForm.appendChild(howManyStudentsBtn);



student_first_name.placeholder = "First Name";
student_last_name.placeholder = "Last Name";
submitBtn.innerText = "Submit";
howManyStudentsBtn.innerText = "How many students?"

var newUl;
var newLi;
function createList() {
    newUl = document.createElement("ul");
    body.appendChild(newUl);

    newLi = document.createElement("li");
    newUl.appendChild(newLi);
    
    newLi.innerHTML = student_first_name.value + " " + student_last_name.value;
    
    addDelBtn();

    event.preventDefault();

    student_first_name.value = "";
    student_last_name.value = "";
}

function addDelBtn() {
    let delBtn = document.createElement("button");
    newLi.appendChild(delBtn);
    delBtn.innerText = "X";
    delBtn.addEventListener("click", function(){
        this.parentElement.remove();
    })
}

function calcStudents() {
    howManyStudents = document.getElementsByTagName("li").length;
    console.log(howManyStudents);
    event.preventDefault();
    alert("There are " + howManyStudents + " students registered in the class");

}


submitBtn.addEventListener("click", createList);
howManyStudentsBtn.addEventListener("click", calcStudents);