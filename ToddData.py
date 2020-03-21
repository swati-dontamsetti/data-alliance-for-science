# Todd: Top 10 Countries for Education Men and Women
# and Education rate vs Net Migration
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
from scipy.stats import linregress

#Assigning a variable to the path each relevant csv file in prep for merge
edu_payload = ("Resources/Clean Education.csv")
migra_payload = ("Resources/Cleaned Demographics.csv")

education_df = pd.read_csv(edu_payload)
migration_df = pd.read_csv(migra_payload)

edumi_df = pd.merge(education_df, migration_df, how="outer", on=["countries and areas"])

#Taking essential columns
wshedmi = edumi_df[['countries and areas','Completion rate 2012–2018, Upper secondary education, male','Completion rate 2012–2018, Upper secondary education, female', 'Net migration rate (per 1,000 population) 2015−2020']]
wshedmi

# get rid of "-" that are supposed to be NA
wshedmi.loc[:,('Completion rate 2012–2018, Upper secondary education, male')] = wshedmi['Completion rate 2012–2018, Upper secondary education, male'].apply(lambda x: x.replace('−',''))
wshedmi.loc[:,('Completion rate 2012–2018, Upper secondary education, female')] = wshedmi['Completion rate 2012–2018, Upper secondary education, female'].apply(lambda x: x.replace('−',''))
wshedmi.loc[:,('Net migration rate (per 1,000 population) 2015−2020')] = wshedmi['Net migration rate (per 1,000 population) 2015−2020'].apply(lambda x: x.replace('−',''))

# chech it was taken out
wshedmi

# save as csv so that we can drop the NAs
wshedmi.to_csv("Output_Data/Education and Migration.csv", encoding='utf-8', index=False)

# import merged and cleaned data
ed_mig = pd.read_csv("Output_Data/Education and Migration.csv")

#drop blank rows
ed_mig = ed_mig.dropna(how="any")

# print new data
ed_mig

# Map out Top 10 Best Contries for Ed Completion
# sort male and female completion rates, and reduce to top 10
sorted_m_ed = ed_mig.sort_values("Completion rate 2012–2018, Upper secondary education, male", ascending = False)
top_ten_m = sorted_m_ed.head(10)
sorted_f_ed = ed_mig.sort_values("Completion rate 2012–2018, Upper secondary education, female", ascending = False)
top_ten_f = sorted_f_ed.head(10)

# bar plot of top 10 countries for male completion rate
top_ten_m.plot.bar(x='countries and areas', y='Completion rate 2012–2018, Upper secondary education, male', rot=90, title="Top 10 Countries for Male High School Completion", legend=False)

# bar plot of top 10 countries for female completion rate
top_ten_f.plot.bar(x='countries and areas', y='Completion rate 2012–2018, Upper secondary education, female', rot=90, title="Top 10 Countries for Female High School Completion", legend=False)

uedm = ed_mig['Completion rate 2012–2018, Upper secondary education, male']
uedf = ed_mig['Completion rate 2012–2018, Upper secondary education, female']
rofm = ed_mig['Net migration rate (per 1,000 population) 2015−2020']
plt.scatter(uedm,rofm, color="blue", label = ("Male Grad Rate vs Migration Rate"));
plt.xlabel('Male Graduation Upper Sec.Ed',fontsize=14)
plt.ylabel('Net Migration Rate',fontsize=14);

(slope, intercept, rvalue, pvalue, stderr) = linregress(uedm,rofm)
regress_values = uedm * slope + intercept
line_eq = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))
plt.scatter(uedm, rofm)
plt.plot(uedm,regress_values,"r-")
plt.annotate(line_eq,(50,-5),fontsize=15,color="red")
plt.xticks(rotation=45)
plt.title("Male School Completion Rate vs Rate of Immigration")
plt.xlabel("Upper Ed Male Grad Completion Rates")
plt.ylabel("Rate of Immigration")
print(f"The r-squared is: {rvalue}")
plt.savefig('Images/Male Upper Ed Completion vs Rate of Immigration.png')

plt.scatter(uedf,rofm, color="green", label = ("Female Grad Rate vs Migration Rate"));
plt.xlabel('Female Graduation Upper Sec.Ed',fontsize=14)
plt.ylabel('Net Migration Rate',fontsize=14);

(slope, intercept, rvalue, pvalue, stderr) = linregress(uedf,rofm)
regress_values = uedf * slope + intercept
line_eq = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))
plt.scatter(uedf, rofm)
plt.plot(uedf,regress_values,"r-")
plt.annotate(line_eq,(50,-5),fontsize=15,color="red")
plt.xticks(rotation=45)
plt.title("Female School Completion Rate vs Rate of Immigration")
plt.xlabel("Upper Ed Female Grad Completion Rates")
plt.ylabel("Rate of Immigration")
print(f"The r-squared is: {rvalue}")
plt.savefig('Images/Female Upper Ed Completion vs Rate of Immigration.png')