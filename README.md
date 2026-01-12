# Assessment2_Q1_COMP1010
Problem:
You are given the following program specifications:
Input: A four-digit positive integer with at least two different digits (leading zeros are allowed).
For example, 11 (it is considered 0011), 104 (it is considered 0104), 0011 (0 and 1 are two different digits), and 1234 (all four are different) are allowed, but 1111 is not allowed.
Program Body:
* If the input is not four digits, add the leading 0s
* Validate the four digit number by checking for at least two different digits in the number.
  Prompt the user for another number if it is invalid.
* Set N to be the input
* Main Loop: Repeat the following until N no longer changes
  Create two new four-digit numbers by arranging the digits of N in (a) ascending, and (b) descending order.
  Set N to be the difference between the larger number and the smaller number.
* Print out: The end result and the number of iterations of the Main Loop.

Part 2:
In a separate Python program, implement code which finds (and prints out) the maximum number of Main Loop iterations taken by any valid integer, by running the given program specification for all valid integers from 1 to 9998.

Got full marks for this task
