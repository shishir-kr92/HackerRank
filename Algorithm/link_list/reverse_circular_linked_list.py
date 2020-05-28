
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

    def reverse(self):
        head = self.tail
        prev = self.tail
        curr = self.tail.next
        nxt = curr.next


        while curr != self.tail:
            curr.next = prev

            prev = curr
            curr = nxt
            nxt = nxt.next
    
        self.tail = curr.next
        curr.next = prev



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
    for i in range(10):
        circular_linked_list.append(i)
    print("Original List")
    circular_linked_list.print_node()
    circular_linked_list.reverse()
    circular_linked_list.print_node()


if __name__ == "__main__":
    main()
