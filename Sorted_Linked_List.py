'''
Sorted Linked List

EN
বাং
Problem Statement
You are given 
N
N integers. Create a singly linked list with these integers sequentially.

A singly linked list is a linear data structure in which the elements are not stored in contiguous memory locations and each element is connected only to its next element using a pointer.
Now, suppose you don't have any infomation, you only have the head pointer of the linked list. You don't even know the size of the linked list. Your task is to determine if the linked list is in non-decreasing order or not.

A linked list is in non-decreasing order if the elementss are greater than, or equal to the previous element. For example, if the given linked list is 
1
1 -> 
3
3 -> 
3
3 -> 
6
6 -> 
7
7 then it's in non-decreasing order and 
1
1 -> 
4
4 -> 
3
3 this linked list is not.

Input
First line of the input contains an integer 
N
N, number of integers.
Next line contains 
N
N space separated integers, the values of the linked list in order.

Output
Print "YES" if the linked list is in non-decreasing order, "NO" otherwise.

Constraints
1
1 
≤
≤ 
N
N 
≤
≤ 
10000
10000
All the provided integers are in range 
[
1
,
10000
]
[1,10000]
Example 1:
Input:
5
1 3 3 6 7
Output:
YES
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create linked list from array
def create_linked_list(arr):
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        current.next = Node(val)
        current = current.next
    return head

# Function to check if list is sorted (non-decreasing)
def is_sorted(head):
    current = head
    while current and current.next:
        if current.data > current.next.data:  # check decreasing order
            return False
        current = current.next
    return True

# Driver code
if __name__ == "__main__":
    N = int(input().strip())
    arr = list(map(int, input().split()))

    head = create_linked_list(arr)
    if is_sorted(head):
        print("YES")
    else:
        print("NO")
