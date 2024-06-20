# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        # 더미 노드를 만들면 순서를 인식하기가 좋기 때문에 만든다.
        # dummy -> 1 -> 2 -> 3 -> 4 -> 5
        dummy = ListNode(0, head)  # dummy -> head(1)
        leftprev, curr = dummy, head

        # left 2, right 4 여서 끊어서 연결 리스트를 재구성해야 한다.
        # dummy -> 1 까지 우선 전진한다.
        for i in range(left - 1):
            leftprev = curr
            curr = curr.next

        # 여기 까지 왔을때 leftprev = node 1에 위치하고 있고, curr 은 node 2에 위치하고 있다.

        # 뒤집어야 하니까 뒤집는 방법을 사용한다.
        prev = None
        for i in range(right - left + 1):
            tmp_next = curr.next
            curr.next = prev

            # 포인터 이동
            prev = curr
            curr = tmp_next

        # 최종적으로 연결을 해주는 작업
        # 1 -> 4, 2 -> 5
        # 중간 단계에서 prev, curr가 필요한 위치에 도달해있는 상태여서 바로 연결하면 된다.
        leftprev.next.next = curr
        leftprev.next = prev

        return dummy.next


# 참고 : https://www.youtube.com/watch?v=RF_M9tX4Eag
