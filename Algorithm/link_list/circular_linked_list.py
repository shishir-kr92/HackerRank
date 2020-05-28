
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

    def insert(self, data, insertAfter):
        if self.tail:
            if self.tail.data == insertAfter:
                self.append(data)
                return

            temp = self.tail

            while True:
                print(temp, temp.data)
                if temp.data == insertAfter:
                    break
                temp = temp.next
            temp.next = self.Node(data, next_node=temp.next)
        else:
            self.push(data)

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

    print()
    print("pushing -1 at head")
    circular_linked_list.push(-1)
    circular_linked_list.print_node() 

    print()
    print("appending new element at tail")
    circular_linked_list.append(10)
    circular_linked_list.print_node()

    print()
    print("inserting new element after 10")
    circular_linked_list.insert(11, 10)
    circular_linked_list.print_node()


if __name__ == "__main__":
    main()
