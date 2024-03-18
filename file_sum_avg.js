const fs = require('fs');

function readAndCalculate(filePath) {
    try {
        const fileContent = fs.readFileSync(filePath, 'utf-8');
        const lines = fileContent.split('\n');
        const numbers = [];

        lines.forEach((line) => {
            const integers = line.match(/-?\d+/g);
            if (integers) {
                integers.forEach((integer) => {
                    numbers.push(parseInt(integer));
                });
            }
        });

        if (numbers.length === 0) {
            throw new Error('No integers found in the file.');
        } else {
            const sum = numbers.reduce((acc, curr) => acc + curr, 0);
            const average = sum / numbers.length;

            console.log('Sum:', sum);
            console.log('Average:', average);
        }
    } catch (error) {
        console.error('Error:', error.message);
    }
}
function testReadAndCalculate() {
    const filePath = 'file.txt';
    readAndCalculate(filePath);
}

const filePath = 'file.txt';
readAndCalculate(filePath);
