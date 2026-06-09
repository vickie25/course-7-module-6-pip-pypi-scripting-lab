from datetime import datetime

def generate_log(data):
    if not isinstance(data, list):
        raise ValueError("data must be a list")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w", encoding="utf-8") as file:
        for entry in data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")
    return filename


def fetch_data():
    import requests

    response = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=10)
    if response.status_code == 200:
        return response.json()
    return {}


if __name__ == "__main__":
    log_data = ["User logged in", "User updated profile", "Report exported"]
    filename = generate_log(log_data)
    post = fetch_data()
    print(f"Fetched Post Title: {post.get('title', 'No title found')}")
