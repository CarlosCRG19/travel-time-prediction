#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 14:54:00 2020

@author: carlosrodriguez
"""

import pandas as pd

df = pd.read_csv("go_tracks.csv")
track_points = pd.read_csv("go_track_trackspoints.csv")

#Travel time is the target value, so I'll assign a different name to it
df = df.rename({"time":"travel_time"}, axis=1)

#Change travel_time from hours to minutes
df["travel_time"] = df["travel_time"].apply(lambda x: x * 60)

#Get the time the data was taken
track_points["time"] = track_points["time"].astype('datetime64[ns]')

df["time"] = df["id"].apply(lambda x: track_points[track_points.track_id == x]["time"].min())

#Check for duplicate values and remove them
df_duplicaterows = df[df.drop("id", axis=1).duplicated()]  #For some reason, although all the data is the same, even position accoring to track_points, there are different ID's for some values
df = df.drop(df_duplicaterows.index)

#Drop id_android as it is not specified the meaning of the values
df = df.drop("id_android", axis = 1)

#Get values for day of the week
df["day"] = df["time"].dt.dayofweek #Returns the day of the week as int (0 for Monday and 6 for Sunday)

#Get values for hour 
df["hour"] = df["time"].dt.hour #Returns the hour as an integer between 0 and 23

#Remove name of bus lines, id, rating_bus and the recently created time column
df = df.drop(["linha","id","rating_bus","time"], axis = 1)

df.to_csv("preprocessed_data.csv")

