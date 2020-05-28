class LinkList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, num):
        if self.tail:
            new_node = self.Node(num)
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.tail = self.head = self.Node(num)

    def print_list(self):
        temp = self.head
        while temp:
            # print(f"[{temp.get_data()}|*]", end="-->")
            print(f"[{temp.data}|*]", end="-->")
            temp = temp.next
        print(None)

    class Node:
        def __init__(self, num):
            self.data = num
            self.next = None


def main():
    link_list = LinkList()

    for i in range(10):
        link_list.add_node(i)

    link_list.print_list()


if __name__ == "__main__":
    main()
