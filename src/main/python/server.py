from flask import Flask, render_template

app = Flask(__name__, template_folder="../resources/templates", static_folder="../resources/static")

@app.route('/')
def comming_soon():
   return render_template("comming_soon.html")

@app.route('/home')
def home():
   return render_template("home.html")

@app.route('/contact')
def contact():
   return render_template("contact.html")

if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=True, port=5000)