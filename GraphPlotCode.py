### CODE FOR PLOTING GRAPHS - Accuracy Review
plt.scatter(airBNB_df["accuracy_review"], features)
plt.xlabel("Accuracy Review")
plt.ylabel("Rating Score")
plt.show

### CODE FOR PLOTING GRAPHS - Cleanliness Review
plt.scatter(airBNB_df["cleanliness_review"], features)
plt.xlabel("Cleanliness Review")
plt.ylabel("Rating Score")
plt.show

### CODE FOR PLOTING GRAPHS - Check-In Review
plt.scatter(airBNB_df["checkin_review"], features)
plt.xlabel("Check-In Review")
plt.ylabel("Rating Score")
plt.show

### CODE FOR PLOTING GRAPHS - Communication Review
plt.scatter(airBNB_df["communication_review"], features)
plt.xlabel("Communication Review")
plt.ylabel("Rating Score")
plt.show

### CODE FOR PLOTING GRAPHS - Location Review
plt.scatter(airBNB_df["location_review"], features)
plt.xlabel("Location Review")
plt.ylabel("Rating Score")
plt.show

### CODE FOR PLOTING GRAPHS - Value Score Review
plt.scatter(airBNB_df["value_score"], features)
plt.xlabel("Value Score")
plt.ylabel("Rating Score")
plt.show

### CODE FOR PLOTING GRAPHS - Number of Properties Review
plt.scatter(airBNB_df["number_properties"], features)
plt.xlabel("Number of Properties")
plt.ylabel("Rating Score")
plt.show

### CODE FOR SCATTER PLOT GRAPH - Number of Properties and Value Score 
plt.scatter(airBNB_df["number_properties","value_score"], features)
plt.xlabel('AirBnB Features')
plt.ylabel("Rating Score")
plt.show()