import joblib
import pandas as pd


model = joblib.load("model.pkl")#load everything over here

def predict_triage(data):

    input_df = pd.DataFrame(data)#getting all our data in tabular format

    input_df = pd.get_dummies(input_df) #converting input text to numerical data to match earlier format, the older one was for training, this is for inputs and the actual backend

    model_columns = model.feature_names_in_#latter is a property, which we use to get the column names and put it into model_columns
    input_df = input_df.reindex(columns=model_columns, fill_value=0)#forces our input responses to get exactly like the one in our model's column names that we got previously, fill_value is a constant argument to put 0 if nothing is provided

    if data["blood pressure"][0] >= 180:#override sequences due to because of data
        return "3 (override: hypertensive crisis)"

    elif data["plasma glucose"][0] >= 200:
        return "2 (override: high glucose)"

    elif data["heart_disease"][0] == 1 and data["age"][0] > 70:
        return "2 (override: high risk patient)"

    else:
        prediction = model.predict(input_df)
        return prediction[0]