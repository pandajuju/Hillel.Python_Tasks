from toolset import fun
from flask import Flask


app = Flask(__name__)
@app.route("/toolset/fun/fizzbuzz/<int:N>/")
def fizzbuzz(N):
    result = fun.fizzbuzz(N)
    return dict(result=f"{result}")



if __name__ == "__main__":
    app.run()