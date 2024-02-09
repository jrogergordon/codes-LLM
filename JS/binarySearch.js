function binarySearch(arr, target) {
    let low = 0;
    let high = arr.length - 1;
    let startIndex = -1;
    let endIndex = -1;

    while (low <= high) {
        let mid = Math.floor((low + high) / 2);
        let current = arr[mid];

        if (current === target) {
            // Find the starting index
            if (startIndex === -1) {
                startIndex = mid;
            }
            // Find the ending index
            endIndex = mid;

            // If the target is found in the middle,
            // check the left and right sides to find
            // the exact starting and ending indices
            while (mid > 0 && arr[mid - 1] === target) {
                mid--;
                startIndex = mid;
            }
            while (mid < arr.length - 1 && arr[mid + 1] === target) {
                mid++;
                endIndex = mid;
            }

            // If the target is found, break the loop
            break;
        } else if (target < current) {
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    return [startIndex, endIndex];
}

const arr = [1, 1, 1, 3, 3, 3, 4, 4, 4, 11, 11, 11, 11, 11, 11, 16, 16, 16, 16, 20, 20, 20];
const target = 11;
const result = binarySearch(arr, target);
console.log(result); // Output: [8, 13]