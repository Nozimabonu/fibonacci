# Fibonacci with iterator
# 0 1 1 2 3 5

class Fibonacci:
    def __init__(self, stop):
        self.prev = 0
        self.current = 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.stop:
            self.prev = self.current
            self.current = self.prev + self.current
            return self.current

        else:
            raise StopIteration
