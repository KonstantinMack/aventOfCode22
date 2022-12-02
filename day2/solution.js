const fs = require("fs");

let data = fs.readFileSync("input.txt", "utf8");
data = data.split("\n").filter((item) => item);

// Question 1:

scoreDict = {
  X: {
    A: 3,
    B: 0,
    C: 6,
  },
  Y: {
    A: 6,
    B: 3,
    C: 0,
  },
  Z: {
    A: 0,
    B: 6,
    C: 3,
  },
};

pointsDict = {
  X: 1,
  Y: 2,
  Z: 3,
};

const solution1 = data
  .map((game) => {
    const [opp, player] = game.split(" ");
    return scoreDict[player][opp] + pointsDict[player];
  })
  .reduce((acc, cur) => acc + cur, 0);

console.log("Solution 1: ", solution1);

// Question 2:

playDict = {
  X: {
    A: "Z",
    B: "X",
    C: "Y",
  },
  Y: {
    A: "X",
    B: "Y",
    C: "Z",
  },
  Z: {
    A: "Y",
    B: "Z",
    C: "X",
  },
};

scoreDict = {
  X: 0,
  Y: 3,
  Z: 6,
};

const solution2 = data
  .map((game) => {
    const [opp, result] = game.split(" ");
    return scoreDict[result] + pointsDict[playDict[result][opp]];
  })
  .reduce((agg, cur) => agg + cur, 0);

console.log("Question 2: ", solution2);
