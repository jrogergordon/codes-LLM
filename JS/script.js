class Character {
    constructor(name, age, backstory) {
        this.name = name;
        this.age = age;
        this.backstory = backstory;
    }
}
let storedCharacters = [];
// Get elements
const modal = document.getElementById("characterModal");
const createCharacterButton = document.getElementById("createCharacterButton");
const closeButton = document.getElementsByClassName("close")[0];
const createForm = document.getElementById("createForm");
const characterDisplay = document.getElementById('characterDisplay');

const viewCharactersButton = document.getElementById("viewCharactersButton");
const viewCharactersModal = document.getElementById("viewCharactersModal");
const createdCharactersDisplay = document.getElementById('createdCharactersDisplay');

const displayCharactersInViewModal = () => {
    createdCharactersDisplay.innerHTML = ''; // Clear previous content
    characterDisplay.childNodes.forEach(characterElement => {
        createdCharactersDisplay.appendChild(characterElement.cloneNode(true));
    });
}
viewCharactersButton.onclick = function () {
    displayCharactersInViewModal();
    viewCharactersModal.style.display = "block";
}

const displayCharacter = (character) => {
    const characterElement = document.createElement('div');
    characterElement.classList.add('character-card');
    // ... existing characterElement content ...
    characterDisplay.appendChild(characterElement);
}

closeDisplayButton.onclick = function () {
    characterDisplayModal.style.display = "none";
}

const displayCharacters = () => {
    characterList.innerHTML = ''; // Reset character list


    storedCharacters.forEach(character => { // Assume you have an array 'storedCharacters'
        const characterElement = document.createElement('div');
        characterElement.classList.add('character-card');
        characterElement.innerHTML = `
            <h3>${character.name}</h3>
            <p>Age: ${character.age}</p>
            <p>Backstory: ${character.backstory}</p>
        `;
        characterList.appendChild(characterElement);
    });
}

// Modal functionality
createCharacterButton.onclick = function () {
    modal.style.display = "block";
}

closeButton.onclick = function () {
    modal.style.display = "none";
}

window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

// Create and display a character

// Create character from form
createForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const name = createForm.elements['name'].value;
    const age = createForm.elements['age'].value;
    const backstory = createForm.elements['backstory'].value;

    const newCharacter = new Character(name, age, backstory);
    storedCharacters.push(newCharacter);

    modal.style.display = 'none';
    createForm.reset();
})