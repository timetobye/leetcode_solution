# ref : https://www.youtube.com/watch?v=XIdigk956u0


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # 더미 노드 생성
        dummy = ListNode()
        # 포인터 역할
        node = dummy

        while list1 and list2:  # 연결 리스트가 계속 존재 할 떄
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next

            else:
                node.next = list2
                list2 = list2.next

            # 병합된 리스트를 만들기 위해서 node.next에 새로 연결된 노드를 설정한 후, node를 다음 위치로 이동
            # 이동하지 않으면 같은 곳에서 연결을 하게 됨
            node = node.next

        # 어떤 것이 먼저 끝날지 알 수 없다.
        if list1:
            node.next = list1
        elif list2:
            node.next = list2

        return dummy.next


# 알고리즘 책에는 아래와 같은 풀이가 제시 되었다.


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if (not list1) or (list2 and list1.val > list2.val):
            list1, list2 = list2, list1

        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)

        return list1
