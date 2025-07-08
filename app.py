from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def submit():
    name = str(request.form.get('name'))
    email = str(request.form.get('email'))
    out="Received data: Name- "+name+", E-mail- "+email
    print(out)
    return render_template('index.html',out =out )
if __name__=="__main__":
    app.run(debug=True)