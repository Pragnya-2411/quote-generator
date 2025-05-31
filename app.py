from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    if response.status_code == 200:
        data = response.json()
        return f'{data[0]["q"]} — {data[0]["a"]}'
    else:
        return "Could not fetch a quote at the moment."

@app.route("/")
def home():
    quote = get_quote()
    return render_template("index.html", quote=quote)

if __name__ == "__main__":
    app.run(debug=True)