# -*- coding: utf-8 -*-
"""
In python, text that is either between """ """ or starts with # 
are not interpretted as commands in Python. I'll use this feature to give
instructions as we edit this base script for our own purposes 

first we need to get our data into python

To do so we need to call our "filepath" to the csv sheet we just downloaded
to the variable health_file 

for mac it should be something like this:
    "/Users/coreyclip/Desktop/Quant_yourself/health_data.csv"
Windows:
    "C:/Desktop/Quant_yourself-master/health data.csv"

"""
import pandas as pd
import numpy as np

health_file = #input the filepath to your health data here
df = pd.read_csv(health_file)


print("-"*15 + "information on your dataset" + "-"*15)
df.info()
print("-"*15 + "first 5 rows of the data" + "-"*15)
print(df.head(5))

'''
you can adjust what our machine learning model tries to predict by changing
the target variable bellow. In Python a variable is set up like this x = 2. 
In that case when you type in x Python will interpret it as 2, just like in 
mathematics. For our purposes the variable "target" should be set to the 
health phenomena we want to predict based off of the predictors we'll set up 
next. As a default I have selected Weight. It's important to note that it's vital
that you type inbetween the " " the name of the column *exactly* how it appears 
in the csv file containing your health data from QS Access 
'''
target = "Weight (lb)"  

'''
Add or remove the names of columns from the list bellow ( the phrases in 
between the [ ]) make sure each column name is surrounded with " " and are 
seperated by commas. Or else the program will break..
'''
predictors = ["Dietary Calories (cal)", "Steps (count)"] 

#lag Y variable, because our weight in the morning is function of what we did yesterday
missing = df.loc[1][target] #save the first value
Y = df[target].shift(-1).dropna().values #shift removes the last value 
Y = np.append(missing,Y) #attach the last value back onto the Y array

#impute missing values
X = df[predictors]
from sklearn.preprocessing import Imputer
imp = Imputer(missing_values=0,strategy='mean',axis=0)
X = imp.fit_transform(X)


#traing the machine learning model
from sklearn.linear_model import LinearRegression
ols = LinearRegression(fit_intercept=True,normalize=False)

ols.fit(X,Y)

#reporting from the model
coefs = ols.coef_
inter = round(ols.intercept_,3)
print("-"*15 + "model intercept" + "-"*15)
print("all else constant the model predicts that {t} should be {i}".format(
        t=target, i=inter))

print("-"*15 + "predictor variables coefficients" + "-"*15)
for i,var in enumerate(predictors):
    print("for one unit increase in {v} your model predicts:".format(v=var))
    print("a {c} change in {t}".format(c=coefs[i], t=target))

predict = input("Do you want to use your model to predict if you are getting heavier? (y/n) \n")

if predict == 'y':
    features = []
    for i in predictors:
        print("input today's {i}".format(i=i))
        features.append(input())
    pred_array = pd.Series(features, dtype=float)
    prediction = ols.predict(pred_array.values.reshape(1,-1))
    print("based off of the information provided {t} will be {p}".format(
            t=target, p=prediction))
    
    