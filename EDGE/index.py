from flask import Flask, render_template

app = Flask(__name__)

# Creating simple Routes 
@app.route('/test')
def test():
    return "Home Page"

@app.route('/test/about/')
def about_test():
    return "About Page"
    
@app.route('/edu')
def edu():
    return render_template("edu.html")

@app.route('/eco')
def eco():
    return render_template("eco.html")    

@app.route('/soc')
def soc():
    return render_template("soc.html")     

# Routes to Render Something
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about', strict_slashes=False)
def about():
    return render_template("about.html")

@app.route('/doc', strict_slashes=False)
def doc():
    return render_template("doc.html")

@app.route('/juego', strict_slashes=False)
def juego():
    return render_template("juego.html")



# Make sure this we are executing this file
if __name__ == '__main__':
    app.run(debug=True)
