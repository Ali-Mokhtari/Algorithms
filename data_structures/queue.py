"""
Title: Data Structures

Author: Ali Mokhtari
GitHub: @Ali-Mokhtari
Date: September 2023

Q: Implement a queue of at most n elements using an array of size n+1. The
queue has an attribute 'head' that indexes, or points to, its head. The
attribute 'tail' indexes the next location at which a newly arriving element
will be inserted into the queue.

Example:
n = 11
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, None]
     ^                                   ^
     |                                   |
    head                                tail

* dequeue() returns 1 and increments head by 1.
A = [None, 2 , 3, 4, 5, 6, 7, 8, 9, 10, 11, None]
           ^                                 ^
           |                                 |
          head                              tail
* enqueue(12) inserts 12 into A[tail].
A = [None, 2 , 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
      ^    ^
      |    |
     tail head
queue is full.

Assumptions:
1. The location 0 immediately follows the location n in the array
in a circular order.


Methods:
1. enqueue(x): Insert x into the queue.
2. dequeue(): Remove and return the head of the queue.
3. is_empty(): Return true if the queue is empty, false otherwise.
4. is_full(): Return true if the number of elements in the queue is n,
   false otherwise.

Solution:
1. Create a class called Queue.
2. Initialize the class with an array of size n+1.
3. Initialize the head and tail to 0.
4. Implement enqueue(x) by checking if the queue is full.
5. If the queue is full, raise an exception.
6. If the queue is not full, insert x into A[tail] and incremen tail by 1.
7. Implement dequeue() by checking if the queue is empty.
8. If the queue is empty, raise an exception.
9. If the queue is not empty, return A[head] and increment head by 1.
10. Implement is_empty() by checking if head == tail.
11. Implement is_full() by checking if head == tail + 1.

Time Complexity: O(1) for all methods.
"""


class Queue:

    def __init__(self, length) -> None:
        self.array = [None] * (length+1)
        self.length = length
        self.head = 0
        self.tail = 0

    def is_full(self):
        if self.tail == self.length:
            return self.head == 0
        else:
            return self.head == self.tail + 1

    def is_empty(self):
        return self.head == self.tail

    def enqueue(self, x):
        if self.is_full():
            raise Exception('Queue is full.')
        self.array[self.tail] = x
        if self.tail == self.length:
            self.tail = 0
        else:
            self.tail += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty.')
        element = self.array[self.head]
        self.array[self.head] = None
        if self.head == self.length:
            self.head = 0
        else:
            self.head += 1
        return element


def test_with_empty_queue():
    q = Queue(3)
    assert q.is_empty() is True, 'Failed with empty queue.'


def test_with_full_queue():
    q = Queue(3)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.is_full() is True, 'Failed with full queue.'


def test_with_enqueue():
    q = Queue(3)
    q.enqueue(1)
    assert q.array == [1, None, None, None], 'Failed with enqueue.'
    q.enqueue(2)
    assert q.array == [1, 2, None, None], 'Failed with enqueue.'
    q.enqueue(3)
    assert q.array == [1, 2, 3, None], 'Failed with enqueue.'
    try:
        q.enqueue(4)
    except Exception as e:
        assert str(e) == 'Queue is full.', 'Failed with enqueue.'


def test_with_dequeue():
    q = Queue(3)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.dequeue() == 1, 'Failed with dequeue.'
    assert q.array == [None, 2, 3, None], 'Failed with dequeue.'
    assert q.dequeue() == 2, 'Failed with dequeue.'
    assert q.array == [None, None, 3, None], 'Failed with dequeue.'
    assert q.dequeue() == 3, 'Failed with dequeue.'
    assert q.array == [None, None, None, None], 'Failed with dequeue.'
    try:
        q.dequeue()
    except Exception as e:
        assert str(e) == 'Queue is empty.', 'Failed with dequeue.'


def test_with_enqueue_dequeue():
    q = Queue(6)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)
    assert q.is_full() is True, 'Failed with enqueue and dequeue.'
    q.dequeue()
    q.dequeue()
    q.dequeue()
    assert q.array == [None, None, None, 4, 5, 6, None], 'Failed with enqueue and dequeue.'
    q.enqueue(7)
    q.enqueue(8)
    assert q.array == [8, None, None, 4, 5, 6, 7], 'Failed with enqueue and dequeue.'


if __name__ == '__main__':
    test_with_empty_queue()
    test_with_full_queue()
    test_with_enqueue()
    test_with_dequeue()
    test_with_enqueue_dequeue()
    print('All tests have passed successfully.')
