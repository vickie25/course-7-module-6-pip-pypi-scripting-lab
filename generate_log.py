# Re-export from lib.generate_log for test compatibility
from lib.generate_log import generate_log, fetch_data

__all__ = ["generate_log", "fetch_data"]

if __name__ == "__main__":
    log_data = ["User logged in", "User updated profile", "Report exported"]
    filename = generate_log(log_data)
    post = fetch_data()
    print(f"Fetched Post Title: {post.get('title', 'No title found')}")
