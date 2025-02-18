# Loan Default Prediction:
# Background
Aggregate consumer debt has been increasing steadily since the 2008-09 financial crisis, According to US Bank, total household debt reached a record 17.94 trillion dollars in 2024 posing a potential macroeconomic threat, as household debt increases we would expect to see consumption weaken and a heightened risk of recession. It is within this macroeconomic context that we should consider the importance of supporting consumer credit risk modeling and therefore probability of default (PD) modeling.

# Data Description

-The dataset leveraged for this analysis is the 'Loan Default Prediction' dataset found here: https://www.kaggle.com/datasets/nikhil1e9/loan-default

-Target Variable: 

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

The `USDAMARS` package also contains a function called `MARS_Table_Directory` which pulls a data set with details (e.g., slugid, report frequency, and publication date) for all of the USDA Market News reports.

# Examples
Below are some examples for the functions above should be used.

Example 1: Setting your API Key
        
          MARS_API_Key("YOUR API KEY")

Example 2: Retrieving the Table Directory

          Directory <- MARS_Table_Directory()

Example 3: Retrieving a Table/Report

          Report <- MARS_Table_Pull(slugid = 1034)

Example 4: Retrieving a Table/Report with Section and Date

          Report <- MARS_Table_Pull(slugid = 3668, section = "Report Detail", date = "09/30/2024")

# Installation
Currently, the package is only available through GitHub and can be installed using the code below
          
          devtools::install_github("jjustice121/USDAMARS")

Note: You need to install the `devtools` package before you can install the `USDAMARS` package using `install.packages("devtools")`.

