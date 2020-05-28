
class CircularLinkedList:
    def __init__(self):
        self.tail = None

    def push(self, data):
        if self.tail:
            new_node = self.Node(data, self.tail.next)
            self.tail.next = new_node
        else:
            self.tail = self.Node(data)
            self.tail.next = self.tail

    def append(self, data):
        if self.tail:
            self.tail.next = self.Node(data, next_node=self.tail.next)
            self.tail = self.tail.next
        else:
            self.push(data)

    def split_list(self):
        head1 = CircularLinkedList()
        head2 = CircularLinkedList()

        head = self.tail.next

        if head == None:
            return

        slow = head
        fast = head

        while fast.next.next != head and fast.next != head:
            slow = slow.next
            fast = fast.next.next

        if fast.next.next == head:
            fast = fast.next

        fast.next = slow.next
        slow.next = head

        head1.tail = slow
        head2.tail = fast

        return head1, head2

    def print_node(self):
        temp = self.tail

        while True:
            print(f"[{temp.data}|*]", end="-->")

            if temp.next is self.tail:
                break
            temp = temp.next
        print()

    class Node:
        def __init__(self, data, next_node=None):
            self.data = data
            self.next = next_node


def main():
    circular_linked_list = CircularLinkedList()
    for i in range(12):
        circular_linked_list.append(i)
    print("Original List")
    circular_linked_list.print_node()

    print()
    list1, list2 = circular_linked_list.split_list()
    list1.print_node()
    list2.print_node()


if __name__ == "__main__":
    main()
