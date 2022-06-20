# Завдання: розширити matrix модуль з sort_matrix_bubble
#           де буде імплементоване сортування бульбашкою.
#           Розширити matrix/n/m/sort endpoint з наступного
#           завдання підтримкою бабл сорту поряд з quicksort'ом

import matrix
import random
from flask import Flask


app = Flask(__name__)

@app.route("/matrix/<int:n>/<int:m>/sort/")
@app.route("/matrix/<int:n>/<int:m>/sort/<sort_algo>")
def sort_matrix(n, m, sort_algo="quick"):
    ret_val = dict(rows=n, cols=m)
    mx = matrix.generate_matrix(m, n)

    if sort_algo == "bubble":
        mx = matrix.sort_matrix_bubble(mx, m)
        ret_val["result"] = mx
    elif sort_algo == "quick":
        mx = matrix.sort_matrix(mx, m)
        ret_val["result"] = mx
    else:
        ret_val["result"] = f"error: unsupported sort algo {sort_algo}"
    return ret_val

# if __name__ == "__main__":
app.run()