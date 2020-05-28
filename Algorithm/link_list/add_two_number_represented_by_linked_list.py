
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


def find_sum(list1, list2):
    node1 = list1.head
    node2 = list2.head
    result_list = LinkedList()
    carry = 0

    while node1 or node2:
        print(node1, node2)
        t1 = node1.data if node1 else 0
        t2 = node2.data if node2 else 0

        sum = t1 + t2 +carry

        carry = 1 if sum >= 10 else 0

        sum = sum % 10 if sum >= 10 else sum

        result_list.push(sum)

        node1 = node1.next if node1 else None
        node2 = node2.next if node2 else None
        print((node1, node2))
    if carry > 0:
        result_list.push(carry)
    return result_list



def main():
    linked_list1 = LinkedList()
    linked_list2 = LinkedList()
    for i in [7, 5, 9, 4, 6]:
        linked_list1.push(i)
    linked_list1.print_list()

    for i in [8, 4]:
        linked_list2.push(i)
    linked_list2.print_list()

    result = find_sum(linked_list1, linked_list2)
    result.print_list()





if __name__ == "__main__":
    main()