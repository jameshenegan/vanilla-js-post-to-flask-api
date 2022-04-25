from flask import Flask, request

app = Flask(__name__, static_folder="../frontend", static_url_path="/")

@app.route("/")
def index():
    return app.send_static_file('index.html')

@app.route("/api/fetchData", methods = ['POST'])
def fetch_data():
    data = request.get_json()
    print(data)
    return {"message": "hello"}

if __name__ == "__main__":
    app.run(host = "0.0.0.0")