# Steve: education rate vs breastfeeding at birth
# and education rate vs life expectancy
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
from scipy.stats import linregress

# identify files
education = "Resources/Clean Education.csv"
life_exp = "Resources/Cleaned Demographics.csv"
breastfeeding = "Resources/Clean Infant Nutrition.csv"

# read csv
education_df = pd.read_csv(education)
life_exp_df = pd.read_csv(life_exp)
breastfeeding_df = pd.read_csv(breastfeeding)

# merge the two data tables
ed_life = pd.merge(education_df, life_exp_df)
ed_b_life = pd.merge(ed_life, breastfeeding_df)

# print combines data frame
ed_b_life

# print column names to identify the required ones
ed_b_life.columns

# choose specific columns
specific_data = ed_b_life.iloc[:, [0, 13, 14, 32, 42]]

# confirm that correct columns are chosen
specific_data

# remove "-"s
specific_data['Life expectancy at birth (years): 2018'] = specific_data['Life expectancy at birth (years): 2018'].apply(lambda x: x.replace('−',''))
specific_data['Completion rate 2012–2018, Upper secondary education, male'] = specific_data['Completion rate 2012–2018, Upper secondary education, male'].apply(lambda x: x.replace('−',''))
specific_data['Completion rate 2012–2018, Upper secondary education, female'] = specific_data['Completion rate 2012–2018, Upper secondary education, female'].apply(lambda x: x.replace('-',''))

# save data frame as csv so we can remove NAs
specific_data.to_csv("Output_Data/Education, Breastfeeding and Life Exp.csv", encoding='utf-8', index=False)

# import merged and cleaned data
spec_data = pd.read_csv("Output_Data/Education, Breastfeeding and Life Exp.csv")

#drop blank rows
spec_data = spec_data.dropna(how="any")

# print new data
spec_data

# identify variables for easier plotting
male = spec_data['Completion rate 2012–2018, Upper secondary education, male']
female = spec_data['Completion rate 2012–2018, Upper secondary education, female'].astype(float)
life_exp = spec_data['Life expectancy at birth (years): 2018']
breast_feeding = spec_data['"Infant and Young Child Feeding (0-23 months) 2013–2018*" Early initiation of breastfeeding (%)']

# scatter plot of male complete rate vs life expectancy
(slope, intercept, rvalue, pvalue, stderr) = linregress(male,life_exp)
regress_values = male * slope + intercept
line_eq = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))
plt.scatter(male, life_exp)
plt.plot(male,regress_values,"r-")
plt.annotate(line_eq,(50,60),fontsize=15,color="red")
plt.title("Male School Completion Rate vs Life Expectancy")
plt.xlabel("Male High School Complete Rates (%)")
plt.ylabel("Life Expectancy")
print(f"The r-squared is: {rvalue}")
plt.savefig("Images/male vs life")

# scatter plot of female complete rate vs life expectancy
(slope, intercept, rvalue, pvalue, stderr) = linregress(female,life_exp)
regress_values = female * slope + intercept
line_eq = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))
plt.scatter(female, life_exp)
plt.plot(female,regress_values,"r-")
plt.annotate(line_eq,(50,60),fontsize=15,color="red")
plt.title("Female School Completion Rate vs Life Expectancy")
plt.xlabel("Female High School Complete Rates (%)")
plt.ylabel("Life Expectancy")
print(f"The r-squared is: {rvalue}")
plt.savefig("Images/female vs life")

# scatter plot of male complete rate vs breastfeeding rate
(slope, intercept, rvalue, pvalue, stderr) = linregress(male,breast_feeding)
regress_values = male * slope + intercept
line_eq = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))
plt.scatter(male, breast_feeding)
plt.plot(male,regress_values,"r-")
plt.annotate(line_eq,(50,60),fontsize=15,color="red")
plt.title("Male School Completion Rate vs Breastfeeding at Birth")
plt.xlabel("Male High School Complete Rates (%)")
plt.ylabel("Early Initiation of Breastfeeding (0-23 months) (%)")
print(f"The r-squared is: {rvalue}")
plt.savefig("Images/male vs breastfeeding")

# scatter plot of male complete rate vs breastfeeding rate
(slope, intercept, rvalue, pvalue, stderr) = linregress(female,breast_feeding)
regress_values = female * slope + intercept
line_eq = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))
plt.scatter(female, breast_feeding)
plt.plot(female,regress_values,"r-")
plt.annotate(line_eq,(50,60),fontsize=15,color="red")
plt.title("Female School Completion Rate vs Breastfeeding at Birth")
plt.xlabel("Female High School Complete Rates (%)")
plt.ylabel("Early Initiation of Breastfeeding (0-23 months) (%)")
print(f"The r-squared is: {rvalue}")
plt.savefig("Images/female vs breastfeeding")