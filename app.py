from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    response = requests.get("https://zenquotes.io/api/random")
    if response.status_code == 200:
        data = response.json()
        quote = data[0].get("q")  # use "q" for the quote
        author = data[0].get("a")  # use "a" for the author
        return render_template("index.html", quote=quote, author=author)
    else:
         return "Could not fetch a quote at the moment."

if __name__ == "__main__":
    app.run(debug=True)
