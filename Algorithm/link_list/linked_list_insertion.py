"""
Insertion Operation in linked list

Node can be added at 3 places
1. At head
2. At Tail
3. After a given node
"""

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        if self.tail:
            self.tail.next = self.Node(data)
            self.tail = self.tail.next
        else:
            self.push(data)

    def push(self, data):
        if self.head:
            self.head = self.Node(data, self.head)

        else:
            self.head = self.tail = self.Node(data)

    def insert(self, data, pos):
        if self.head:
            temp = self.head
            counter = 1
            while temp:
                if counter == pos - 1:
                    temp.next = self.Node(data, temp.next)
                    break
                temp = temp.next
                counter += 1
        else:
            self.push(data)

    def print_list(self):
        temp = self.head
        while temp:
            print(f"[{temp.data}|*]", end="-->")
            temp = temp.next
        print(None)

    class Node:
        def __init__(self, data, next_node=None):
            self.data = data
            self.next = next_node

def main():
    linked_list = LinkedList()

    # insertion at tail
    print("****************************************************************************")
    print("creating list")
    for i in range(10):
        linked_list.append(i)
    linked_list.print_list()
    print("****************************************************************************")
    print("insertion at head")
    linked_list.push(-1)
    linked_list.print_list()
    print("****************************************************************************")
    print("insertion at tail")
    linked_list.append(10)
    linked_list.print_list()
    print("****************************************************************************")
    print("insertion at specific node")
    linked_list.insert(30, 4)
    linked_list.print_list()



if __name__ == "__main__":
    main()
