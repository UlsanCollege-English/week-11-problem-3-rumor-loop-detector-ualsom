
## main.py
```python
"""
HW03 — Rumor Loop Detector (Cycle in Undirected Graph)

Implement:
- has_cycle(graph)
- find_cycle(graph)
"""

def has_cycle(graph):
    """Return True if the undirected graph has any cycle; else False."""
    raise NotImplementedError

def find_cycle(graph):
    """Return a list of nodes forming a simple cycle where first == last.
    If no cycle, return None.

    Note:
    - Use DFS and a parent map.
    - Self-loop counts: return [u, u].
    """
    raise NotImplementedError
