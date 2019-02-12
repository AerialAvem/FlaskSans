from flask import Flask, flash, redirect, render_template, request, session, abort
app = Flask(__name__)
 
@app.route("/")
def hello():
    return "greetings"

@app.route("/sans")
def sans():
    return '''
<html>
    <div class="block1">
        <h1>it's sans</h1>

        <img src="https://i.redd.it/1gf70fvvki521.jpg">
 
    </div>
<html>'''


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)