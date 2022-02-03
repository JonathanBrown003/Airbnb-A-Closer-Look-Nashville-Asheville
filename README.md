# Airbnb, A Closer Look: Nashville & Asheville

### Project Overview
Analyzing the Nashville and Asheville short-term rental market using Airbnb listings data

Nashville, TN and Asheville, NC are magnets for tourists in their own unique ways. As a result, Airbnb has many offerings to suit tourists flocking to these destinations. 

The objective of this analysis is to explore the most statistically-significant characteristics related to rating, reviews, and pricing. This topic was selected to analyze the Airbnb offerings of these two tourist-heavy cities to look for similarities, differences, and any correlations the data analysis can uncover. 

<img src=https://github.com/tutran90/White-/blob/5feb5bb640dbc5694c8ab2c60759fc923a680ed6/Resources/nashville-word-cloud.jpeg width="400" height="400"> <img src=https://github.com/tutran90/White-/blob/5feb5bb640dbc5694c8ab2c60759fc923a680ed6/Resources/asheville-word-cloud.jpeg width="400" height="400">

### Sources of Data
Our data sources were pulled from insideairbnb.com [here](http://insideairbnb.com/get-the-data.html). These datasets have a diverse set of features in which to work with for this project. The data contained within these datasets are mirrors of each other with 74 features each so a thorough, like for like comparison can be done. The Nashville dataset has nearly 6,400 listings to analyze while the Asheville dataset has just over 2,600 listings. 

The Nashville dataset can be accessed ![here](https://github.com/tutran90/White-/blob/5feb5bb640dbc5694c8ab2c60759fc923a680ed6/listings.csv) for viewing while the Asheville dataset can be accessed ![here](https://github.com/tutran90/White-/blob/5feb5bb640dbc5694c8ab2c60759fc923a680ed6/Asheville_listings.csv). 

#### Notable Features

- Description
- Neighborhood Overview
- Host Response Time
- Host Response Rate
- Host Listings Count
- Neighbourhood Cleansed (District # corresponds to neighborhood or zip code)
- Latitude
- Longitude
- Bedrooms
- Bathrooms
- Accommodates (# of guests)
- Price
- Number of Reviews
- Review Scores Rating
- Review Scores Accuracy
- Review Scores Cleanliness
- Review Scores Checkin
- Review Scores Communication
- Review Scores Location
- Review Scores Value
- Reviews Per Month

### Questions to answer
1) Are there certain zip codes that have noticeably higher ratings than other zip codes?
2) Do the number of reviews per month (good indicator of tenancy) correlate with high ratings for Airbnb units?
3) Do certain short-term rental characteristics fare better in the short-term rental market? 
4) What characteristics are needed for a successful (high ranking) rental property? 
5) Does the host response rate correlate with higher overall ratings?
6) What are the most common key words/phrases used in Airbnb host descriptions? Are these descriptors telling in what would be successful in a rental property? 
7) Is there a correlation between host listing count and superhost? 

### Communication Protocols
The team has been meeting twice per week during Zoom class time to jointly work on this project. We discuss deliverables and timelines for completion to ensure everyone is on track with their portion of the project. We use the group Slack channel to communicate between and during meetings as well as on an ad-hoc basis. 

### Database
Our team will be using PostgreSQL to create a database then link from it to feed our machine learning model. 

### Machine Learning Model
Our team will be using supervised machine learning (Logistic Regression) to suggest listings based on pre-specified criteria such as rating scores, pricing, and host communication and response rate.

### Data Visualization
We'll also be using Tableau to create an interactive dashboard to tell our story of the data.

![](https://github.com/tutran90/White-/blob/58e5ed1ee2dc51c98cca09e47500b88af00f2b1b/Resources/Nash_Airbnb_District.PNG)
