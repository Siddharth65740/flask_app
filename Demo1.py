from flask import Flask
app=Flask(__name__)
@app.route("/")
@app.route("/home")
def Home():
    return "Hello You Have Entered Into Home"
@app.route("/about")
def About():
    return "Hello You Have Entered Into About"
if __name__== '__main__':
    app.run(debug=True)

