/*
Question 1

Your task is to make a function that can take any non-negative
integer as an argument and return it with its digits in descending 
order. Essentially, rearrange the digits to create the highest possible number.
*/
function descendingOrder(n){
  return Number(String(n).split("").sort().reverse().join(""))
}

/* 
Question 2
Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.

Numerical Score	Letter Grade
90 <= score <= 100	'A'
80 <= score < 90	'B'
70 <= score < 80	'C'
60 <= score < 70	'D'
0 <= score < 60	'F'
*/
function getGrade (s1, s2, s3) {
  let avg = (s1 + s2 + s3) / 3
  avg = Math.floor(avg)
  console.log(avg)
  if (90 <= avg){
    return "A"
  } else if (80 <= avg){
    return "B"
  } else if (70 <= avg){
    return "C"
  } else if (60 <= avg){
    return "D"
  } else if (0 <= avg){
    return "F"
  }
}

/* 
Question 3
Your classmates asked you to copy some paperwork for them. 
You know that there are 'n' classmates and the paperwork has 'm' pages.

Your task is to calculate how many blank pages do you need. If n < 0 or m < 0 return 0.
*/
function paperwork(n, m) {
  if (n <= 0 || m <= 0){
    return 0
  } else {
    return n * m
  }
}
