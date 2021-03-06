# Sorting Algorithms Implementation

### Inversion

- Inversion Count for an array indicates – how far (or close) 
the array is from being sorted. If array is already sorted 
then inversion count is 0. If array is sorted in reverse 
order that inversion count is the maximum. 


##### Algorithm
###### geeksforgeeks explanation

 - The idea is similar to merge sort, divide the array into two equal or almost equal halves in each step until the base case is reached.
 
 - Create a function merge that counts the number of 
 inversions when two halves of the array are merged, create
  two indices i and j, i is the index for first half and j is
   an index of the second half. if a[i] is greater than a[j], 
   then there are (mid – i) inversions. because left and right
    subarrays are sorted, 
    so all the remaining elements in 
    left-subarray (a[i+1], a[i+2] … a[mid]) will be
     greater than a[j].
     
 - Create a recursive function to divide the array into halves
  and find the answer by summing the number of inversions is
   the first half, number of inversion in the second half and 
   the number of inversions by merging the two.
   
 - The base case of recursion is when there is only one 
 element in the given half.

### Complexity Analysis:
  Time Complexity:
   - Runtime of subroutine: O(n) + O(n) = O(n)
   - Merge runtime O(nlog(n)) 
   
### Status 
    - Done ( check screenshot below and inversionmain.py file )
    - Finding different solution for Inversion counting with best time complextity
    link: https://www.geeksforgeeks.org/counting-inversions/

#### My Code after some edits

<a href="https://ibb.co/30gS9Wv"><img src="https://i.ibb.co/p3Y4BZQ/Screen-Shot-2020-08-12-at-6-27-21-PM.png" alt="Screen-Shot-2020-08-12-at-6-27-21-PM" border="0"></a>
#### My Code 
- Less inversions 

<a href="https://ibb.co/s31SZCk"><img src="https://i.ibb.co/PCWpdM3/Screen-Shot-2020-08-06-at-7-08-05-PM.png" alt="Screen-Shot-2020-08-06-at-7-08-05-PM" border="0"></a>
#### GeeksForGeeks Code
<a href="https://ibb.co/Wcv3kTq"><img src="https://i.ibb.co/NL2394Q/Screen-Shot-2020-08-06-at-7-08-42-PM.png" alt="Screen-Shot-2020-08-06-at-7-08-42-PM" border="0"></a>
      