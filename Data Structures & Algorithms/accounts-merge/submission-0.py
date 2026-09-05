from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        n = len(accounts)

        parent = list(range(n))
        rank = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                return

            if rank[root_a] < rank[root_b]:
                root_a, root_b = root_b, root_a

            parent[root_b] = root_a
            rank[root_a] += rank[root_b]

        email_to_account = {}

        # Connect accounts that share an email
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_account:
                    union(i, email_to_account[email])
                else:
                    email_to_account[email] = i

        # Group emails by their final parent
        groups = defaultdict(list)

        for email, account_index in email_to_account.items():
            root = find(account_index)
            groups[root].append(email)

        result = []

        for root, emails in groups.items():
            name = accounts[root][0]
            result.append([name] + sorted(emails))

        return result