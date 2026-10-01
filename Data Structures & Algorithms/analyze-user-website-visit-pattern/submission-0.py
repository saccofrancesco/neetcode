from collections import defaultdict
from itertools import combinations

class Solution:
    def mostVisitedPattern(
        self,
        username: List[str],
        timestamp: List[int],
        website: List[str]
    ) -> List[str]:

        visits = sorted(zip(timestamp, username, website))

        user_sites = defaultdict(list)

        for time, user, site in visits:
            user_sites[user].append(site)

        count = defaultdict(int)

        for sites in user_sites.values():
            patterns = set(combinations(sites, 3))

            for pattern in patterns:
                count[pattern] += 1

        best_pattern = None
        best_score = 0

        for pattern, score in count.items():
            if score > best_score:
                best_score = score
                best_pattern = pattern
            elif score == best_score and pattern < best_pattern:
                best_pattern = pattern

        return list(best_pattern)