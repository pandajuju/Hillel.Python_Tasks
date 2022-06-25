# Завдання: встановити requests (так само як колись flask),
#           запустати сервер на виконання та викликати
#           http://localhost:5000/image у браузері.
#
# Підказка: Виконати pip install requests або sudo pip install requests
#           у консолі.
import flask
import requests

app = flask.Flask(__name__)


@app.route("/jokes")
def get_joke():
    ret = requests.get(
        "https://api.jokes.one/jod",
        params={"content-type": "application/json"}
    )
    response_json = ret.json()
    joke = response_json["contents"]["jokes"][0]["joke"]
    return dict(title=joke["title"], joke=joke["text"])


if __name__ == "__main__":
    app.run(debug=True)