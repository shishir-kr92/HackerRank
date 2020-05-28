
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

    def rotate(self, k):
        temp = self.head
        count = 1

        while temp:
            if count == k:
                self.tail.next = self.head
                self.head = temp.next
                temp.next = None
                return
            count += 1
            temp = temp.next

    def print_list(self):
        temp = self.head
        # print(f"head - {self.head}")
        # print(f"tail - {self.tail}")

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
    for i in range(1, 11):
        linked_list.push(i)
    linked_list.print_list()
    linked_list.rotate(9)
    linked_list.print_list()


if  __name__ == "__main__":
    main()