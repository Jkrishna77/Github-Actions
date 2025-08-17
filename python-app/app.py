import requests

def get_github_status():
    """Fetch GitHub status API and return status"""
    response = requests.get("https://api.github.com")
    if response.status_code == 200:
        return "GitHub API is reachable"
    return "GitHub API is not reachable"

def add(a, b):
    """Simple add function"""
    return a + b

if __name__ == "__main__":
    print("Sum:", add(2, 3))
    print(get_github_status())
