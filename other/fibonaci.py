class Fibonacci:

    @staticmethod
    def generate(n):
        a, b = 1, 1
        while n > 0:
            yield a
            a, b = b, a + b
            n -= 1
