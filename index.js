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
