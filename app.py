import sys
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/user")
def show_user():
    print('enter getJSONReuslt', flush=True)
    return """<!DOCTYPE html>
<html>
<head>
<title>타이틀</title>
</head>
<body>
<h1>저의 첫 웹사이트 오신것을 환영합니다!</h1>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True, port=26900)