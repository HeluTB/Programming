class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        parts = path.split("/")
        
        for p in parts:
            if p == "..":
                if stack:
                    stack.pop()
            elif p == "." or not p:
                continue
            else:
                stack.append(p)
        
        return "/" + "/".join(stack)