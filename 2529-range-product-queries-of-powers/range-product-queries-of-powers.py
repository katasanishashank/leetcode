class Solution(object):
    def productQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10**9 + 7

        # Step 1: Get list of powers of 2 that sum to n
        powers = []
        for i in range(31):  # Since 2^30 > 1e9
            if n & (1 << i):
                powers.append(1 << i)

        # Step 2: Precompute prefix products
        prefix = [1] * len(powers)
        prefix[0] = powers[0]
        for i in range(1, len(powers)):
            prefix[i] = (prefix[i - 1] * powers[i]) % MOD

        # Step 3: Answer the queries
        result = []
        for left, right in queries:
            if left == 0:
                result.append(prefix[right])
            else:
                # Use modular inverse to divide under modulo
                product = (prefix[right] * pow(prefix[left - 1], MOD - 2, MOD)) % MOD
                result.append(product)

        return result
