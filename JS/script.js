class Character {
    constructor(name, age, backstory) { // Add more properties as needed
        this.name = name;
        this.age = age;
        this.backstory = backstory;
    }
}

// Get modal elements
const modal = document.getElementById("characterModal");
const createCharacterButton = document.getElementById("createCharacterButton");
const closeButton = document.getElementsByClassName("close")[0];

// Open the modal when the button is clicked
createCharacterButton.onclick = function () {
    modal.style.display = "block";
}

// Close the modal when the X is clicked
closeButton.onclick = function () {
    modal.style.display = "none";
}

// Close the modal when the user clicks anywhere outside of the modal content
window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

// Function to display a character on the page 
// (You'll want to modify this to style how you see fit)
const displayCharacter = (character) => {
    const characterDisplay = document.getElementById('characterDisplay');
    const characterElement = document.createElement('div');
    characterElement.innerHTML = `
    <h3>${character.name}</h3>
    <p>Age: ${character.age}</p>
    <p>Backstory: ${character.backstory}</p>
  `;
    characterDisplay.appendChild(characterElement);
}

// Add functionality to the form to create a character and display it on the page 
// (ensure form has id="createForm")
const createForm = document.getElementById('characterDisplay');

createForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const name = createForm.elements['name'].value; // ensure name input has name="name"
    // Add additional properties as needed
    const newCharacter = new Character(name);
    displayCharacter(newCharacter);
    modal.style.display = 'none';
    createForm.reset();
})