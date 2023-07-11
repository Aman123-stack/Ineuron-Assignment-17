q1>def first_uniq_char(s):
    char_counts = {}

    # Count the frequencies of each character
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    # Find the first non-repeating character
    for i in range(len(s)):
        if char_counts[s[i]] == 1:
            return i

    return -1


q2>def max_subarray_sum_circular(nums):
    # Case 1: Find the maximum sum subarray (non-circular)
    max_sum_non_circular = kadane(nums)

    # Case 2: Find the maximum sum subarray (circular)
    max_sum_circular = sum(nums) + kadane([-num for num in nums])

    # Return the maximum of the two cases
    return max(max_sum_non_circular, max_sum_circular)

def kadane(nums):
    current_max = nums[0]
    global_max = nums[0]

    for i in range(1, len(nums)):
        current_max = max(nums[i], current_max + nums[i])
        global_max = max(global_max, current_max)

    return global_max


q3>def count_students_unable_to_eat(students, sandwiches):
    queue = students.copy()
    stack = sandwiches.copy()

    while queue:
        if queue[0] == stack[0]:
            queue.pop(0)
            stack.pop(0)
        else:
            if stack.count(queue[0]) == 0:
                break
            else:
                queue.append(queue.pop(0))

    return len(queue)



q4>from collections import deque

class RecentCounter:
    def __init__(self):
        self.requests = deque()

    def ping(self, t):
        self.requests.append(t)

        while self.requests[0] < t - 3000:
            self.requests.popleft()

        return len(self.requests)



q5>def find_winner(n, k):
    friends = list(range(1, n + 1))
    current = 0

    while len(friends) > 1:
        current = (current + k - 1) % len(friends)
        friends.pop(current)

    return friends[0]



q6>import collections

def reveal_cards_increasing_order(deck):
    deck.sort()
    n = len(deck)
    result = [0] * n
    queue = collections.deque(range(n))
    index = 0

    while queue:
        result[queue.popleft()] = deck[index]
        index += 1
        if queue:
            queue.append(queue.popleft())

    return result



q7>from collections import deque

class FrontMiddleBack:
    def __init__(self):
        self.queue = deque()

    def pushFront(self, val):
        self.queue.appendleft(val)

    def pushMiddle(self, val):
        middle = len(self.queue) // 2
        self.queue.insert(middle, val)

    def pushBack(self, val):
        self.queue.append(val)

    def popFront(self):
        if self.queue:
            return self.queue.popleft()
        else:
            return -1

    def popMiddle(self):
        if self.queue:
            middle = (len(self.queue) - 1) // 2
            return self.queue.pop(middle)
        else:
            return -1

    def popBack(self):
        if self.queue:
            return self.queue.pop()
        else:
            return -1



q8>from collections import deque

class DataStream:
    def __init__(self, value, k):
        self.value = value
        self.k = k
        self.stream = deque()

    def consec(self, num):
        self.stream.append(num)

        if len(self.stream) >= self.k:
            return list(self.stream)[-self.k:] == [self.value] * self.k

        return False
