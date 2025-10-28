class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def delete_dupes(head):
    if not head:
        return None
    freq = {}
    current = head

    while current:
        freq[current.value] = freq.get(current.value, 0) + 1
        current = current.next

    dummy = Node(0)
    tail = dummy
    current = head

    while current:
        if freq[current.value] == 1:
            tail.next = Node(current.value)
            tail = tail.next
        current = current.next

    return dummy.next

head = Node(1, Node(2, Node(3, Node(3, Node(4, Node(5))))))

# Linked List: 1 -> 2 -> 3 -> 3 -> 4 -> 5
print_linked_list(delete_dupes(head))