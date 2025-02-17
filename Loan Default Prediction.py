# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Loan Default Prediction

#Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import kagglehub
import sklearn as sk
import sys
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from imblearn.over_sampling import SMOTE
import seaborn as sns

#Ingest Data#############################################################################################################################################
path = kagglehub.dataset_download("nikhil1e9/loan-default", force_download = True)

Loan_Default = pd.read_csv(path + "\loan_default.csv")


#Exploratory Data Analysis/Data Validation/Sanity Checks#################################################################################################

#get summary statistics
Summary_Stats = Loan_Default.describe()

#check for NA values
Loan_Default.isna().sum()

#check data types for each column
print(Loan_Default.dtypes)

#check for duplicate values
Loan_Default.duplicated().sum()

#Data Wrangling and Visualization########################################################################################################################

#get list of numeric feature/variable names
Num_Features = list(Loan_Default.select_dtypes(include = np.number))

#get list of categorical variables, exclude LoanID by index
Cat_Features = list(Loan_Default.select_dtypes(include = object))[1:8]

#iterate over list of numeric features to get boxplots
def plot_and_show (df,var):
        
    sns.boxplot(x = df[var])

    plt.show()

[plot_and_show(Loan_Default, i) for i in Num_Features]

#encode categorical variables
Loan_Default[Cat_Features] = Loan_Default[Cat_Features].apply(LabelEncoder().fit_transform)

#check for class imbalance in default
sns.countplot(x = Loan_Default['Default'])

plt.show()

#generate correlation matrix
Corr_Matrix = Loan_Default[(Num_Features + Cat_Features)].corr()

#Modeling and Prediction#################################################################################################################################

#Test-Train Split
X = Loan_Default[Num_Features + Cat_Features].drop('Default', axis  = 1)

y = Loan_Default['Default']

X_train, X_test, y_train, y_test = sk.model_selection.train_test_split(X,y, test_size=0.4, random_state=57)

#apply SMOTE to balance default classes
smote = SMOTE(random_state=57)

X_train, y_train = smote.fit_resample(X_train, y_train)

#check for class balance visually
sns.countplot(x = y_train)

plt.show()

#Write function to convert string to class
def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)

#Write function to generate model fit and metrics
def model_fit_and_metrics (classifier):
    
    model = str_to_class(classifier)()

    model_fit = model.fit(X_train, y_train)

    model_pred = model.predict(X_test)

    print(classifier,'Accuracy:',accuracy_score(y_test, model_pred), 'Precision:',precision_score(y_test, model_pred),
          'Recall:',recall_score(y_test, model_pred),'F1 Score:' ,f1_score(y_test, model_pred))

#list of classifiers
Classifiers = ['LogisticRegression','RandomForestClassifier']

#Iterate over list of classifiers
[model_fit_and_metrics(i) for i in Classifiers]

