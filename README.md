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

Afther this, the data was usable for the model.

### Exploratory Data Analysis (exploratory_data_analysis.ipynb)
visualized data, removed outliers and null values and checked the correlation of the parameters

### Model Building (*model_building.ipynb*)
tried three different regression models, stacked the best two models with a meta-regressor and saved the prediction results in a new spreadsheet.

## Data Preprocessing 
## Resources Used
**Python Version:** 3.7  
**Packages:** pandas, numpy, sklearn, matplotlib, mlxtend
**Article on Model Stacking:** https://mlfromscratch.com/model-stacking-explained/#/
**Big inspiration from Ken Jee's Data Science Salary Project:** https://www.youtube.com/playlist?list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t



