#                      <center>Timeline<center>
Task|Assignment|Time
-|:-:|:-:
Front-end stylesheet design|Zhelin Liang|5.6- 5.19
Data analysis/statistics and visualization.|Xinzhi  Huo|5.6- 5.19
Machine Learning-Data:<br><br><br>| Li Ma with <br>Xinzhi Huo| 5.6-6.10
Machine Learning-Model<br>|Yuxuan He with <br>Zhelin Liang|5.6-6.10
  
## which also means
Task|Assignment|Time
-|:-:|:-:
Statistics & Analysis<br>(1)Analyze the correlation of data in each column.<br>(2)Set predictive goals.<br>(3)Select appropriate features and preprocess the data.<br>(1)Import dataset and libraries and quick overview of the data and dataset structure so that checking for and filling the missing values. We will leave the numeric data-types alone and focus on object data-types as what cannot be directly put into a machine learning model. Therefore, we try to give it a discrete value which would help us in prediction and draw a heatmap to clearly see what are the correlations here<br>(2) the predictive goal is to predict Purchase for the customer will be in the store base on other features <br>(3) we try to build a model to predict purchase amount (Purchase column in dataset) from other features. Probably, this is a regression problem and we'll use random forest. We'll choose number of trees (n_estimators) in our forest and max_depth for each tree by calculating scores for each combination and choosing the best one. Scoring metric we'll use is RMSE.<br>|Xinzhi Huo|5.6- 5.19
Regression & classification<br>(1)Select several models to calculate and compare their performance.<br>(2)Perhaps use multiple models together.|Li ma <br>Yuxuan He|5.19- 5.30
Clustering<br>Clustering(K-mean):We try and see if we can cluster our customers (User_IDs) based on products they have purchased and other features.We change our features a little bit to be more suitable for clustering. Firstly, we are going to cluster users and not the transactions so we should group our transactions by User_ID and create our features based on that. Then, choose number of clusters (K). We will use elbow method to choose one and plot different distance sums for different number of clusters.<br>|All members|5.19- 5.30
Visualization<br>(1) Front-end stylesheet design<br>(2)Use Bar-chart & Donut-chart to visualize some interesting data in the analyze module<br>(3) Show the prediction result by reading combination data that users input |Zhelin Liang|5.31-6.10
