class Knapsack:
    """
    weights[], capacity
    """

    def resolve(self, weights, capacity):
        if not self._is_valid(weights, capacity):
            return [], -1

        n = len(weights)
        dp = [[False for _ in range(capacity + 1)] for _ in range(n)]
        dp[0][0] = True
        dp[0][weights[0]] = True
        for i in range(1, n):
            # exclusion
            for w in range(0, capacity + 1):
                if dp[i - 1][w]:
                    dp[i][w] = True

            # inclusion
            for w in range(0, capacity - weights[i] + 1):
                if dp[i - 1][w]:
                    dp[i][w + weights[i]] = True

        # find the max weight under the capacity limit
        max_weight = -1
        for w in range(capacity, -1, -1):
            if dp[n - 1][w]:
                max_weight = w
                break

        # find what items are selected
        items, weight = [], max_weight
        for i in range(n - 1, 0, -1):
            if dp[i - 1][weight - weights[i]]:
                items.append(weights[i])
                weight -= weights[i]

        if weight > 0:
            items.append(weights[0])

        return items, max_weight

    def resolve_v2(self, weights, capacity):
        """
        dp[i][j] refers to the max weight of first i (not "i"th) elements in the capacity of j.

        if j >= weights[i-1]:
            dp[i][j] = max(dp[i-1][j - weights[i-1]] + weights[i-1], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
        """
        if not self._is_valid(weights, capacity):
            return -1

        n = len(weights)
        dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, capacity + 1):
                if j >= weights[i - 1]:
                    dp[i][j] = dp[i - 1][j - weights[i - 1]] + weights[i - 1]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n][capacity]

    @staticmethod
    def _is_valid(weights, capacity):
        if not weights or capacity < 0:
            return False
        else:
            return True


class KnapsackII:
    """
    weights[], values[], capacity
    """

    def resolve(self, weights, values, capacity):
        if not self._is_valid(weights, values, capacity):
            return [], -1, -1

        n = len(weights)
        dp = [[-1 for _ in range(capacity + 1)] for _ in range(n)]
        dp[0][0] = 0
        dp[0][weights[0]] = values[0]
        for i in range(1, n):
            # exclusion
            for w in range(0, capacity + 1):
                if dp[i - 1][w] > -1:
                    dp[i][w] = dp[i - 1][w]

            # inclusion
            for w in range(0, capacity - weights[i] + 1):
                if dp[i - 1][w] > -1:
                    dp[i][w + weights[i]] = max(dp[i][w + weights[i]], dp[i - 1][w] + values[i])

        # get the max value as well as the weight
        max_weight, max_value = -1, -1
        for w in range(capacity, -1, -1):
            value = dp[n - 1][w]
            if value > max_value:
                max_value = value
                max_weight = w

        # find what items are selected
        items, weight, value = [], max_weight, max_value
        for i in range(n - 1, 0, -1):
            if dp[i - 1][weight - weights[i]] == value - values[i]:
                items.append((weights[i], values[i]))
                weight -= weights[i]
                value -= values[i]

        if weight > 0:
            items.append((weights[0], values[0]))

        return items, max_weight, max_value

    def resolve_v2(self, weights, values, capacity):
        """
        dp[i][j] refers to the max value of first i (not "i"th) elements in the capacity of j.

        if j >= weights[i-1]:
            dp[i][j] = max(dp[i-1][j - weights[i-1]] + values[i-1], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
        """
        if not self._is_valid(weights, values, capacity):
            return -1

        n = len(weights)
        dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, capacity + 1):
                if j >= weights[i - 1]:
                    dp[i][j] = max(dp[i - 1][j - weights[i - 1]] + values[i - 1], dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][capacity]

    @staticmethod
    def _is_valid(weights, values, max_weight):
        if not weights or not values or max_weight < 0:
            return False
        else:
            return True

# print(Knapsack().resolve([1, 3, 6, 8], 13))
# print(Knapsack().resolve_v2([1, 3, 6, 8], 13))
# print(KnapsackII().resolve([2, 2, 6, 5, 4], [6, 3, 5, 4, 6], 10))
# print(KnapsackII().resolve_v2([2, 2, 6, 5, 4], [6, 3, 5, 4, 6], 10))
