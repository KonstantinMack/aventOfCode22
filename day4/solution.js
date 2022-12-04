const fs = require("fs");

let data = fs.readFileSync("input.txt", "utf8");
data = data.split("\n").filter((item) => item);

// Question 1:

const solution1 = data.reduce((agg, curr) => {
  const [elf1, elf2] = curr.split(",");
  const [elf1Start, elf1End] = elf1.split("-").map((x) => Number(x));
  const [elf2Start, elf2End] = elf2.split("-").map((x) => Number(x));
  if (elf1Start <= elf2Start && elf1End >= elf2End) return agg + 1;
  if (elf2Start <= elf1Start && elf2End >= elf1End) return agg + 1;
  return agg;
}, 0);

console.log("Question 1: ", solution1);

// Question 2:

const solution2 = data.reduce((agg, curr) => {
  const [elf1, elf2] = curr.split(",");
  const [elf1Start, elf1End] = elf1.split("-").map((x) => Number(x));
  const [elf2Start, elf2End] = elf2.split("-").map((x) => Number(x));
  if (elf1Start <= elf2Start && elf1End >= elf2Start) return agg + 1;
  if (elf2Start <= elf1Start && elf2End >= elf1Start) return agg + 1;
  return agg;
}, 0);

console.log("Question 2: ", solution2);
