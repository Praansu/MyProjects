
// Simple calculator script by a human developer
// Handles all the math and button clicks

// Reference the screen elements so we can update them easily
const mainScreen = document.getElementById('calc-display');
const historyLabel = document.getElementById('history');

// This adds a number or operator to the screen when a button is clicked
function addToScreen(value) {
    // If the screen shows an error, clear it before starting fresh
    if (mainScreen.value === "Error" || mainScreen.value === "NaN") {
        mainScreen.value = "";
    }

    // Logic to stop users from entering two dots in one number
    // We split by operators and check the last part for an existing dot
    if (value === '.' && mainScreen.value.split(/[\+\-\*\/]/).pop().includes('.')) {
        return;
    }

    // Don't let the text get too long or it'll overflow the display
    if (mainScreen.value.length < 15) {
        mainScreen.value += value;
    }
}

// Reset everything back to zero/blank
function clearAll() {
    mainScreen.value = "";
    historyLabel.innerText = "";
}

// Just remove the last character (like a backspace)
function backspace() {
    mainScreen.value = mainScreen.value.slice(0, -1);
}

// The main function that does the math
function runCalculation() {
    try {
        const inputString = mainScreen.value;
        if (!inputString) return;

        // Put the old math in the small history line at the top
        historyLabel.innerText = inputString + " =";

        // Using Function() to do the math safely side-step eval() issues
        const total = new Function('return ' + inputString)();

        // Check if the result is a valid number
        if (Number.isFinite(total)) {
            // Clean up the decimal places so it's not super long
            let finalOutput = Number(total.toPrecision(12)).toString();

            // If the number is still huge, use scientific notation
            if (finalOutput.length > 14) {
                finalOutput = Number(total).toExponential(8);
            }
            mainScreen.value = finalOutput;
        } else {
            mainScreen.value = "Error";
        }

    } catch (err) {
        // If they type something weird like "5++5", just show Error
        mainScreen.value = "Error";
    }
}

// Allow typing numbers directly on the physical keyboard
document.addEventListener('keydown', (e) => {
    const key = e.key;

    // Numbers keys
    if (/[0-9]/.test(key)) {
        addToScreen(key);
    }
    // Math symbol keys
    else if (['+', '-', '*', '/'].includes(key)) {
        addToScreen(key);
    }
    // Pressing Enter runs the math
    else if (key === 'Enter') {
        runCalculation();
    }
    // Esc or 'C' key resets display
    else if (key === 'Escape' || key.toLowerCase() === 'c') {
        clearAll();
    }
    // Backspace works as expected
    else if (key === 'Backspace') {
        backspace();
    }
    // Dot/Period key
    else if (key === '.') {
        addToScreen('.');
    }
});
