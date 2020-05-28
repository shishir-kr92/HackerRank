
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



    class Node:
        def __init__(self, data, next_node=None):
            self.data = data
            self.next = next_node


def merge_sorted_list( l1, l2):
    final_list = LinkedList()
    final_list.push(None)
    
    x = l1.head
    y = l2.head

    while x and y:
        if x.data > y.data:
            final_list.push(y.data)
            y = y.next
        else:
            final_list.push(x.data)
            x = x.next


    while x:
        final_list.push(x.data)
        x = x.next
    while y:
        final_list.push(y.data)
        y = y.next
    temp = final_list.head
    final_list.head = final_list.head.next
    temp.next = None
    del temp
    return final_list


def main():
    l1 = LinkedList()
    for i in range(1, 8, 2):
        l1.push(i)
    l1.print_list()

    l2 = LinkedList()
    for i in range(2, 8, 2):
        l2.push(i)
    l2.print_list()
    merge_sorted_list(l1, l2).print_list()




if __name__ == "__main__":
    main()