// Listen for messages from the main script
self.onmessage = function(event) {
  const number = event.data;
  const factorial = calculateFactorial(number);
  self.postMessage(factorial); // Send result back to the main script
};

// Function to calculate factorial using recursion
function calculateFactorial(n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * calculateFactorial(n - 1);
  }
}
