from flask import Flask, jsonify

app = Flask(__name__)
# Test Route

@app.route('/test', methods = ["GET"])
def test():
    response = jsonify("This is a test")
    response.status_code = 200
    return response

if __name__ == "__main__":
    app.run(debug=True)