class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def delete(self, data):
        curr = self.head

        while curr:
            if curr.data == data:
                if not curr.next:
                    self.tail = curr.prev
                    curr.prev.next = None
                    curr.prev = None

                elif not curr.prev:
                    self.head = curr.next
                    curr.next.prev = None
                    curr.next = None

                else:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                    curr.next = None
                    curr.prev = None
                del curr
                return
            curr = curr.next

    def insert(self, data, insert_after):
        if self.head:
            if insert_after == self.tail.data:
                self.append(data)
                return
            temp = self.head
            while temp.next:
                if temp.data == insert_after:
                    new_node = self.Node(data)
                    new_node.prev = temp
                    new_node.next = temp.next

                    temp.next.prev = new_node
                    temp.next = new_node

                temp = temp.next

        else:
            self.push(data)


    def push(self, data):
        if self.head:
            new_node = self.Node(data)
            new_node.next = self.head

            self.head.prev = new_node
            self.head = new_node
        else:
            self.head = self.tail = self.Node(data)

    def append(self, data):
        if self.head and self.tail:
            new_node = self.Node(data)
            new_node.prev = self.tail
            self.tail.next = new_node

            self.tail = self.tail.next
        else:
            self.push(data)

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

def main():
    doubly_linked_list = DoublyLinkedList()

    print("Push item to list")
    r = 9
    for i in range(r):
        doubly_linked_list.push(i)
    doubly_linked_list.print_list()

    print()
    print("Append item to tail")
    doubly_linked_list.append(-1)
    doubly_linked_list.print_list()

    print()
    print("inserting node in list")
    doubly_linked_list.insert(-2, 3)
    doubly_linked_list.print_list()
    print()

    print("deleting tail node in list")
    doubly_linked_list.delete(0)
    doubly_linked_list.print_list()
    print()

    print("deleting head node in list")
    doubly_linked_list.delete(8)
    doubly_linked_list.print_list()
    print()

    print("deleting node from mid of list")
    doubly_linked_list.delete(-2)
    doubly_linked_list.print_list()
    print()





if __name__ == "__main__":
    main()
