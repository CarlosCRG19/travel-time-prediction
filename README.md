# Travel Time Estimator
This tool makes a prediction of the travel time of a vehicle (according to certain parameters) in the city of Aracaju in Brazil.
* **Note:** The database was provided by my Introduction to Engineering class. Actually, the intention was for us to learn to use Excel with this data (graphs, filters, etc.), but I wanted to do this little project, lol.

## The data 
I started with two spreadsheets (*go_tracks* and *go_track_trackspoints*), both contain information about the route of different vehicles in Aracaju. *go_track_trackspoints* contains a record of the vehicle's position change every 5 seconds and *go_tracks* contains the general attributes that I took into account for the elaboration of the model.

* *go_tracks columns description*:
    * **id_android:** represents the device used to capture the information
    * **speed:** average speed (kilometers per hour)
    * **distance:** total distance traveled (kilometers) 
    * **rating:** it is an evaluation parameter. Traffic assessment is a way to verify the user's perception of traffic during the journey. In other words, if the user arrives somewhere with traffic jams, they might evaluate the traffic as "bad". The scale used is: 3 = good, 2 = normal, 1 = bad.
    * **rating_bus** another user evaluation parameter. The evaluation scale is: 3 = the bus is very full, 2 = the bus is a little full, 1 = there are very few people on the bus
    * **rating_weather**: The evaluation scale is: 2 = sunny, 1 = rainy
    * **car_or_bus:** if the user was driving a car or a bus. 1 = car, 2 = bus
    * **linha:** name of the bus line
    
## Project Overview 

### Data Preprocessing (*data_preprocessing.py*) 
I added new columns to consider them as parameters and then dropped some other that either didn't represent important information or were only related to buses. 

The changes made were:
* Got the date and time data from *go_track_trackspoints* and create columns for both of them
* Changed the column "time" to "travel_time" and converted its values to minutes instead of hours
* Dropped the "linha", "id_android", "id" and "rating_bus" columns
* Created a new file for the preprocessed data

After this, the data was usable for the model.

### Exploratory Data Analysis (*exploratory_data_analysis.ipynb*)
Once the database was clean, I made several visualizations of the data before moving on to building the model. Here are some highlights...

![alt text](https://github.com/CarlosCRG19/travel-time-prediction/blob/master/car_bus_speed.png "Car and bus speeds")
![alt text](https://github.com/CarlosCRG19/travel-time-prediction/blob/master/day_graph.png "Number of vehicles by Day")
![alt text](https://github.com/CarlosCRG19/travel-time-prediction/blob/master/hour_graph.png "Number of vehicles by Hour")
![alt text](https://github.com/CarlosCRG19/travel-time-prediction/blob/master/heat_map.png "Correlations")

This step was helpful in identifying null values and outliers. In this way, I realized that unfortunately the "rating_weather" parameter was only answered by bus passengers, so the data for cars had no value ... for this reason I decided to delete the column -although I would have liked see if the weather had an influence on the travel time-. Also, outliers based on speed were removed since the accuracy of the model.

Since speed is the relationship between distance and time, it would be a redundant variable for the model, so I decided to remove it. *Also, trying to predict travel time, knowing the distance and speed, would be cheating, jeje.*

### Model Building (*model_building.ipynb*)
I tried three different regression models and evaluated them using R-squared, as it is easy to interpret. The performance of the models was as follows:

* **Linear Regression:** 0.639
* **Random Forest Regression:** 0.550
* **Lasso Regression:** 0.641

Tbh, I thought that Random Forest and Lasso would easily outperform the Linear model. However, this was not true as Random Forest was much worse and Lasso regression was only slightly better.

Finally, I tried to improve performance through model stacking. I took inspiration from an article by Casper Hansen on how this is a good practice and how it improves the results... and it did...

* **Meta-regressor:** 0.655

Just a small improvement (.014 from the Lasso model), but it does make a difference :)

## Results 
The results were satisfactory and I saved them to a new spreadsheet. Although the accuracy of the model is not that high, I am very happy with the learning of this project.

![alt text](https://github.com/CarlosCRG19/travel-time-prediction/blob/master/results_head.png "Head of the Results spreadsheet")

## Resources Used
* **Python Version:** 3.7  
* **Packages:** pandas, numpy, sklearn, matplotlib, mlxtend
* **Article on Model Stacking:** https://mlfromscratch.com/model-stacking-explained/#/ 
* **Big inspiration from Ken Jee's Data Science Salary Project:** https://www.youtube.com/playlist?list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t



