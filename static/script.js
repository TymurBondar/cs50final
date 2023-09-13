const words = [
    "the", "be", "to"
];

function getRandomInt(max) {
    return Math.floor(Math.random() * max);
}

let currentWordIndex = 0;
let mistakes = 0;
let totalChars = 0;
let startTime;
let endTime;
let playedTime;
let counter = 0;
let accuracy;
let res;

const wordContainer = document.getElementById("word-container");
const resultContainer = document.getElementById("result");
const typingForm = document.getElementById("typing-form");
const typedWord = document.getElementById("typedWord");

function displayWord() {
    typedWord.value = "";
    wordContainer.textContent = words[getRandomInt(words.length)];
}

// wordContainer.textContent represents the word to type
// input.value represent the word that the user entered
// wordContainer.textContent !== input.value


// Define the event listener function
const eventListenerFunction = (event) => {
    if (event.keyCode === 32) {
        counter++;
        totalChars += wordContainer.textContent.length;
        let input = typedWord.value;
        let goal = wordContainer.textContent
        //check for mistakes
        if (input.trim() !== goal) {
            mistakes++;
        }

        displayWord();
        if (counter >= words.length) {
            // Remove the event listener here
            typingForm.removeEventListener("keyup", eventListenerFunction);
            endTime = new Date();
            //calculate the speed
            playedTime = (endTime - startTime) / 1000; //gives time in seconds
            res = Math.round((totalChars / playedTime) * 60); //gives chars per minute
            console.log(`You speed is ${res} characters per minute`);
            //calculate accuracy
            accuracy = (words.length - mistakes) / words.length * 100;
            console.log(`Your accuracy is ${accuracy}%`);
            typedWord.disabled = true;
            resultField = document.getElementById("result");
            resultField.textContent = `Your speed is ${res} characters per minute with  ${accuracy}% accuracy`;
        }
    }
};

// Add the event listener
typingForm.addEventListener("keyup", eventListenerFunction);
startTime = new Date();


displayWord();
