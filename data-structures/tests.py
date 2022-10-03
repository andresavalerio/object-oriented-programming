# Andresa Lopes Valério
# RA 149451

from data_structures import Stack, Queue

def test_stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    p = stack.pop()
    assert p == 2

def test_long_stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(6)
    p = stack.pop()
    assert p == 6

def test_string_stack():
    stack = Stack()
    stack.push("John")
    stack.push("Annie")
    p = stack.pop()
    assert p == "Annie"

def test_queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    d = queue.dequeue()
    assert d == 1

def test_long_queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(6)
    d = queue.dequeue()
    assert d == 1

def test_string_queue():
    queue = Queue()
    queue.enqueue("John")
    queue.enqueue("Annie")
    d = queue.dequeue()
    assert d == "John"
