
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

    def detect_and_remove_loop(self):
        """
        Using slow and fast pointer we are detecting whether there is any loop
        in linked list
        """
        slow = self.head
        fast = self.head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                self.remove_loop(slow)
                return 1
        return 0

    def remove_loop(self, loop_node):

        node1 = self.head
        node2 = loop_node
        counter = 1

        while node1.next != node2:
            node1 = node1.next
            counter += 1

        node1 = self.head
        node2 = self.head

        for i in range(counter):
            node2 = node2.next

        while node1.next != node2.next:
            node1 = node1.next
            node2 = node2.next

        node2.next = None


    def print_list(self):
        temp = self.head
        print(f"head - {self.head}")
        print(f"tail - {self.tail}")
        k = 1

        while temp:
            print(f"[{temp.data}|*]", end="-->")
            temp = temp.next
            if k == 10:
                break
            k += 1
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
    linked_list.tail.next = linked_list.head.next
    linked_list.print_list()

    linked_list.detect_and_remove_loop()
    linked_list.print_list()


if __name__ == "__main__":
    main()