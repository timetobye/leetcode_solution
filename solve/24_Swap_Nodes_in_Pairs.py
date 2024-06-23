# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        # 값을 스왑해주는 방법
        while curr and curr.next:
            curr.val, curr.next.val = curr.next.val, curr.val
            curr = curr.next.next

        return head


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = prev = ListNode(None)
        prev.next = head

        while head and head.next:
            b = head.next
            head.next = b.next
            b.next = head

            prev.next = b

            head = head.next
            prev = prev.next.next

        return root


"""
head = 1 -> 2 -> 3 -> 4 기준
처음 While 문이 실행된다고 할 때
- b는 현재 노드(head)의 다음 노드를 가리킵니다. (b = 2)
- 현재 노드(head, 즉 1)의 다음 노드를 b의 다음 노드로 변경합니다. (head.next = 3)
- b의 다음 노드를 현재 노드로 변경합니다. (b.next = 1)
- prev의 다음 노드를 b로 설정합니다. (prev.next = 2)
- head를 다음 위치로 이동시킵니다. (head = 3)
- prev를 두 칸 앞으로 이동시킵니다. (prev = 1)

상태 (첫 번째 반복 후: 2 -> 1 -> 3 -> 4)
- head = 3
- prev = 1

두 번째 반복 (현재 상태: head = 3 -> 4)
- b는 head의 다음 노드를 가리킵니다. (b = 4)
- head.next를 b.next로 설정합니다. (head.next = None)
- b.next를 head로 설정합니다. (b.next = 3)
- prev.next를 b로 설정합니다. (prev.next = 4)
- head를 다음 위치로 이동시킵니다. (head = None)
- prev를 두 칸 앞으로 이동시킵니다. (prev = 3)

상태 (두 번째 반복 후: 2 -> 1 -> 4 -> 3)
- head = None
- prev = 3

정리
- root는 더미 노드로 결과 리스트의 시작을 추적합니다.
- prev는 현재 노드의 이전 노드를 추적하여 스왑 후 올바른 링크를 설정합니다.
- while 문 내에서 두 노드를 스왑하고 포인터들을 업데이트하여 다음 쌍으로 이동합니다.
- root.next를 반환하여 더미 노드 이후의 리스트를 결과로 반환합니다.
"""
