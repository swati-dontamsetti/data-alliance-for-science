# import pandas
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
from scipy.stats import linregress

# identify files
education = "Clean Education.csv"
water_sanitation = "Clean WASH.csv"

# read csv
education_df = pd.read_csv(education)
water_san_df = pd.read_csv(water_sanitation)

# print education data
education_df

# print water and sanitation data
water_san_df

# merge the two data tables
education_wash = pd.merge(education_df, water_san_df)

# take out the "−" inside the columns
education_wash['Completion rate 2012–2018, Upper secondary education, male'] = education_wash['Completion rate 2012–2018, Upper secondary education, male'].apply(lambda x: x.replace('−',''))
education_wash['Completion rate 2012–2018, Upper secondary education, female'] = education_wash['Completion rate 2012–2018, Upper secondary education, female'].apply(lambda x: x.replace('−',''))

# identify specific columns necessary
upper_ed_wash = education_wash.iloc[:, [0,13,14,23,26]]

# save data frame as csv
upper_ed_wash.to_csv("Education completion rate and Household WASH.csv", encoding='utf-8', index=False)

# import merged and cleaned data
u_ed_wash = pd.read_csv("Education completion rate and Household WASH.csv")

#drop blank rows
u_ed_wash = u_ed_wash.dropna(how="any")

# print new data
u_ed_wash

# label each column
male = u_ed_wash["Completion rate 2012–2018, Upper secondary education, male"]
female = u_ed_wash["Completion rate 2012–2018, Upper secondary education, female"]
water = u_ed_wash["Households: At least basic drinking water services (%) 2017: Total"]
sanitation = u_ed_wash["Households: At least basic sanitation services (%) 2017: total"]

# scatter plot of male complete rate vs water availability
(slope, intercept, rvalue, pvalue, stderr) = linregress(male,water)
regress_values = male * slope + intercept
line_eq = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))
plt.scatter(male, water)
plt.plot(male,regress_values,"r-")
plt.annotate(line_eq,(50,60),fontsize=15,color="red")
plt.title("Male School Completion Rate vs Water Availability")
plt.xlabel("Male High School Complete Rates (%)")
plt.ylabel("Availabilty of Drinking Water at Home (%)")
print(f"The r-squared is: {rvalue}")
plt.savefig("male rate vs water")

# scatter plot of female complete rate vs water availability
(slope, intercept, rvalue, pvalue, stderr) = linregress(female,water)
regress_values = female * slope + intercept
line_eq = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))
plt.scatter(female, water)
plt.plot(female,regress_values,"r-")
plt.annotate(line_eq,(50,60),fontsize=15,color="red")
plt.title("Female School Completion Rate vs Water Availability")
plt.xlabel("Female High School Complete Rates (%)")
plt.ylabel("Availabilty of Drinking Water at Home (%)")
print(f"The r-squared is: {rvalue}")
plt.savefig("female rate vs water")

# scatter plot of male complete rate vs sanitation services
(slope, intercept, rvalue, pvalue, stderr) = linregress(male,sanitation)
regress_values = male * slope + intercept
line_eq = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))
plt.scatter(male, sanitation)
plt.plot(male,regress_values,"r-")
plt.annotate(line_eq,(50,45),fontsize=15,color="red")
plt.title("Male School Completion Rate vs Sanitation Services")
plt.xlabel("Male High School Complete Rates (%)")
plt.ylabel("Availabilty of Sanitation Services at Home (%)")
print(f"The r-squared is: {rvalue}")
plt.savefig("male completion vs sanitation")

# scatter plot of female complete rate vs sanitation services
(slope, intercept, rvalue, pvalue, stderr) = linregress(female,sanitation)
regress_values = female * slope + intercept
line_eq = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))
plt.scatter(female, sanitation)
plt.plot(female,regress_values,"r-")
plt.annotate(line_eq,(50,45),fontsize=15,color="red")
plt.title("Female School Completion Rate vs Sanitation Services")
plt.xlabel("Female High School Complete Rates (%)")
plt.ylabel("Availabilty of Sanitation Services at Home (%)")
print(f"The r-squared is: {rvalue}")
plt.savefig("female completion vs sanitation")