'''
Problem Statement
You are given 
N
N integers. Create a singly linked list with these integers sequentially.

A singly linked list is a linear data structure in which the elements are not stored in contiguous memory locations and each element is connected only to its next element using a pointer.
Now, suppose you don't have any infomation, you only have the head pointer of the linked list. You don't even know the size of the linked list. Your task is reverse the linked list and print the values of the reversed linked list.

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
5 then the after reversing the linked list should be 
5
5 -> 
4
4 -> 
3
3 -> 
2
2 -> 
1
1.

Input
First line of the input contains an integer 
N
N, number of integers.
Next line contains 
N
N space separated integers, the values of the linked list in order.

Output
Print 
N
N integers, the values of the reversed linked list in order.

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
1000
]
[1,1000]
Example 1:
Input:
5
1 2 3 4 5
Output:
5 4 3 2 1
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

# Reverse linked list
def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev  # new head

# Print linked list
def print_linked_list(head):
    current = head
    result = []
    while current:
        result.append(str(current.data))
        current = current.next
    print(" ".join(result))

# Driver code
if __name__ == "__main__":
    N = int(input().strip())
    arr = list(map(int, input().split()))

    head = create_linked_list(arr)
    new_head = reverse_linked_list(head)
    print_linked_list(new_head)

