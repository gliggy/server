console.log("hello world!");
console.log(document.documentURI);

var toggler = document.getElementsByClassName("caret");
var i;

for (i = 0; i < toggler.length; i++) {
  toggler[i].addEventListener("click", function() {
    this.parentElement.querySelector(".nested").classList.toggle("active");
    this.classList.toggle("caret-down");
  });
}

//var myElement = document.getElementById("lilili");
//document.getElementById("demo").innerHTML = "The text from the intro paragraph is " + myElement.innerHTML;

//document.getElementById("lilili").innerHTML = "Hello World!";

