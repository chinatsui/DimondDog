class Fibonacci:
    def generate(self, n, a=1, b=1):
        if n <= 2:
            return b
        else:
            return self.generate(n - 1, b, a + b)

    @staticmethod
    def iterator(n):
        a, b = 1, 1
        while n > 0:
            yield a
            n -= 1
            a, b = b, a + b
