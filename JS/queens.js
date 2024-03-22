function groupThePeople(groupSizes) {
    const groups = {}; // Store groups based on their size
    let result = [];

    for (let i = 0; i < groupSizes.length; i++) {
        const size = groupSizes[i];
        if (!groups[size]) groups[size] = []; // Initialize group if needed
        groups[size].push(i);

        // If a group is full, add to result and reset
        if (groups[size].length === size) {
            result.push(groups[size]);
            groups[size] = [];
        }
    }

    return result; // Return all the formed groups
}
console.log(groupThePeople([2,2,2,3,3,3,2]))



