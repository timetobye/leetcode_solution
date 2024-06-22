# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = ListNode()
        node = head  # linked list 의 시작 부분을 기억을 할 수 있도록 처리

        carry_value = 0

        while l1 or l2 or carry_value:
            sum_value = 0

            if l1:
                sum_value += l1.val
                l1 = l1.next

            if l2:
                sum_value += l2.val
                l2 = l2.next

            # sum_value = carry_value + sum_value
            # carry_value = sum_value // 10
            # sum_value = sum_value - carry_value * 10
            # 찾아보니 이렇게 간단하게 처리가 가능하다.
            carry_value, sum_value = divmod(sum_value + carry_value, 10)

            head.next = ListNode(sum_value)
            head = head.next

        return node.next  # 시작 부분 다음부터 출력 하면 정답
