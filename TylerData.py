# tyler: countries education rate vs malnutrition rate AND 
# countries education rate vs fertility (# of children per woman)
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
from scipy.stats import linregress

edu_df = pd.read_csv('Clean Education.csv')
nut_df = pd.read_csv('Clean School Aged Nutrition.csv')
demog_df = pd.read_csv('Cleaned Demographics.csv')

# merge
tylerData1 = pd.merge(edu_df, nut_df)
tylerDataComplete = pd.merge(tylerData1, demog_df)

# print column names to identify the required ones
tylerDataComplete.columns

# remove "-"s
tylerDataComplete['Total fertility  (live births per woman) 2018'] = tylerDataComplete['Total fertility  (live births per woman) 2018'].apply(lambda x: x.replace('−',''))
tylerDataComplete['Completion rate 2012–2018, Upper secondary education, male'] = tylerDataComplete['Completion rate 2012–2018, Upper secondary education, male'].apply(lambda x: x.replace('−',''))
tylerDataComplete['Completion rate 2012–2018, Upper secondary education, female'] = tylerDataComplete['Completion rate 2012–2018, Upper secondary education, female'].apply(lambda x: x.replace('-',''))

# choose specific columns
tylerDataSpecific = tylerDataComplete.iloc[:, [13, 14, 23, 41]]

# save data frame as csv so we can remove NAs
tylerDataSpecific.to_csv("Education and Fertility.csv", encoding='utf-8', index=False)

# import merged and cleaned data
tylerDS = pd.read_csv("Education and Fertility.csv")

#drop blank rows
tylerDS = tylerDS.dropna(how="any")

# print new data
tylerDS

# identify variables for easier plotting
male = tylerDS['Completion rate 2012–2018, Upper secondary education, male']
female = tylerDS['Completion rate 2012–2018, Upper secondary education, female'].astype(float)
fertility = tylerDS['Total fertility  (live births per woman) 2018']
malnutrition = tylerDS['Malnutrition among preschool-aged children (0–4 years of age) 2013–2018*: Stunted (%) (moderate and severe): all children'].astype(float)

# scatter plot of male complete rate vs fertility rates
(slope, intercept, rvalue, pvalue, stderr) = linregress(male,fertility)
regress_values = male * slope + intercept
line_eq = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))
plt.scatter(male, fertility)
plt.plot(male,regress_values,"r-")
plt.annotate(line_eq,(50,6),fontsize=15,color="red")
plt.title("Male School Completion Rate vs Fertility Rates")
plt.xlabel("Male High School Complete Rates (%)")
plt.ylabel("Live Births per Woman")
print(f"The r-squared is: {rvalue}")
plt.savefig("male rate vs fertility")

# scatter plot of female complete rate vs fertility rates
(slope, intercept, rvalue, pvalue, stderr) = linregress(female, fertility)
regress_values = female * slope + intercept
line_eq = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))
plt.scatter(female, fertility)
plt.plot(female,regress_values,"r-")
plt.annotate(line_eq,(50,6),fontsize=15,color="red")
plt.title("Female School Completion Rate vs Fertility Rates")
plt.xlabel("Female High School Complete Rates (%)")
plt.ylabel("Live Births per Woman")
print(f"The r-squared is: {rvalue}")
plt.savefig("female rate vs fertility")

# scatter plot of male complete rate vs malnutrition
(slope, intercept, rvalue, pvalue, stderr) = linregress(male,malnutrition)
regress_values = male * slope + intercept
line_eq = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))
plt.scatter(male, malnutrition)
plt.plot(male,regress_values,"r-")
plt.annotate(line_eq,(50,38),fontsize=15,color="red")
plt.title("Male School Completion Rate vs Malnutrition Rates")
plt.xlabel("Male High School Complete Rates (%)")
plt.ylabel("Malnutrition among preschool-aged children (%)")
print(f"The r-squared is: {rvalue}")
plt.savefig("male rate vs malnutrition")

# scatter plot of female complete rate vs malnutrition
(slope, intercept, rvalue, pvalue, stderr) = linregress(female,malnutrition)
regress_values = female * slope + intercept
line_eq = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))
plt.scatter(female, malnutrition)
plt.plot(female,regress_values,"r-")
plt.annotate(line_eq,(50,38),fontsize=15,color="red")
plt.title("Female School Completion Rate vs Malnutrition Rates")
plt.xlabel("Female High School Complete Rates (%)")
plt.ylabel("Malnutrition among preschool-aged children (%)")
print(f"The r-squared is: {rvalue}")
plt.savefig("female rate vs malnutrition")