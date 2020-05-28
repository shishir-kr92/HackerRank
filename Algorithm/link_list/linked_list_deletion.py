

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.counter = 0

    def delete(self, pos):

        if not self.head:
            return

        temp = self.head
        index = 0

        # deleting head
        if pos - 1 == 0:
            self.head = temp.next
            temp.next = None
            self.counter -= 1
            del temp
            return


        while temp and index <= self.counter:
            if index == pos - 2:
                temp.next = temp.next.next
                self.counter -= 1
                return
            temp = temp.next
            print(temp, temp.data)
            index += 1


    def append(self, data):
        if self.tail:
            self.tail.next = self.Node(data)
            self.tail = self.tail.next
        else:
            self.head = self.tail = self.Node(data)
        self.counter += 1

    def print_list(self):
        print(f"No of element in linked list : {self.counter}")
        if self.head:
            temp = self.head
            while temp:
                print(f"[{temp.data}|*]", end="-->")
                temp = temp.next
            print("None")


    class Node:
        def __init__(self, data, next_node=None):
            self.data = data
            self.next = next_node


def main():
    linked_list = LinkedList()
    for i in range(10):
        linked_list.append(i)
    linked_list.print_list()
    print()
    print(f"deleting entry at index 1")
    linked_list.delete(2)
    linked_list.print_list()



if __name__ == "__main__":
    main()
