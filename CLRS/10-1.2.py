"""
CLRS Question
Author: Ali Mokhtari
GitHub: @Ali-Mokhtari
Date: September 2023

Q: Implement two stacks in one array A[1..n] in such a way that neither stack
overflows unless the total number of elements in both stacks together is n.
The PUSH and POP operations should run in O(1) time.

Methods:
1. Push1(x): Insert x into stack 1.
2. Push2(x): Insert x into stack 2.
3. Pop1(): Remove and return the most recently inserted element from stack 1.
4. Pop2(): Remove and return the most recently inserted element from stack 2.
5. IsEmpty1(): Return true if stack 1 is empty, false otherwise.
6. IsEmpty2(): Return true if stack 2 is empty, false otherwise.
6. IsFull(): Return true if top1 == top2 - 1, false otherwise.

Solution:
1. Create a class called TwoStacks.
2. Initialize the class with an array of size n.
3. Initialize the top1 and top2 to -1.
4. Implement Push1(x) by incrementing top1 by 1 and inserting x into A[top1].
5. Implement Push2(x) by incrementing top2 by 1 and inserting x into A[top2].
6. Implement Pop1() by returning A[top1] and decrementing top1 by 1.
7. Implement Pop2() by returning A[top2] and decrementing top2 by 1.
8. Implement IsEmpty() by checking if top1 and top2 are -1.
9. Implement IsFull() by checking if top1 + top2 == n - 1.

Time Complexity: O(1) for all methods.
"""


class TwoStacks:
    def __init__(self, n):
        self.size = n
        self.array = [None] * n
        self.top1 = -1
        self.top2 = n

    def push1(self, x):
        if self.is_full():
            raise Exception('Stack 1 is full.')
        self.top1 += 1
        self.array[self.top1] = x

    def push2(self, x):
        if self.is_full():
            raise Exception('Stack 2 is full.')
        self.top2 -= 1
        self.array[self.top2] = x

    def pop1(self):
        if self.top1 == -1:
            raise Exception('Stack 1 is empty.')
        else:
            self.top1 -= 1
            element = self.array[self.top1 + 1]
            self.array[self.top1 + 1] = None
            return element

    def pop2(self):
        if self.top2 == self.size:
            raise Exception('Stack 2 is empty.')
        else:
            self.top2 += 1
            element = self.array[self.top2 - 1]
            self.array[self.top2 - 1] = None
            return element

    def is_empty1(self):
        return self.top1 == -1

    def is_empty2(self):
        return self.top1 == self.size

    def is_full(self):
        return self.top1 == self.top2 - 1


def test_push1():
    two_stacks = TwoStacks(4)
    two_stacks.push1(1)
    assert two_stacks.array == [1, None, None, None], 'Failed with push1'
    two_stacks.push1(2)
    assert two_stacks.array == [1, 2, None, None], 'Failed with push1'
    two_stacks.push1(3)
    assert two_stacks.array == [1, 2, 3, None], 'Failed with push1'
    two_stacks.push1(4)
    assert two_stacks.array == [1, 2, 3, 4], 'Failed with push1'


def test_push1_exception():
    two_stacks = TwoStacks(4)
    two_stacks.push1(1)
    two_stacks.push1(2)
    two_stacks.push1(3)
    two_stacks.push1(4)
    try:
        two_stacks.push1(5)
    except Exception as e:
        assert str(e) == 'Stack 1 is full.', 'Failed with push1 exception'


def test_push1_push2():
    two_stacks = TwoStacks(4)
    two_stacks.push1(1)
    two_stacks.push1(2)
    two_stacks.push2(3)
    two_stacks.push2(4)
    assert two_stacks.array == [1, 2, 4, 3], 'Failed with push1 and push2'


def test_push1_push2_exception():
    two_stacks = TwoStacks(4)
    two_stacks.push1(1)
    two_stacks.push1(2)
    two_stacks.push2(3)
    two_stacks.push2(4)
    try:
        two_stacks.push2(5)
    except Exception as e:
        assert str(e) == 'Stack 2 is full.', 'Failed with push1 and push2 exception'
    try:
        two_stacks.push1(5)
    except Exception as e:
        assert str(e) == 'Stack 1 is full.', 'Failed with push1 and push2 exception'


def test_pop1():
    two_stacks = TwoStacks(4)
    two_stacks.push1(1)
    two_stacks.push1(2)
    two_stacks.push1(3)
    two_stacks.push1(4)
    assert two_stacks.pop1() == 4, 'Failed with pop1'
    assert two_stacks.pop1() == 3, 'Failed with pop1'
    assert two_stacks.pop1() == 2, 'Failed with pop1'
    assert two_stacks.pop1() == 1, 'Failed with pop1'


def test_pop1_exception():
    two_stacks = TwoStacks(4)
    try:
        two_stacks.pop1()
    except Exception as e:
        assert str(e) == 'Stack 1 is empty.', 'Failed with pop1 exception'


def test_pop2():
    two_stacks = TwoStacks(4)
    two_stacks.push2(1)
    two_stacks.push2(2)
    two_stacks.push2(3)
    two_stacks.push2(4)
    assert two_stacks.pop2() == 4, 'Failed with pop2'
    assert two_stacks.pop2() == 3, 'Failed with pop2'
    assert two_stacks.pop2() == 2, 'Failed with pop2'
    assert two_stacks.pop2() == 1, 'Failed with pop2'


def test_pop2_exception():
    two_stacks = TwoStacks(4)
    try:
        two_stacks.pop2()
    except Exception as e:
        assert str(e) == 'Stack 2 is empty.', 'Failed with pop2 exception'


def test_pop1_pop2():
    two_stacks = TwoStacks(4)
    two_stacks.push1(1)
    two_stacks.push1(2)
    two_stacks.push2(3)
    two_stacks.push2(4)
    assert two_stacks.pop1() == 2, 'Failed with pop1 and pop2'
    assert two_stacks.pop2() == 4, 'Failed with pop1 and pop2'
    assert two_stacks.pop1() == 1, 'Failed with pop1 and pop2'
    assert two_stacks.pop2() == 3, 'Failed with pop1 and pop2'


def test_pop1_pop2_exception():
    two_stacks = TwoStacks(4)
    two_stacks.push1(1)
    two_stacks.push1(2)
    two_stacks.push2(3)
    two_stacks.push2(4)

    try:
        two_stacks.pop1()
        two_stacks.pop2()
        two_stacks.pop1()
        two_stacks.pop2()
        two_stacks.pop2()
    except Exception as e:
        assert str(e) == 'Stack 2 is empty.', 'Failed with pop1 and pop2 exception'


if __name__ == '__main__':
    test_push1()
    test_push1_exception()
    test_push1_push2()
    test_push1_push2_exception()
    test_pop1()
    test_pop1_exception()
    test_pop2()
    test_pop2_exception()
    test_pop1_pop2()
    test_pop1_pop2_exception()
    print('All tests passed successfully.')
