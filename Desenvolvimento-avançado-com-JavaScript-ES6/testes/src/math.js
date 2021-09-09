class Math {
    sum(...numbers) {
        return numbers.reduce((previousValue, currentValue) => {
            return previousValue + currentValue;
        });
    }
    mult(...numbers) {
        return numbers.reduce((previousValue, currentValue) => {
            return previousValue * currentValue;
        });
    }
}

module.exports = Math;