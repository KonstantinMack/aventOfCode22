const fs = require("fs");

let data = fs.readFileSync("input.txt", "utf8");
data = data.split("\n");

// Question 1: Elf carrying most calories
const elfCals = [];

let currentCals = 0;
for (const cal of data) {
  if (cal) {
    currentCals += Number(cal);
  } else {
    elfCals.push(currentCals);
    currentCals = 0;
  }
}

console.log("Question 1: ", Math.max(...elfCals));

//  Question 2: Top 3 elf calories combined

console.log(
  "Question 2: ",
  elfCals
    .sort((a, b) => b - a)
    .slice(0, 3)
    .reduce((prev, curr) => prev + curr, 0)
);
