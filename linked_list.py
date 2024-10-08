class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next


class Solution:

    # 141. Linked List Cycle
    def hasCycle(self, head):

        fast = head
        slow = head

        if fast == None:
            return False

        while fast != None and fast.next != None:

            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False

    # 876. Middle of the Linked List
    def middleNode(self, head):


        '''
        Naive solution

        iterator = head
        solution = head
        if iterator == None:
            return

        count = 0
        while iterator != None:
            count += 1
            iterator = iterator.next

        middle = int(count / 2)
        index = 0

        while index < middle:
            solution = solution.next
            index += 1

        return solution
        '''


        # two pointer solution
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

    # 142. Linked List Cycle II
    def detectCycle(self, head):

        fast = head

        if fast is None:
            return None

        table_hash = {}
        while fast is not None:

            key = (fast, fast.val)

            if key not in table_hash:
                table_hash[key] = True
            else:
                return fast

            fast = fast.next

        return None

    # 234. Palindrome Linked List
    def isPalindrome(self, head):

        stack = []
        aux = head
        iterator = head

        while iterator is not None:
            stack.append(iterator.val)
            iterator = iterator.next

        print(stack)
        while stack and aux is not None:
            value = stack.pop()
            if value != aux.val:
                return False
            aux = aux.next
        return True

    # 206. Reverse Linked List
    def reverseList(self, head):

        current = head
        previous = None

        while current is not None:
            aux = current.next # save current next pointer
            current.next = previous # point to previous
            previous = current # previous move to current
            current = aux # current move to next

        head = previous
        return head

    # 92. Reverse Linked List II
    def reverseSubList(self, head, left, right):

        startSub = head
        prevSub = None

        while startSub != None and startSub.val != left:
            prevSub = startSub
            startSub = startSub.next

        if startSub is not None:
            endSub = startSub # save the last previous Node before to reverse
            iterator = startSub # an iterator to reverse the list
        else:
            return head

        prev = None
        while iterator != None and iterator.val != right:
            aux = iterator.next
            iterator.next = prev
            prev = iterator
            iterator = aux

        secondPart = iterator.next
        iterator.next = prev
        endSub.next = secondPart

        if prevSub is not None:
            prevSub.next = iterator
        else:
            head = iterator

        while head is not None:
            print({head.val})
            head = head.next

        return head

    def reversing(self, head, tail):

        previous = None
        while head != tail:

            aux = head.next
            head.next = previous
            previous = head
            head = aux

        return previous


if __name__ == '__main__':
    head = Node(100)
    head.next = Node(200)
    head.next.next = Node(300)
    head.next.next.next = Node(400)
    head.next.next.next.next = Node(500)
    head.next.next.next.next.next = Node(600)
    # 1 -> 12 - > 103 - > 1004 -> 10005 -> 100006

    solution = Solution()
    result = solution.reverseSubList(head, 2, 5)

    while result is not None:
        print(f"{result.val}")
        result = result.next
