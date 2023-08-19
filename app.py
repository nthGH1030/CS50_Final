from flask import Flask, flash, redirect, render_template, request, session

app = Flask(__name__)

@app.route('/')
@app.route("/helloworld/")
def index():
    return render_template('hello.html')



if __name__ == "__main__":
    app.run(debug=True)