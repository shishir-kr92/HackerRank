class Stack:
    def __init__(self):
        self.head = None
        self.count = 0

    def push(self, data):
        if self.head:
            temp = self.Node(data)
            temp.next = self.head
            self.head = temp
        else:
            self.head = self.Node(data)

    def pop(self):
        if self.head:
            temp = self.head
            self.head = temp.next
            temp.next = None
            return temp.data

    def top(self):
        return self.head

    def is_empty(self):
        if self.head:
            return False
        else:
            return True

    def print_stack(self):
        temp = self.head

        while temp:
            print(f"[{temp.data}|*]", end="-->")
            temp = temp.next
        print(None)

    class Node:
        def __init__(self, data):
            self.data = data
            self.next= None

def main():
    stack = Stack()
    for i in range(10):
        stack.push(i)
    stack.print_stack()

    print(f"Pop : {stack.pop()}")
    print(f"Pop : {stack.pop()}")
    print(f"Pop : {stack.pop()}")
    stack.print_stack()
    import os
    print(os.getenv("_SC_LEVEL1_DCACHE_LINESIZE"))


if __name__ == "__main__":
    main()