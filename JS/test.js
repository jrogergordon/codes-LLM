function calc(str) {
    const expr = str.trim().split(/([+\-*/])/);
    const nums = expr.filter(x => !isNaN(x));
    const op = expr.filter(x => x !== ' ' && x !== '');

    if (nums.length !== 2 || op.length !== 1) {
        throw new Error(`Invalid input: ${str}`);
    }

    const num1 = parseFloat(nums[0]);
    const num2 = parseFloat(nums[1]);
    const operator = op[0];

    switch (operator) {
        case '+':
            return num1 + num2;
        case '-':
            return num1 - num2;
        case '*':
            return num1 * num2;
        case '/':
            if (num2 === 0) {
                throw new Error('Cannot divide by zero');
            }
            return num1 / num2;
        default:
            throw new Error(`Unknown operator: ${operator}`);
    }
}


let ans = calc("2+2");
console.log(ans)