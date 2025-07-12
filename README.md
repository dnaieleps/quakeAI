# Overview
  In this project, I created a machine learning regression model from XGBoosted trees using the XGB Regressor from the XGB ML library. Given an input array of 10 features, this model is able to predict with relatively good accuracy the depth and magnitude of an earthquake. The input array features consists of: date, latitude, longitude, time since last 5.0-9.0 magnitude earthquake, distance (km) from Ring of Fire faultline, and root mean squared error (rms) of the residuals of the earthquake's hypocenter location. This project uses data from the Kaggle dataset which can be found at https://www.kaggle.com/datasets/usamabuttar/significant-earthquakes, and the csv file used is also included within this repo. A geoJSON file was also used in this project in order to be able to calculate each of the earthquake's kilometric distances from the major fault lines which make up the Pacific Ring of Fire. 

  Ended up with a model that could accurately predict earthquake magnitude correctly within a range of ±0.5 magnitude with a 90% success rate, and could predict earthquake depth correctly within a range of ±100km with a 96% success rate. 

Languages used: Python 

Libraries used: numpy, matplotlib, pandas, sklearn, tensorflow, seaborn, xgboost, geopandas
