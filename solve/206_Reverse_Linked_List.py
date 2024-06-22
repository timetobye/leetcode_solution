# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    """
    풀이는 이렇다.
    - prev(previous) / curr(current) 를 가리키는 객체(포인터, 파이썬이니까 객체)가 있다.
    - 연결 객체를 변경을 해줘야 한다.
    - 우선 연결 객체를 임시로 저장한다. next 라고 칭한다.
    - 그 다음에 curr.next = prev 로 연결 해준다. 가장 처음일 때는 None 상태일거고, 반복을 돌면서 다음 노드로 이동을 한 것을 가리킬 것이다.
    - None <- 1 <- 2 <- 3 <- 4 <- 5(new head)
    - prev = node 가 된다. 다음으로 이동을 시킨다.
    - node = next 값을 넣어준다.
    - 이게 무슨 말이냐면 기존에 None -> 1-> 2 -> 3 -> 4 -> 5 가 있다고 하면 prev 는 None 에 있었고, node 는 1에 있었을 것이다.
    - 서로 한 칸씩 이동을 해야 하니까 prev = node 가 되고, node 는 처음에 node.next 로 가리킨 객체로 이동을 할 것이다.
    - 이제 반복을 계속 하고 더 이상 이동을 할 곳이 없으면 while 문이 종료 되고, 역순으로 연결 리스트가 생성된 것을 리턴한다.
    """

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while node:
            next = node.next
            node.next = prev
            prev = node
            node = next

        return prev


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        new_head = head

        if head.next:
            new_head = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return new_head
