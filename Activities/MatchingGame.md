# Matching Game!
#### Please MATCH each code snippet's LETTER to its corresponding comment's NUMBER.
You can test this code in a notebook if you move the data from inside the Activities_DATA folder,
 to the folder where you create a new notebook.


## Code

A:
`rf_model.fit(X_train, y_train)` 

B:
`print('Test Set Accuracy:',rf_model.score(test_X,test_y))`  
`print('Training Set Accuracy:', rf_model.score(X_train,y_train))`
`print('Out of the Box Accuracy:',rf_model.oob_score_)`

C:
`tables = pd.read_csv('mydata.csv')`

D:
`X = tables`

E:
`score = rf_model.score(test_X,test_y)
print(score)`

F:
`predictions = rf_model.predict(test_X)`

G:
`X_train, test_X, y_train, test_y = train_test_split(X, y, random_state = 11)`

H:
`%matplotlib inline`
`import numpy as np`
`import matplotlib.pyplot as plt`
`import pandas as pd`
`from sklearn.model_selection import train_test_split`
`from sklearn.ensemble import RandomForestClassifier`
                       
I:
`rf_model = RandomForestClassifier(n_estimators = 100,
                           n_jobs = -1,
                           oob_score = True,
                           bootstrap = True,
                           random_state = 42)`
                           
J:
`classes = np.load('mydata_labels.npy')`

K:
`y = classes`



## Comments


1. fit model to data
2. load data
3. print accuracy scores
4. split data into test and training set
5. import libraries
6. load labels
7. set variable for correct labels
8. have fit model predict labels for previously unseen data
9. define random forest model
10. set variable for feature data
11. check the accuracy of fit model




