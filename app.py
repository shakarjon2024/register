from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        name = request.form.get("name")
        age = request.form.get('age')

        return f"Salom {name}, siz {age} yoshdasiz"
    
    return render_template("register.html")


if __name__ == '__main__':
    app.run(debug=True)
