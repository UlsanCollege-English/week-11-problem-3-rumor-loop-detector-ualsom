# HW03 — Rumor Loop Detector (DFS Cycle in Undirected Graph)

**Story intro.**  
In a chat group, a rumor can circle back to its start if people repeat it in a loop. You will check if the contact network contains a **cycle**. If yes, return one simple cycle.

**Technical description.**  
- **Input:** `graph` as adjacency list `dict` for an **undirected** graph.  
- **Outputs:**  
  - `has_cycle(graph)` → `True/False`.  
  - `find_cycle(graph)` → list of nodes forming a simple cycle where first == last, or `None` if acyclic.  
- **Constraints:**  
  - Graph may be disconnected.  
  - Self-loop counts as a cycle of length 1 (`['X','X']`).  
- **Expected complexity:** **O(V+E)** time, **O(V)** space.

## ESL scaffold with the 8 Steps
**Brief prompts (Steps 1–3)**
1. **Read & Understand:** What is a cycle in an undirected graph?  
2. **Re-phrase:** “Follow edges; if we see a visited node that is not the parent, we found a cycle.”  
3. **Identify I/O:** Inputs: `graph`. Outputs: bool and a cycle list.

**You handle Steps 4–8.**  
- Use DFS with a `parent` map.  
- Rebuild the cycle by walking parents from the two meeting nodes.  
- State big-O in a sentence.

## Hints
- For each new DFS start, set parent to `None`.  
- When at `(u, v)` and `v` is visited and `v != parent[u]`, you found a back-edge.  
- To build a cycle list, walk `u` and `v` up their parents until they meet.

## Run tests locally
```bash
python -m pytest -q
```
## FAQ
Q: Directed cycles? A: Not in this homework. Undirected only.

Q: Multiple cycles? A: Return any one.

Q: Self-loop? A: Treat as a valid cycle ['X','X'].

Q: Parallel edges? A: You may treat neighbor lists as given; typical inputs avoid multi-edges.

Q: Big-O? A: O(V+E) time, O(V) space.

Q: Reading stdin? A: No. Implement functions.

Q: Tests failing with order differences? A: We check sets/structure, not exact order except start==end.