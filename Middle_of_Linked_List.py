'''
Middle of Linked List

EN
বাং
Problem Statement
You are given 
N
N integers. Create a singly linked list with these integers sequentially.

A singly linked list is a linear data structure in which the elements are not stored in contiguous memory locations and each element is connected only to its next element using a pointer.
Now, suppose you don't have any infomation, you only have the head pointer of the linked list. You don't even know the size of the linked list. Your task is to find the middle element of the linked list using only the limited information you have.

For example, if the given linked list is 
1
1 -> 
2
2 -> 
3
3 -> 
4
4 -> 
5
5 then the output should be 
3
3.

If there are even number of element, then there would be two elements, we need to print the second middle element. If the given linked list is 
1
1 -> 
2
2 -> 
3
3 -> 
4
4 -> 
5
5 -> 
6
6 then the output should be 
4
4.

Input
First line of the input contains an integer 
N
N, number of integers.
Next line contains 
N
N space separated integers.

Output
Print an integer, the value of the middle element of the linked list.

Constraints
1
1 
≤
≤ 
N
N 
≤
≤ 
1000
1000
All the provided integers are in range 
[
1
,
1000
]
[1,1000]
Example 1:
Input:
5
1 2 3 4 5
Output:
3
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create linked list
def create_linked_list(arr):
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        current.next = Node(val)
        current = current.next
    return head

# Find middle using slow & fast pointer
def find_middle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data

# Driver code
if __name__ == "__main__":
    N = int(input().strip())
    arr = list(map(int, input().split()))

    head = create_linked_list(arr)
    print(find_middle(head))

