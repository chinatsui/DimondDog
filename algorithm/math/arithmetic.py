class PrimeFactorization:

    @staticmethod
    def factorize(n):
        i = 2
        res = []
        while n > 1:
            if n % i == 0:
                res.append(i)
                n = n // i
            else:
                i += 1
        return res


class GreatestCommonDivisor:

    @staticmethod
    def get_gcd_by_prime_factorization(x, y):
        pf = PrimeFactorization()
        x_fac = pf.factorize(x)
        y_fac = pf.factorize(y)

        common_divisors = []
        i, j = 0, 0
        while i < len(x_fac) and j < len(y_fac):
            if x_fac[i] == y_fac[j]:
                common_divisors.append(x_fac[i])
                i += 1
                j += 1
            elif x_fac[i] < y_fac[j]:
                i += 1
            else:
                j += 1

        res = 1
        for div in common_divisors:
            res *= div

        return res

    def get_gcd_by_euclidean(self, x, y):
        if x % y == x:
            return self.get_gcd_by_euclidean(y, x)
        elif x % y == 0:
            return y
        else:
            return self.get_gcd_by_euclidean(y, x % y)


class LeastCommonMultiple:

    @staticmethod
    def get_lcm(x, y):
        pf = PrimeFactorization()
        x_fac = pf.factorize(x)
        y_fac = pf.factorize(y)

        common_divs = []
        exclusive_divs = []

        i, j = 0, 0
        while i < len(x_fac) and j < len(y_fac):
            if x_fac[i] == y_fac[j]:
                common_divs.append(x_fac[i])
                i += 1
                j += 1
            elif x_fac[i] < y_fac[j]:
                exclusive_divs.append(x_fac[i])
                i += 1
            else:
                exclusive_divs.append(y_fac[j])
                j += 1

        while i < len(x_fac):
            exclusive_divs.append(x_fac[i])
            i += 1

        while j < len(y_fac):
            exclusive_divs.append(y_fac[j])
            j += 1

        res = 1
        for div in common_divs:
            res *= div

        for div in exclusive_divs:
            res *= div

        return res


print(GreatestCommonDivisor().get_gcd_by_prime_factorization(24, 60))
print(GreatestCommonDivisor().get_gcd_by_euclidean(319, 377))
print(LeastCommonMultiple().get_lcm(24, 60))
