#WHITE TEAM CHALLENGE - Linier Regression on AirBnB data

#Nashville + Asheville AirBnB Data-----------------

#Import Library()
library(dplyr)

#Read in csv file as dataframe
AirBnBListdf <- read.csv("unknown_all_zip_ratings.csv")

#Inspect the result
#head(AirBnBdf)

#Find feature v. overall score

#Perform linear regression using lm() function. 
#Pass 6 variables: rating_score, acciracy_review, communication_review, beds, price, bathrooms
#Add the "AirBnBListdf" dataframe as the data parameter
lm(formula = rating_score ~ accuracry_review + communication_review + beds + price + bathrooms, data= AirBnBListdf)

#Using summary() determine the p-value and r-squared value
summary(lm(formula = rating_score ~ accuracry_review + communication_review + beds + price + bathrooms, data= AirBnBListdf)
)


