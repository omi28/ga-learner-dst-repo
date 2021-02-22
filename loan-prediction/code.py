# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)
#Let's check which variable is categorical and which one is numerical so that you will get a basic idea about the features of the bank dataset.
categorical_var=bank_data.select_dtypes(include = 'object')
numerical_var=bank_data.select_dtypes(include="number")
#drop the column 
banks=bank_data.drop(["Loan_ID"],axis=1)
banks.isnull().sum()
bank_mode=banks.mode().iloc[0]
bank_mean=banks.mean()
print(bank_mode)
#apply mode
banks.fillna(bank_mode,inplace=True)
banks.isnull().sum()
banks.isnull().sum().values.sum() 

#pivot table
avg_loan_amount=pd.pivot_table(banks,index=["Gender","Married","Self_Employed"],values="LoanAmount",aggfunc="mean")
print(avg_loan_amount['LoanAmount'][1])

#Now let's check the loan amount of an average person based on 'Gender', 'Married', 'Self_Employed'.
loan_approved_se=banks[(banks["Self_Employed"]=="Yes") & (banks["Loan_Status"]=="Y")]["Loan_Status"].count()
loan_approved_nse=banks[(banks["Self_Employed"]=="No") & (banks["Loan_Status"]=="Y")]["Loan_Status"].count()
loan_status=banks["Loan_Status"].count()
percentage_se=(loan_approved_se/loan_status)*100
percentage_nse=(loan_approved_nse/loan_status)*100
#let's check the percentage of loan approved based on a person's employment type.
def mon(months):
    a=months/12
    return a
#apply function is used here
loan_term=banks["Loan_Amount_Term"].apply(mon)
big_loan_term=np.greater_equal(loan_term, 25).count()
print(big_loan_term)
#let's check the average income of an applicant and the average loan given to a person based on their income.
#apply groupby function
loan_groupby=banks.groupby("Loan_Status")[["ApplicantIncome","Credit_History"]]
#check mean and roundoff it by 2 value
mean_values=round(loan_groupby.mean(),2)
mean_values.iloc[1,0]


#Code starts here




