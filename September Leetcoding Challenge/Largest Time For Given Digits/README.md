# Largest Time for Given Digits

Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

Example 1:

	Input: A = [1,2,3,4]
	Output: "23:41"

Example 2:

	Input: A = [5,5,5,5]
	Output: ""

Example 3:

	Input: A = [0,0,0,0]
	Output: "00:00"

Example 4:

	Input: A = [0,0,1,0]
	Output: "10:00"
 

#### Constraints:

arr.length == 4
0 <= arr[i] <= 9
