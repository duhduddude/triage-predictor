from flask import Flask, render_template, request#flask main web page,render is for html, request is whole module for just that
from backend import predict_triage

app = Flask(__name__) #just important. dont question it. depth of flask. its like int main and psvm for java

@app.route("/")#when the user opens te site take them to the enxt line of this code
def home():#home page request
    return render_template("index.html")#show index.html


@app.route("/predict", methods=["POST"])#when form is submitted , it comes from html's form action, uses post cause it be postin
def predict():
    data = {
        "age": [int(request.form["age"])],
        "gender": [int(request.form["gender"])],
        "chest pain type": [int(request.form["chest_pain"])],
        "blood pressure": [int(request.form["bp"])],
        "cholesterol": [int(request.form["cholesterol"])],
        "max heart rate": [int(request.form["max_hr"])],
        "exercise angina": [int(request.form["angina"])],
        "plasma glucose": [int(request.form["glucose"])],
        "skin_thickness": [int(request.form["skin"])],
        "insulin": [int(request.form["insulin"])],
        "bmi": [float(request.form["bmi"])],
        "diabetes_pedigree": [float(request.form["pedigree"])],
        "hypertension": [int(request.form["hypertension"])],
        "heart_disease": [int(request.form["heart_disease"])],
        "Residence_type": [request.form["residence"]],
        "smoking_status": [request.form["smoking"]]
    }

    result = predict_triage(data)

    return render_template("index.html", prediction=result)#returns back to the html of index, prediction is an argument variable with the result, html handles it


if __name__ == "__main__":
    app.run(debug=True)#start the ap