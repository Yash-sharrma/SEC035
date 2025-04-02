from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    items = ["Apple", "Banana", "Cherry", "Date"]
    return render_template("list.html", items=items)

if __name__ == '__main__':
    app.run(debug=True)
