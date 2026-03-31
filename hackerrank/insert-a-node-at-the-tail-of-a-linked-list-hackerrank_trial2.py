def insertNodeAtTail(head, data):
    dummy = SinglyLinkedListNode(data)
    if not head:
        return dummy
        
    cur = head
    while cur.next:
        cur = cur.next
    
    cur.next = dummy
    return head
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head, '\n', fptr)
    fptr.write('\n')

    fptr.close()