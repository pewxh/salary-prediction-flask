from flask import Flask, render_template, request
import joblib

app = Flask("SalaryPrediction")

model = joblib.load('../MODEL/model.x')

@app.route("/")
def root():
    return render_template('index.html')
    
@app.route('/predict',methods=['GET'])
def predict():
    name = request.args.get('name')
    exp = request.args.get('exp')
    sal = str(model.predict([[exp]]))
    sal = round(float(sal[2:-2]))
    return render_template('predict.html',data=[name,sal])

@app.errorhandler(404)
def not_found_error(error):
    return render_template('error.html'),404
 
#Handling error 500 and displaying relevant web page
@app.errorhandler(500)
def internal_error(error):
    return render_template('error.html'),500
app.run(host="0.0.0.0")
