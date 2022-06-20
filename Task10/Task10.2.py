import matrix
import random
from flask import Flask


app = Flask(__name__)


@app.route("/matrix/<int:n>/<int:m>/sort")
def sort_matrix(n, m):
    mx = matrix.generate_matrix(m, n)
    mx = matrix.sort_matrix(mx, m)
    return dict(rows=n, cols=m, result=mx)

# if __name__ == "__main__":
app.run()