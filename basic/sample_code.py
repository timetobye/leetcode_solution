# type hint

# def fn_non_type(a):
#     return a

def fn_type(a: int) -> bool:
    """
    <class 'int'>
    3
    """
    print(type(a))

    return a

# dict
a = {key: value for key, value in original.items()}

# generator : 1억 개의 숫자를 만든다고 할 때, 1억 개를 보관하고 있을 것인가? 하나씩 나중에 만들 것인가?


def get_natural_number():
    n = 0

    while True:
        n += 1
        yield n

g = get_natural_number()
for _ in range(0, 100):
    print(next(g))

def generator():
    yield 1
    yield 'string'
    yield True

g = generator()


# 메모리 점유율

a = [n for n in range(100000)]
b = range(100000)
b[999] # 이렇게 해도 slicing 가능

"""
a 는 생성된 값이 담겨 있고, b는 생성해야 한다는 조건만 존재

sys.getsizeof(a), sys.getsizeof(b) 를 하면 훨씬 더 적은 메모리 차지 하고 있음
"""


# print 출력 방식
"""
>>> print('A1', 'A2', sep=',')
A1,A2
>>> print('A1', 'A2')
A1 A2
"""

