
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

    def print_list(self):
        temp = self.head
        print(f"head - {self.head}")
        print(f"tail - {self.tail}")

        while temp:
            print(f"[{temp.data}|*]", end="-->")
            temp = temp.next
        print("None")
        print()

    def swap_nodes(self, x, y):
        
        # x and y may or may not be adjacent

        # either x or y be the head node

        # either x or y be the tail node

        # either x or y may or may not be present in a list

        # x and y both are same
        if x == y:
            return

        prevX = None
        curX = self.head

        while curX and curX.data != x:
            prevX = curX
            curX = curX.next

        prevY = None
        curY = self.head

        while curY and curY.data != y:
            prevY = curY
            curY = curY.next

        # either x or y is nor present in list
        if not curX or not curY:
            return

        if prevX:
            prevX.next = curY
        else:
            self.head = curY

            if not curY.next:
                self.tail = curX

        if prevY:
            prevY.next = curX
        else:
            self.head = curX
            if not curX.next:
                self.tail = curX

        # swap current X and Y pointer
        temp = curX.next
        curX.next = curY.next
        curY.next = temp


    class Node:
        def __init__(self, data, next_node=None):
            self.data = data
            self.next = next_node


def main():
    linked_list = LinkedList()
    for i in range(10):
        linked_list.push(i)
    linked_list.print_list()

    linked_list.swap_nodes(-1, 6)
    linked_list.print_list()


if __name__ == "__main__":
    main()