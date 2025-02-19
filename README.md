# Loan Default Prediction:
# Background
Aggregate consumer debt has been increasing steadily since the 2008-09 financial crisis, According to US Bank, total household debt reached a record 17.94 trillion dollars in 2024 posing a potential macroeconomic threat, as household debt increases we would expect to see consumption weaken and a heightened risk of recession. It is within this macroeconomic context that we should consider the importance of supporting consumer credit risk modeling and therefore probability of default (PD) modeling.

# Data Description

-The dataset leveraged for this analysis is the 'Loan Default Prediction' dataset found here: https://www.kaggle.com/datasets/nikhil1e9/loan-default

-Dependent Variable: 

    -Loan Default Rate: indicator for whether or not consumer defaulted on loan

-Independent Variables: 

    -Age: consumer age

    -Income: consumer income

    -Loan Amount: outstanding balance on loan

    -Credit Score: consumer credit score

    -Months Employed: work experience/employment history

    -Number of Credit Lines: number of open credit lines

    -Interest Rate: interest rate on loan

    -Loan Term: length of loan term/number of months to maturity

    -Debt-to-Income Ratio: ratio of consumer debt to gross income, indicator of whether or not a consumer is "overburdened"

    -Education: education level/category

    -Employment Status: status of consumer employment

    -Marital Status: consumer marital status

    -Mortgage: indicator for whether or not consumer has mortgage

    -Dependents: indicator for whether or not consumer has dependents

    -Loan Purpose: type of loan

    -Cosigner: indicator for whether or not the loan has a cosigner

# Exploratory Data Analysis

Important Observations

-The Average DTI Ratio in the sample is 0.5 (50%), this is substantially higher than the average DTI Ratio of 0.115 (11.5%) in the United States and the generally acceptable ("good") DTI Ratio of 0.35 (35%) according to US Bank

-The Average Age in the sample is about 43 years old, which is higher than the average age in the United States of about 38 years old according to the US Census.

-The Average loan amount is $127,579 which might be considered a bit high for a single consumer loan but, we should keep in mind that business loans are included in the sample as well and may be skewing the distribution.

-The loan default variable is subject to class imbalance and needs to be adjusted using resamplihg in order to reduce bias in our prediction (in other words, if we don't resample we run the risk of our model predicting non-defaults (majority class) better than defaults (minority class))

-We should encode our categorical independent variables to facilitate model training

-We should scale our numeric independent variables to account for different units/magnitude of units (ex. age in years vs income in dollars) to prevent biased weighting towards variables with larger units/magnitude

# Modeling and Selection




        
