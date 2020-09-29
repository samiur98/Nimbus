import requests

# Test request
def test_request():
    URL = "http://127.0.0.1:5000/test"
    request = requests.get(url = URL)
    data = request.json()
    print(data)

# Main entry point of the client
def main():
    test_request()
    print("Working")

if __name__ == "__main__":
    main()