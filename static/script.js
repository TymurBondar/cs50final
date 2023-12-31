import { displayWord, wordContainer } from './helpers.js';

const gameLength = 20;
let mistakes = 0;
let totalChars = 0;
let counter = 0;
let startTime;
let endTime;
let playedTime;
let accuracy;
let res;

const typingForm = document.getElementById("typing-form");
const typedWord = document.getElementById("typedWord");

// Define the event listener function
const eventListenerFunction = (event) => {
    if (event.key === " ") {
        counter++;
        let input = typedWord.value;
        totalChars += input.length;
        let goal = wordContainer.textContent
        //check for mistakes
        if (input.trim() !== goal) {
            mistakes++;
        }

        displayWord();
        if (counter >= gameLength) {
            // Remove the event listener here
            typingForm.removeEventListener("keydown", eventListenerFunction);
            endTime = new Date();
            //calculate the speed
            playedTime = (endTime - startTime) / 1000; //gives time in seconds
            res = Math.round((totalChars / playedTime) * 60); //gives chars per minute
            //calculate accuracy
            accuracy = Math.round(100 * (gameLength - mistakes) / gameLength * 100) / 100;
            typedWord.disabled = true;
            let resultField = document.getElementById("result");
            resultField.textContent = `Your speed is ${res} characters per minute with  ${accuracy}% accuracy`;

            var data = {
                res: res,
                accuracy: accuracy
            };
            fetch('/save_res', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            })
        }
    }
};

// Add the event listener
typingForm.addEventListener("keydown", eventListenerFunction);
typingForm.addEventListener("keyup", (event) => {
    if (event.key === " ") {
        typedWord.value = "";
    }
})
startTime = new Date();

displayWord();
