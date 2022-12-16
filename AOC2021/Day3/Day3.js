let counter = 0;
let reducerIndex = 0;

const bitsReducer = (arr, sortBit, keepBit) => {
    if (arr.length === 1) {
    counter, (reducerIndex = 0);
    return parseInt(arr, 2);
}

    let tempArr = \[\];
    let oneCount = null;
    const createKeepBit = (item) => {
        if (sortBit === 1) {
            return item >= arr.length / 2 ? 1 : 0;
        }
    return item < arr.length / 2 ? 1 : 0;
    };

    if (counter === 0 || counter % 2 === 0) {
        arr.forEach((item) => {
            if (parseInt(item\[reducerIndex\]) === 1) oneCount++;
        });
        counter++;
        return bitsReducer(arr, sortBit, createKeepBit(oneCount));
    }

    arr.forEach((item) => {
        const curBit = parseInt(item\[reducerIndex\]);
        if (keepBit === curBit) {
            tempArr.push(item);
        }
    });
    counter++;
    reducerIndex++;
    return bitsReducer(tempArr, sortBit);
};

const oxygenRating = bitsReducer(bits, 1);
const co2Rating = bitsReducer(bits, 0);
console.log("Oxygen Rating:", oxygenRating);
console.log("CO2 Rating:", co2Rating);
console.log("Life Support Rating:", oxygenRating \* co2Rating);