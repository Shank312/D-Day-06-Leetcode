
class Solution:
    def putMarbles(self, weights, k):

        n = len(weights)
        if k == 1 or k == n:
            return 0
        # compute contribution if we cut between i and i+1
        pair_sums = [weights[i] + weights[i+1] for i in range(n-1)]

        # sort possible cut contributions
        pair_sums.sort()

        # maximum score -> choose (k-1) largest cuts
        # minimum score -> choose (k-1) smallest cuts
        return sum(pair_sums[-(k-1):]) - sum(pair_sums[:k-1])