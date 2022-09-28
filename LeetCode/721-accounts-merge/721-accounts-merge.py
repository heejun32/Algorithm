import collections

'''
N is accounts.length. M is a total of emails.
Time Complexity
- O(MlogM) because of sorted
Space Complexity is O(N + M). N is accounts.length. M is a total of emails.
'''
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
                
                # email이라는 edge로 연결되어 있는 이웃 account(노드)를 dfs 수행.
                for neighbor in email_accounts[email]:
                    dfs(neighbor, emails)
                    
        for i, account in enumerate(accounts):
            if not visited[i]:
                name, emails = account[0], set()
                dfs(i, emails)
                result.append([name] + sorted(emails))
        
        return result