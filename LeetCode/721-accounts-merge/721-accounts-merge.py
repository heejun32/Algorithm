import collections


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        visited = [False] * len(accounts)
        email_accounts = collections.defaultdict(list)
        result = list()
        
        # Bulid a graph
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                email = account[j]
                email_accounts[email].append(i)
                
        # dfs
        def dfs(node, emails):
            if visited[node]:
                return None
            
            visited[node] = True
            for i in range(1, len(accounts[node])):
                email = accounts[node][i]
                emails.add(email)
                
                for neighbor in email_accounts[email]:
                    dfs(neighbor, emails)
                    
        for i, account in enumerate(accounts):
            if not visited[i]:
                name, emails = account[0], set()
                dfs(i, emails)
                result.append([name] + sorted(emails))
        
        return result