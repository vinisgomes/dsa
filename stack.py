# LIFO - LAST IN FIRST OUT
class Stack:
    stack = []
    final_node = 0

    def __init__(self):
        self.stack = []

    # O(1)
    def push(self, element):
        self.stack.append(element)
        self.final_node += 1
    # O(1)
    def pop(self):
        self.stack.pop(self.final_node - 1)
        self.final_node -= 1
    
    def __str__(self):
        return f"{self.stack}"


def main():
    test = Stack()

    test.push(3)
    test.push(2)
    test.push(1)
    test.push(4)
    test.push(5)
    test.push(6)
    test.push(7)
    test.push(10)
    
    test.pop()
    test.pop()
    test.pop()

    print(test)

if __name__ == "__main__":
    main()
