import pandas as pd

df = pd.read_csv("patient_priority.csv")

df = df.drop("Unnamed: 0", axis=1)#some weird value in the data so we removed it
df = df.dropna()#few values didnt have what we needed, triage, gender etc. so drop that

X = df.drop("triage", axis=1)#contains all columns(due to axis) other than triage since we working on triage with y
y = df["triage"]

X = pd.get_dummies(X)#highly important, converts word based entries to columns containing 1 and 0 value for easier use. pdb/pcm example

from sklearn.model_selection import train_test_split#scikitlearn importing test traion split. which does exactly that, splita the data for training and testing

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)#the function returns 4 values to be stores,the arguments is the input x and output y, rest are addons  0.2 is 20% for test, 80% for train, random state is defined for controlled tests, like minecraft seed


from sklearn.tree import DecisionTreeClassifier#dont ask, its a tree, you gotta learn trees in depth to know how it does what it does. much like inbuilt sort, it sorts the thing, but if you wanna learn how it sorts you need to know sorting techniques

model = DecisionTreeClassifier(max_depth=5, min_samples_split=20,class_weight="balanced")#we put the decision maker in this, put limit on its depth if-else, increases generality and might lead to inaccurate stuff but given that model is too good to be real so we add a lil bit of realism, min split is increasing the nubmer needed to make an actual rule   

model.fit(X_train, y_train)#giving the model all the training info. inputs-outputs

import joblib#to save the model so it dont need to train every time we use it

joblib.dump(model, "model.pkl")#dump like in file handlers, dumps all model's learnt patterns from training into a file to be used