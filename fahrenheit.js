/**
 * Converts Celsius to Fahrenheit.
 * @param {number} celsius - The temperature in Celsius.
 * @returns {number} - The temperature in Fahrenheit.
 */
function celsiusToFahrenheit(celsius) {
    return celsius * 9 / 5 + 32;
}

// Example usage with better error handling and variable names
const userInput = prompt("Enter temperature in Celsius:");
const celsius = parseFloat(userInput);

if (!isNaN(celsius)) {
    const fahrenheit = celsiusToFahrenheit(celsius);
    alert(`${celsius} Celsius is ${fahrenheit} Fahrenheit.`);
} else {
    alert("Please enter a valid number.");
}
