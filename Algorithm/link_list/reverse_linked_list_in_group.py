
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def push(self, data):
        if self.tail:
            temp = self.Node(data)
            self.tail.next = temp
            self.tail = temp
        else:
            self.head = self.tail = self.Node(data)

    def reverse(self, k):
        start = self.head
        node = self.head

        while node != self.tail:
            if 


    def print_list(self):
        temp = self.head
        print(f"head - {self.head}")
        print(f"tail - {self.tail}")

        while temp:
            print(f"[{temp.data}|*]", end="-->")
            temp = temp.next
        print("None")
        print()


    class Node:
        def __init__(self, data, next_node=None):
            self.data = data
            self.next = next_node


def main():
    linked_list = LinkedList()
    for i in range(5):
        linked_list.push(i)
    linked_list.print_list()

    linked_list.reverse()
    linked_list.print_list()


if __name__ == "__main__":
    main()