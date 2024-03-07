let a = 5;
let b = 6;
let total = a+b;


var button = document.getElementById('myButton');

// Define a function to be called when the button is clicked
function handleClick() {
    alert('Button clicked!');
    document.getElementById('abc').innerText = total

}

// Add an event listener to the button, listening for the 'click' event
button.addEventListener('click', handleClick);

function incrementVisitCount() {
    if (typeof(Storage) !== "undefined") {
      if (localStorage.visitCount) {
        localStorage.visitCount = Number(localStorage.visitCount) + 1;
      } else {
        localStorage.visitCount = 1;
      }
      document.getElementById("visitCount").innerHTML = "You have visited this page " + localStorage.visitCount + " time(s).";
    } else {
      document.getElementById("visitCount").innerHTML = "Sorry, your browser does not support web storage...";
    }
  }

  // Call the function when the page loads
  window.onload = function() {
    incrementVisitCount();
  };