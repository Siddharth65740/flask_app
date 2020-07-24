from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
@app.route("/home")
def Home():
    return render_template("home.html")
@app.route("/about")
def About():
    return render_template("about2.html")
if __name__=='__main__':
    app.run(debug=True)