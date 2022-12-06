const fs = require("fs");

let data = fs.readFileSync("input.txt", "utf8");
const [signal] = data.split("\n").filter((item) => item);

const findSignal = (n) => {
  for (let i = n; i < signal.length; i++) {
    const subString = signal.slice(i - n, i);
    if ([...new Set(subString)].length === n) return i;
  }
};

console.log("Question 1: ", findSignal(4));
console.log("Question 2: ", findSignal(14));
