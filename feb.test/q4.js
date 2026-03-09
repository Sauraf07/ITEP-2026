// Write a JavaScript program to find the occurrence of each element in:
let arr = [1, 2, 2, 3, 1];

let count = {};

for (let i = 0; i < arr.length; i++) {
  let element = arr[i];
  
  if (count[element]) {
    count[element]++;
  } else {
    count[element] = 1;
  }
}

console.log("the numbers of times it occurs: ",count);
