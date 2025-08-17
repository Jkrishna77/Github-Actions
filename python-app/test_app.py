from app import add, get_github_status

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_github_status():
    status = get_github_status()
    assert "GitHub API" in status
