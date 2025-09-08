'''
K-th elemnt from end

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
Now, suppose you don't have any infomation, you only have the head pointer of the linked list. You don't even know the size of the linked list. Your task is to delete 
K
K-th element from the end of linked list.

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
2
2 then after deleting the linked list will be 
1
1 -> 
2
2 -> 
3
3 -> 
5
5

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
Print the elements of linked list after deleting 
K
K-th element from the end.

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
1 2 3 5
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to create linked list from array
def create_linked_list(arr):
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        current.next = Node(val)
        current = current.next
    return head

# Function to delete K-th node from end
def delete_kth_from_end(head, K):
    dummy = Node(0)       # dummy node before head
    dummy.next = head
    first = dummy
    second = dummy

    # Move first pointer K+1 steps ahead
    for _ in range(K + 1):
        first = first.next

    # Move both until first reaches end
    while first:
        first = first.next
        second = second.next

    # Delete K-th node from end
    second.next = second.next.next

    return dummy.next

# Function to print linked list
def print_linked_list(head):
    current = head
    result = []
    while current:
        result.append(str(current.data))
        current = current.next
    print(" ".join(result))

# Driver code
if __name__ == "__main__":
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    head = create_linked_list(arr)
    new_head = delete_kth_from_end(head, K)
    print_linked_list(new_head)
