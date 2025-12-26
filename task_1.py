class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def reverse_list(self):
        previous = None
        current = self.head

        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            
            current = next
        self.head = previous
      
    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


def merge_sort(l_node):
    if not l_node or not l_node.next:
        return l_node

    slow = l_node
    fast = l_node
    prev = None
    
    # Поки швидкий вказівник може зробити два кроки
    while fast is not None and fast.next is not None:
        prev = slow
        slow = slow.next          # один крок
        fast = fast.next.next     # два кроки
    
    if prev:
        prev.next = None
        
    left_part = l_node
    right_part = slow # тут slow вказує на середину
    
    return merger(merge_sort(left_part), merge_sort(right_part))

def merger(left, right):
    # Створюємо фіктивний вузол (dummy), щоб почати новий список
    dummy = Node(0)
    current = dummy

    cur_left = left
    cur_right = right
    # Спочатку об'єднайте менші елементи
    while cur_left is not None and cur_right is not None:
        if cur_left.data <= cur_right.data:
            current.next = cur_left
            cur_left = cur_left.next
            
        else:
            current.next = cur_right
            cur_right = cur_right.next
        
        current = current.next
        
    if cur_left is not None:
        current.next = cur_left
    elif cur_right is not None:
        current.next = cur_right
        
    return dummy.next

def merge_two_lists(first_list, second_list):
    # Створюємо новий ліст:
    merged_list = LinkedList()
    # Отримуємо першу ноду у відсортованому лісті злиттям
    merged_list_head = merger(first_list.head, second_list.head)
    merged_list.head = merged_list_head
    
    return merged_list


if __name__ == "__main__":
    llist_1 = LinkedList()
    llist_2 = LinkedList()

    # Вставляємо вузли в початок
    llist_1.insert_at_beginning(5)
    llist_1.insert_at_beginning(10)
    llist_1.insert_at_beginning(15)

    # Вставляємо вузли в кінець
    llist_1.insert_at_end(20)
    llist_1.insert_at_end(25)

    llist_2.insert_at_beginning(3)
    llist_2.insert_at_beginning(8)
    llist_2.insert_at_beginning(11)
    llist_2.insert_at_beginning(4)
    llist_2.insert_at_beginning(60)
    llist_2.insert_at_beginning(18)

    # Друк зв'язного списку
    print("Зв'язний список 1:")
    llist_1.print_list()
    print("Зв'язний список 2:")
    llist_2.print_list()

    print("******************** REVERSE *****************")
    llist_1.reverse_list()
    llist_1.print_list()

    print("********************* MERGE SORT 1 ******************")
    llist_1.head = merge_sort(llist_1.head)
    llist_1.print_list()
    print("********************* MERGE SORT 2 ******************")
    llist_2.head = merge_sort(llist_2.head)
    llist_2.print_list()

    print("******************** MERGE 2 LISTS *****************")
    llist_3 = merge_two_lists(llist_1, llist_2)
    llist_3.print_list()

    print("******************** REVERSE *****************")
    llist_3.reverse_list()
    llist_3.print_list()
