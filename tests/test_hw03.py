from hw03.main import has_cycle, find_cycle

def test_no_cycle():
    graph = {"A": ["B"], "B": ["A", "C"], "C": ["B"]}
    assert has_cycle(graph) is False
    assert find_cycle(graph) is None

def test_simple_cycle():
    graph = {"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B"]}
    assert has_cycle(graph) is True
    cycle = find_cycle(graph)
    assert cycle[0] == cycle[-1]
    assert len(cycle) >= 3

def test_self_loop():
    graph = {"A": ["A"]}
    assert has_cycle(graph) is True
    cycle = find_cycle(graph)
    assert cycle == ["A", "A"]
