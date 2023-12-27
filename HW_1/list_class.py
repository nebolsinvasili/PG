class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        self.head = Node(value, self.head)
    

    def insert(self, index, value):
        if self.head is None:
            self.head = Node(value, None)
        elif index == 0:
            self.add(value)
        else:
            current = self.head
            while current.next is not None and index > 1:
                current = current.next
                index = index - 1

            current.next = Node(value, current.next)


    def contains(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False


    def length(self):
        result = 0
        current = self.head

        while current is not None:
            result += 1
            current = current.next

        return result


    def remove(self):
        if self.head is None:
            return None

        value = self.head.value
        self.head = self.head.next

        return value


    def remove_at(self, index):
        if self.head is None:
            return None

        elif index == 0 or self.head.next is None:
            return self.remove()

        else:
            current = self.head
            while current.next.next is not None and index > 1:
                current = current.next
                index -= 1

            value = current.value
            current.next = current.next.next

            return value
    

    def show_list(self):     
        l = ''   
        current = self.head
        while current is not None:
            l = l + str(current.value) + ' '
            current = current.next
        else:
            print(f'[{l.strip()}]')


if __name__ == '__main__':
    test_list = LinkedList()
    test_list.add(1)
    test_list.add(2)
    test_list.show_list()