
class Stack:
    def __init__(self):
        self.head = None
        self.count = 0

    def push(self, data):
        new_node = self.Node(data)
        new_node.next = self.head
        self.head = new_node
        self.count += 1

    def pop(self):
        if self.head:
            temp = self.head
            self.head, temp.next  = temp.next, None
            self.count -= 1
            return temp.data

    def print_stack(self):
        temp = self.head

        while temp:
            print(temp.data, end=",")
            temp = temp.next
        print()

    def is_empty(self):
        if self.count:
            return True
        return False

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

class Postfix:
    def __init__(self):
        self.stack = Stack()
        self.expression_precedence = {'+':1,
                                      '-':1,
                                      '*':2,
                                      '/':2,
                                      '%': 2,
                                      '//':2,
                                      '^':3
                                      }

    def is_operator(self, symbol):
        if symbol in self.expression_precedence:
            return True
        else:
            return False

    def is_greater(self, op1, op2):
        try:
            return True if self.expression_precedence[op1] > self.expression_precedence[op2] else False
        except KeyError:
            return False


    def postfix(self, expression):
        postfix_exp = list()
        bracket_opened = False
        for entry in expression:
            self.stack.print_stack()
            if entry == "(":
                bracket_opened = True
                self.stack.push(entry)

            elif bracket_opened and entry == ")":
                bracket_opened = False
                while self.stack.head and self.stack.head.data != "(":
                    postfix_exp.append(self.stack.pop())
                self.stack.pop()

            elif self.is_operator(entry):
                while self.stack.head and not bracket_opened and (not self.is_greater(entry, self.stack.head.data)):
                    postfix_exp.append(self.stack.pop())
                self.stack.push(entry)

            else:
                postfix_exp.append(entry)

        while self.stack.head:
            postfix_exp.append(self.stack.pop())

        return "".join(postfix_exp)

def main():
    exp = "a+b*c+d"
    result = Postfix().postfix(exp)
    print(result)

    print()
    exp = "a+(b-c)+d"
    result = Postfix().postfix(exp)
    print(result)

    print()
    exp = "a+b*(c^d-e)^(f+g*h)-i"
    result = Postfix().postfix(exp)
    print(result)

# abcde-^fgh*+^*+i-
# abcd^e-fgh*+^*+i-


if __name__ == "__main__":
    main()
