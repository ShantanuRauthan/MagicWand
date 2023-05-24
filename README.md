# MagicWand
Python solution to Techgladiators "Magic Wand" Problem


**Explanation:**

Sample Input
_5 3

1 2 3 4 5

5 2 1_

Where **5**(N in main.py) is the length of the first array and **3**(M in main.py) is the length of the queries array

1 2 3 4 5 are the 5 elements entered for first array (arr in main.py)

5 2 1 are the 3 elements entered for the 2nd array (queries in main.py)

Output
_10 7 10_  (cost[] in main.py)

Now
Take the first element of the queries array which is **5** in our case , now we have to add/subsctract some number from all the elements of **arr** array so that it comes down to **5**.

1+4 = 5

2+3 = 5

3+2 = 5 

4+1 = 5

5+0 = 5  (Exclude this one since no operation is needed in this case)

So our first output which is **10** is the addition of all the numbers (4+3+2+1), We are appending this value to the list **cost** (in main.py), do the same process for other elements of **queries** array and at the end append the output and print it (cost[]).
