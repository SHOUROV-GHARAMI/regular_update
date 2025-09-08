'''
Rotate Linked List

EN
বাং
Problem Statement
You are given 
N
N integers and an integer 
K
K 
(
1
≤
K
≤
N
)
(1≤K≤N). Create a singly linked list with the 
N
N integers sequentially.

A singly linked list is a linear data structure in which the elements are not stored in contiguous memory locations and each element is connected only to its next element using a pointer.
Now, suppose you don't have any infomation, you only have the head pointer of the linked list. You don't even know the size of the linked list. Your task is to rotate the linked list 
K
K times counter-clockwise.

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
5 and 
K
K is 
3
3 then
after rotating 
1
s
t
1st time 
2
2 -> 
3
3 -> 
4
4 -> 
5
5 -> 
1
1
after rotating 
2
n
d
2nd time 
3
3 -> 
4
4 -> 
5
5 -> 
1
1 -> 
2
2
after rotating 
3
r
d
3rd time 
4
4 -> 
5
5 -> 
1
1 -> 
2
2 -> 
3
3

Input
First line of the input contains two integers 
N
N and 
K
K.
Next line contains 
N
N space separated integers, the values of the linked list in order.

Output
Print the elements of linked list after rotating 
K
K times counter-clockwise.

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
1
1 
≤
≤ 
K
K 
≤
≤ 
N
N
All the provided integers are in range 
[
1
,
10000
]
[1,10000]
Example 1:
Input:
5 2
1 2 3 4 5
Output:
3 4 5 1 2
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to create linked list
def create_linked_list(arr):
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        current.next = Node(val)
        current = current.next
    return head

# Function to rotate linked list K times counter-clockwise
def rotate_linked_list(head, K):
    if not head or K == 0:
        return head

    # Step 1: Find length and last node
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1

    # Step 2: Adjust K (in case K > length)
    K = K % length
    if K == 0:
        return head

    # Step 3: Traverse to the K-th node
    current = head
    for _ in range(K - 1):
        current = current.next

    # Step 4: Rearrange pointers
    new_head = current.next
    current.next = None
    tail.next = head

    return new_head

# Function to print linked list
def print_linked_list(head):
    current = head
    result = []
    while current:
        result.append(str(current.data))
        current = current.next
    print(" ".join(result))


# Driver Code
if __name__ == "__main__":
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    head = create_linked_list(arr)
    new_head = rotate_linked_list(head, K)
    print_linked_list(new_head)
