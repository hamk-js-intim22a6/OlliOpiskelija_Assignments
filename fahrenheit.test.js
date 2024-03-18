/**
 * Unit tests for the celsiusToFahrenheit function.
 */

// Import the function to be tested
const celsiusToFahrenheit = require('./fahrenheit');

// Test case 1: Positive temperature
test('Converts positive Celsius temperature to Fahrenheit', () => {
  const celsius = 25;
  const expected = 77;
  const result = celsiusToFahrenheit(celsius);
  expect(result).toBe(expected);
});

// Test case 2: Negative temperature
test('Converts negative Celsius temperature to Fahrenheit', () => {
  const celsius = -10;
  const expected = 14;
  const result = celsiusToFahrenheit(celsius);
  expect(result).toBe(expected);
});

// Test case 3: Zero temperature
test('Converts zero Celsius temperature to Fahrenheit', () => {
  const celsius = 0;
  const expected = 32;
  const result = celsiusToFahrenheit(celsius);
  expect(result).toBe(expected);
});

// Test case 4: Decimal temperature
test('Converts decimal Celsius temperature to Fahrenheit', () => {
  const celsius = 37.5;
  const expected = 99.5;
  const result = celsiusToFahrenheit(celsius);
  expect(result).toBe(expected);
});