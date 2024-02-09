function multiplyLargeNumbers(a, b) {
    // Split the numbers into arrays of digits
    const aDigits = a.toString().split('');
    const bDigits = b.toString().split('');

    // Initialize the result array
    const result = [];

    // Iterate through the digits of each number
    for (let i = 0; i < aDigits.length; i++) {
        for (let j = 0; j < bDigits.length; j++) {
            // Multiply the current digits and add to the result
            const product = parseInt(aDigits[i]) * parseInt(bDigits[j]);
            result.push(product);
        }
    }

    // Flatten the result array and convert to a string
    flatResult = result.reduce((acc, val) => acc.concat(val), []);
    const resultString = flatResult.join('');

    // Return the result as a string
    return resultString;
}

let ans1 = multiplyLargeNumbers("123", "456");
let ans2 = multiplyLargeNumbers("2", "3");
console.log(ans1, ans2);