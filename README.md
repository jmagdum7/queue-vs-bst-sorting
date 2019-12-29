# queue-vs-bst-sorting
This mini-project has been completed as part of a Data Structures course objective. 
Through this project, we aim to use Queue and Binary Search Tree data structures to understand two different approaches to sorting.  
We analyze the working of both of these operations and also detail the time, space complexity and their performance in a variety of test cases.

Explanation:

1. The main method calls in a random data set method that generates data.
2. The main file calls the dedicated sort methods with the input as the random data set.
3. Once both the data sets are sorted, we record their running time in a list.
4. Using the time list and the data set size, we plot different graphs for experimental analysis.

For more detailed explanations and involved concepts, please read the Project Report.pdf

How to Run:

1. Open the folder in terminal.
2. Type the command : python main.py

Analysis:

A) Time Complexity:

1. After observation of the tree_time and queue_time lists, it is evident that sorting using a binary search tree is much faster as compared to that using a queue.
2. This is because the average time complexity for tree sort is O(n logn) as compared to O(n) for queue sort, where ‘n’ is the number of elements in the input.

B) Space Complexity:

1. The space taken by tree sort however is more as compared to queue sort since queue sort performs the sorting operation in-place.
2. Hence, no extra memory is used for sorting using a queue i.e. O(1) space complexity.
3. Comparatively, tree sort inserts the elements of list as nodes in a tree and hence, the space taken up during tree sort is the number of nodes generated.
4. Hence, final space complexity for sorting using a binary search tree is O(n), where ‘n’ is the number of unique elements in the input.

