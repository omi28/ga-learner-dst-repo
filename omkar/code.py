# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
#New record


#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
data.shape
cenus=np.concatenate((new_record,data),axis=0)
cenus.shape
print(cenus)
age=cenus[:,0]
max_age=age.max()
print(max_age)
min_age=age.min()
mean_age=np.mean(age)
age_std=np.std(age)
race=cenus[:,2]
print(race)
race_0=(race==0)
len_0=len(race[race_0])
print(len_0)
race_1=(race==1)
len_1=len(race[race_1])
race_2=(race==2)
race_3=(race==3)
race_4=(race==4)
len_2=len(race[race_2])
len_3=len(race[race_3])
len_4=len(race[race_4])
minority_race=3
print(minority_race)

senior_citizen=(age>60)
working_hour_sum=sum(cenus[:,6][senior_citizen])
print(working_hour_sum)
senior_citizen_len=len(age[senior_citizen])
avg_working_hours=working_hour_sum/senior_citizen_len
avg_working_hours=round(avg_working_hours,2)

education_num=cenus[:,1]
print(education_num)
high=education_num>10
#high=education_num[high]
print(high)
low=education_num<=10
#low=education_num[low]
print(low)
INCOME=cenus[:,7][high]
print(INCOME)
print(np.mean(INCOME))
avg_pay_high=round(np.mean(INCOME),2)
print(avg_pay_high)
LOW_AVG=cenus[:,7][low]
avg_pay_low=round(np.mean(LOW_AVG),2)
print(avg_pay_low)


#Code starts here




