class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data):
        if self.head:
            new_node = self.Node(data)
            new_node.next = self.head

            self.head.prev = new_node
            self.head = new_node
        else:
            self.head = self.tail = self.Node(data)

    def reverse(self):
        curr = self.head

        while curr:
            nxt = curr.next
            curr.swap_pointer()
            curr = nxt
        temp = self.head
        self.head = self.tail
        self.tail = temp

    def print_list(self):
        temp = self.head

        while temp:
            if temp.prev and temp.next:
                print(f"{temp.prev.data}<--|{temp.data}|-->{temp.next.data}")
            elif temp.prev:
                print(f"{temp.prev.data}<--|{temp.data}|-->None")
            elif temp.next:
                print(f"None<--|{temp.data}|-->{temp.next.data}")
            else:
                print(f"{temp.prev}<--|{temp.data}|-->{temp.next}")
            temp = temp.next

    class Node:
        def __init__(self, data):
            self.prev = None
            self.data = data
            self.next = None

        def swap_pointer(self):
            temp = self.prev
            self.prev = self.next
            self.next = temp


def main():
    doubly_linked_list = DoublyLinkedList()

    print("Push item to list")
    r = 10
    for i in range(r):
        doubly_linked_list.push(i)
    doubly_linked_list.print_list()
    print()
    doubly_linked_list.reverse()
    doubly_linked_list.print_list()



if __name__ == "__main__":
    main()
