# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head) -> bool:
        q = []

        if not head:
            return True

        node = head
        while node is not None:
            q.append(node.val)  # 데이터 추가
            node = node.next  # 다음 노드로 연결

        while len(q) > 1:
            if q.pop(0) != q.pop():  # 값 비교
                return False

        return True


from collections import deque

# deque 를 이용한 풀이 : 코드 최적화 관점에서 접근
# q.pop(0) 를 사용할 경우 모든 값이 한 칸씩 시프팅(shifting) 되면서 시간 복잡도 O(n)이 발생
# 최적화를 위해 데이터를 가져올 때 deque 를 이용하면 O(1) 시간내에 가져올 수 있다.


class Solution:
    def isPalindrome(self, head) -> bool:
        deq = deque()

        if not head:
            return True

        node = head
        while node is not None:
            deq.append(node.val)  # 데이터 추가
            node = node.next  # 다음 노드로 연결

        while len(deq) > 1:
            if deq.popleft() != deq.pop():
                return False

        return True


# Runner - Fast Runner + Slow Runner


class Solution:
    def isPalindrome(self, head) -> bool:
        rev = None
        slow = fast = head

        while fast and fast.next:
            # 두 칸씩 이동
            fast = fast.next.next
            # 중간에 도달하는 느린 런너가 나머지 경로를 이동할 때 역순으로 만든 연결 리스트와 일치하는지 확인
            # rev 는 역순을 확인하기 위해 붙임 -> 앞에 계속 새로운 노드가 추가되는 형태 -> slow 의 역순 연결 리스트
            rev, rev.next, slow = slow, rev, slow.next

        # 입력값이 홀수일 때와 짝수일 때 처리 방법
        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next

        # 정상적이라면 slow, rev 가 모두 끝까지 이동해 둘다 None이 될 것이다
        return not rev
