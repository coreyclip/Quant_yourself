# -*- coding: utf-8 -*-
"""
In python, text that is either between """ """ or starts with # 
are not interpretted as commands in Python. I'll use this feature to give
instructions as we edit this base script for our own purposes 

first we need to get our data into python

To do so we need to call our "filepath" to the csv sheet we just downloaded
to the variable health_file 

for mac it should be something like this:
    "/Users/coreyclip/quant_yourself/health_data.csv"
Windows:
    "H:/

"""
import pandas as pd
import numpy as np

health_file = "/Users/coreyclip/quant_yourself/Health Data_2.csv"

df = pd.read_csv(health_file)


df.info()

target = "Weight (lb)"  

predictors = ["Dietary Calories (cal)", "Steps (count)"]

train_df = df[predictors]

#lag Y variable, because our weight in the morning is function of what we did yesterday
last = df[-1:][target] #save the last value
Y = df[target].shift(1).dropna().values #shift removes the last value 
Y = np.append(Y,last) #attach the last value back onto the Y array

#impute missing values
X = df[[predictors]].round(decimals=2)
from sklearn.preprocessing import Imputer
imp = Imputer(missing_values=0,strategy='mean',axis=0)
X = imp.fit_transform(X)



from sklearn.linear_model import LinearRegression

ols = LinearRegression(fit_intercept=True,normalize=False)

ols.fit(X,Y)

from reporter import report

inputs_json = {
        "Y":target,
        "X":predictors
        }

report(ols,inputs_json)
