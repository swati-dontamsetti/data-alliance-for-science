# Education and Living Conditions
**Group Members:** Swati Dontamsetti (Project Manager), Tyler Neher, Todd M, Steven Kilawattie

## Background
We were interested in seeing whether a location's High School graduation rate is affected by other living conditions such as the number of children a woman has or life expectancy.

Initially we tried to do this solely in the United States, and to compare state by state data, or even district by district data within one state. Unfortunately finding that data was difficult. The one instance in which we found the data on https://www.data.gov/, the data was 10 years old and the formatting was completely inconsistent. It would take too long to clean the data.

In the end we found "The State of the World’s Children 2019 Statistical Tables" on UNICEF at https://data.unicef.org/resources/dataset/sowc-2019-statistical-tables/.

This thorough and detailed data allowed us to continue with out object of seeing whether a myriad of living conditions affected a locations high school graduation data. Instead of focusing on the US or on a specific state, we focused bigger on country by country basis. And because we graduation rates were separated by male and female, we are able to see if these different living conditions affected men and women differently.

## Motivation:
Education is commonly touted as the great equalizer of people. Education is meant to help people out of poverty. And the more educated a country is, the better the living conditions are supposed to be in that country. We wanted to see if the data supported these claims. Can we demonstrate actual relationships between how educated a country was and whether or not the people had access to drinking water.

Our hypothesis was that education does affect a country's living conditions.

## Questions asked:
* What 10 countries have the highest graduation rates?
* Do people move to OR move out of a country based on the country's graduation rate?
* Does breastfeeding a child reflect on the country's graduation rate?
* Does life expectancy increase as a country's graduation rate increases?
* If a country's young are malnutritioned, does this reflect on the country's graduation rate?
* Do women have more or less children as the country's graduation rate gets higher?
* Does having access to drinking water affect a country's graduation rates?
* Does having access to sanitation services affect a country's graduation rates?

Each group member took two questions and represented that data with either bar graphs or scatter plot with a linear regression line. The Jupyter Notebook (and the individual data folder) shows who took which questions.

# Results
## Top 10 Countries
![Top10Male](https://github.com/swati-dontamsetti/data-alliance-for-science/blob/master/Images/top%2010%20male.png?raw=true) ![Top10Female](https://github.com/swati-dontamsetti/data-alliance-for-science/blob/master/Images/top%2010%20female.png?raw=true)

**Conclusion:** Based of the fact that North Korea is the top country at 100%, we expect that not all countries are reporting honestly. Or if a country lets on top performing or the wealthies students attend high school could skew the data as well.

## Net Migration
![1](https://github.com/swati-dontamsetti/data-alliance-for-science/blob/master/Images/Male%20Upper%20Ed%20Completion%20vs%20Rate%20of%20Immigration.png?raw=true)![2](https://github.com/swati-dontamsetti/data-alliance-for-science/blob/master/Images/Female%20Upper%20Ed%20Completion%20vs%20Rate%20of%20Immigration.png?raw=true)

**Conclusion:** Most data points are clustered around 0 regardless of graduation rate.

## Life Expectancy
![3](https://github.com/swati-dontamsetti/data-alliance-for-science/blob/master/Images/male%20vs%20life.png?raw=true)![4](https://github.com/swati-dontamsetti/data-alliance-for-science/blob/master/Images/female%20vs%20life.png?raw=true)

**Conclusion:** Not a perfect relationship, but a country's life expectancy does seem to increase when more of the country is educated.

## Breastfeeding
![5](https://github.com/swati-dontamsetti/data-alliance-for-science/blob/master/Images/male%20vs%20breastfeeding.png?raw=true)![6](https://github.com/swati-dontamsetti/data-alliance-for-science/blob/master/Images/female%20vs%20breastfeeding.png?raw=true)

**Conclusion:** There does not seem to be any relationship between breastfeeding early on and a country's graduation rate.

## Number of Live Births per Woman
![7](https://github.com/swati-dontamsetti/data-alliance-for-science/blob/master/Images/male%20rate%20vs%20fertility.png?raw=true)![8](https://github.com/swati-dontamsetti/data-alliance-for-science/blob/master/Images/female%20rate%20vs%20fertility.png?raw=true)

**Conclusion:** Not a perfect relationship, but it does seem that the higher a country's graduation rate the fewer times a woman gives birth.

## Malnutrition among Preschool-aged children
![9](https://github.com/swati-dontamsetti/data-alliance-for-science/blob/master/Images/male%20rate%20vs%20malnutrition.png?raw=true)![10](https://github.com/swati-dontamsetti/data-alliance-for-science/blob/master/Images/female%20rate%20vs%20malnutrition.png?raw=true)

**Conclusion:** Not a perfect relationship, but it does seem that the higher a country's graduation rate the smaller the malnutrition rate amongst children. One issue with the data could be that we are comparing different children - the students who are graduating are not the same who are malnutritioned based on the time period.

## Drinking Water Availability at Home
![11](https://github.com/swati-dontamsetti/data-alliance-for-science/blob/master/Images/male%20rate%20vs%20water.png?raw=true)![12](https://github.com/swati-dontamsetti/data-alliance-for-science/blob/master/Images/female%20rate%20vs%20water.png?raw=true)

**Conclusion:** Not a perfect relationship, but it does seem that the higher country's graduation rate the more likely it is that citizens have access to drinking water at home.

## Sanitation Services Available at Home
![13](https://github.com/swati-dontamsetti/data-alliance-for-science/blob/master/Images/male%20completion%20vs%20sanitation.png?raw=true)![14](https://github.com/swati-dontamsetti/data-alliance-for-science/blob/master/Images/female%20completion%20vs%20sanitation.png?raw=true)

**Conclusion:** There does seem to be a relationship between a country's graduation rate and whether or not kids have access to sanitation services at home.

## Summary
Life Expectancy, Live Births per Woman, Sanitation Services seems to be most affect by high school graduation rates. A country's people live longer the more educated they. A country's women have fewer children when they are more educated. And sanitation services do affect a country's education rate. This makes sense especially for women because of the reports from all over the world of girls who have to drop out of school because they don't have access to pads.
