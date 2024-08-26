function sumEvenNumbers(upperLimit) {
    let sum = 0;
    for (let i = 0; i <= upperLimit; i++) {
        if (i % 2 === 0) { // მოიძიოს ლუწი რიცხვის არსებობა
            sum += i;
        }
    }
    return sum;
}

// ფუნქციის გამოტყუება სხვადასხვა მნიშვნელობებით
console.log(sumEvenNumbers(10)); // 0 + 2 + 4 + 6 + 8 + 10 = 30
console.log(sumEvenNumbers(20)); // 0 + 2 + 4 + 6 + 8 + 10 + 12 + 14 + 16 + 18 + 20 = 110
