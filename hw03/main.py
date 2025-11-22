# hw03/main.py

def has_cycle(graph):
    """Return True if the undirected graph has any cycle; else False."""
    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                # Found a back edge => cycle
                return True
        return False

    for node in graph:
        if node not in visited:
            if dfs(node, None):
                return True
    return False


def find_cycle(graph):
    """Return a list of nodes forming a simple cycle where first == last.
    If no cycle, return None.
    """
    visited = set()
    parent = {}

    def dfs(node, par):
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                parent[neighbor] = node
                result = dfs(neighbor, node)
                if result:
                    return result
            elif neighbor != par:
                # Cycle detected: reconstruct path
                path = [neighbor]
                cur = node
                while cur != neighbor:
                    path.append(cur)
                    cur = parent[cur]
                path.append(neighbor)
                path.reverse()
                return path
        return None

    for node in graph:
        if node not in visited:
            parent[node] = None
            result = dfs(node, None)
            if result:
                return result
    return None
