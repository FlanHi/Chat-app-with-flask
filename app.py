from flask import Flask, render_template, request

app = Flask(__name__)
messages = []

@app.route('/')
@app.route("/index", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if 'username' in request.form and 'message' in request.form and 'link' in request.form:
            username = request.form['username']
            message = request.form['message']
            link = request.form['link']
            messages.append((username, message, link))
            return render_template("chat.html", messages=messages)
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
