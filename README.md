# Airbnb, A Closer Look: Nashville & Asheville

Please see our main code [here.](Main_Analysis.ipynb) Our machine learning code can be accessed [here.](https://github.com/tutran90/Airbnb-A-Closer-Look-Nashville-Asheville/blob/main/ML_AirBNB.ipynb)

Please access our slides [here.](https://docs.google.com/presentation/d/10pbRhsqGu9zStp6knlFmChnecsVGmCRh07Zs_VdRvIk/edit?usp=sharing)

Please see our Tableau dashboard [here](https://public.tableau.com/app/profile/jonathan.brown2419/viz/AirbnbACloserLookNashvilleAsheville/Dashboard1?publish=yes). This dashboard displays graphics for two of our questions: highest-rated neighborhoods and host response rate's correlation to rating. The interactive feature ties to the neighborhood graphic. It allows you to toggle among the ratings scores for the neighborhoods. 

### Project Overview
Analyzing the Nashville and Asheville short-term rental market using Airbnb listings data

Nashville, TN and Asheville, NC are magnets for tourists in their own unique ways. As a result, Airbnb has many offerings to suit tourists flocking to these destinations. 

The objective of this analysis is to explore the most statistically-significant characteristics related to rating, reviews, and pricing. This topic was selected to analyze the Airbnb offerings of these two tourist-heavy cities to look for similarities, differences, and any correlations the data analysis can uncover. 

<img src=https://github.com/tutran90/White-/blob/5feb5bb640dbc5694c8ab2c60759fc923a680ed6/Resources/nashville-word-cloud.jpeg width="400" height="400"> <img src=https://github.com/tutran90/White-/blob/5feb5bb640dbc5694c8ab2c60759fc923a680ed6/Resources/asheville-word-cloud.jpeg width="400" height="400">

### Sources of Data
Our data sources were pulled from insideairbnb.com [here](http://insideairbnb.com/get-the-data.html). These datasets have a diverse set of features in which to work with for this project. The data contained within these datasets are mirrors of each other with 51 features each so a thorough, like for like comparison can be done. The Nashville dataset has 2,692 listings to analyze while the Asheville dataset has 1,028 listings. 

The Nashville dataset can be accessed ![here](https://github.com/tutran90/White-/blob/5feb5bb640dbc5694c8ab2c60759fc923a680ed6/listings.csv) for viewing while the Asheville dataset can be accessed ![here](https://github.com/tutran90/White-/blob/5feb5bb640dbc5694c8ab2c60759fc923a680ed6/Asheville_listings.csv). 

The zip codes for the Nashville dataset was obtained from the following [website.](https://simplemaps.com/data/us-zips) The uszips.csv file was parsed down to obtain the correlating zip codes that matched with the given latitude and longitude coordinates. The file can be accessed ![here](https://github.com/tutran90/White-/tree/main/US%20(1)).

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
1) Are there certain districts that have noticeably higher ratings than other districts?
2) Do the current fixed variables (bedrooms, bathrooms, location, etc.) of the property affect the overall rating score?
3) Which 3 features have the highest correlation with overall rating score? 
4) Does the host response rate correlate with higher overall ratings? 
5) Is there a correlation between host listing count and superhost? 

### Communication Protocols
The team has been meeting twice per week during Zoom class time to jointly work on this project. We discuss deliverables and timelines for completion to ensure everyone is on track with their portion of the project. We use the group Slack channel to communicate between and during meetings as well as on an ad-hoc basis.

### Exploratory Data Analysis
- Nashville has an average rating score of 4.856 with a 0.057 standard deviation. A rating at 4.913 or above would constitute 1 standard deviation above the mean or the 68th percentile. 4.97 would constitute a rating score 2 standard deviations above the mean or in the 95th percentile. 

- Asheville has an average rating score of 4.892 with a 0.019 standard deviation. A rating at 4.911 or above would constitute 1 standard deviation above the mean or the 68th percentile. 4.93 would constitute a rating score 2 standard deviations above the mean or in the 95th percentile.

- The difference in the standard deviations for Nashville (0.057 st. dev.) versus Asheville (0.019 st. dev.) is significant. This could be explained by the complexities in the respective markets or Asheville having fewer listings than Nashville. 

- For the Nashville data, there is an 86.8% correlation for accuracy of listing with the rating score. There is also an 82.4% correlation for communication of the host with rating score as well as a 80.9% correlation for cleanliness with the rating score. Location had a 63.2% correlation with rating score for the Nashville market. 

- For the Asheville data, there is an 80.7% correlation for accuracy of listing with the rating score. There is also an 67% correlation for communication of the host with rating score as well as a 73.4% correlation for cleanliness with the rating score. Location had a 52% correlation with rating score for the Asheville market.

- It is telling that the accuracy of the listing had the highest correlation with the total rating score in both markets. Communication (15% delta) and location (10% delta) were the largest differences between the markets in correlation with the rating score. Nashville scored higher in both measures. 

- For the Nashville data, there is an 86.8% correlation for rating score with the accuracy of listing. There is also an 75.5% correlation for communication of the host with accuracy as well as a 74.4% correlation for cleanliness with the accuracy score. Location had a 58.4% correlation with accuracy for the Nashville market.

- For the Asheville data, there is an 80.7% correlation for rating score with the accuracy of listing. There is also an 63.8% correlation for communication of the host with accuracy as well as a 63.7% correlation for cleanliness with the accuracy score. Location had a 40.1% correlation with accuracy for the Asheville market.

- Once again, communication (12% delta) and location (18% delta) were the largest percentage differences for the two markets with the Music City (Nashville) scoring higher in both measures. 

- No significant correlations for host listings count for Nashville. 57.8% of host listing counts in the Asheville market were entire home listings. 

- Significantly higher rating scores correlated with higher host response rate.

- The Airbnb data for Nashville and Ashville have identical characteristics in the datasets. This includes, number of people the listing accommodates, number of bedrooms, beds, and bathrooms. The max and minimum number of nights for the booking as well as if the listing is for "Entire home/apt" or "Private room" is a part of the characteristics of an Airbnb.

### Database
Our team used PostgreSQL to create a database. Our entity relationship diagram (ERD) can be accessed [here.](https://github.com/tutran90/White-/blob/2bd465f61c69daf7d0cd9c3b652b59f6188ab917/images/ERD.pgerd.png)

### Machine Learning Model
Our team used supervised machine learning (Linear Regression) to suggest listings based on pre-specified features of the data.

### Data Visualization
We used Tableau to create an interactive [dashboard](https://public.tableau.com/app/profile/jonathan.brown2419/viz/AirbnbACloserLookNashvilleAsheville/Dashboard1?publish=yes) to visually display host response rate compared to rating as well as highest rated neighborhoods in both cities. 

![](https://github.com/tutran90/White-/blob/e0bcc062491b5930db6651ed20db6f2c39df6208/Resources/Dashboard.PNG)
