#-------------------------------------------------------------------------
# AUTHOR: kiana yao
# FILENAME: knn.py
# SPECIFICATION: reads in file binary_points.csv
# FOR: CS 4210 - Assignment #2
# TIME SPENT: 12:30 - 1:15 = 45 min
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn.neighbors import KNeighborsClassifier
import csv
import copy

db = []

#reading the data in a csv file
with open('binary_points.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append(row)

#loop your data to allow each instance to be your test set
index_counter = -1
correct_count = 0
wrong_count = 0
for test in db:
    index_counter += 1
    new_copy = copy.deepcopy(db)
    # add the training features to the 2D array X removing the instance that will be used for testing in this iteration. 
    # For instance, X = [[1, 3], [2, 1,], ...]]. Convert each feature value to
    # float to avoid warning messages
    #--> add your Python code here
    X = []
    for i in range(0, len(db), 1):
        temp = []
        if i != index_counter:
            for j in range(0, len(db[i]) - 1, 1):
                temp.append(float(db[i][j]))
            X.append(temp)
    print(X)
    # transform the original training classes to numbers and add to the vector Y removing the instance that will be used 
    # for testing in this iteration. For instance, Y = [1, 2, ,...]. Convert each
    # feature value to float to avoid warning messages
    #--> add your Python code here
    Y = []
    for i in range(0, len(db), 1):
        temp = []
        if i != index_counter:
            if db[i][len(db[i]) - 1] == '+':
                Y.append(1)
            else:
                Y.append(2)

    #store the test sample of this iteration in the vector testSample
    #--> add your Python code here
    t_test = test.copy()
    t_test.pop()
    testSample = [float(t) for t in t_test]

    #fitting the knn to the data
    clf = KNeighborsClassifier(n_neighbors=1, p=2)
    clf = clf.fit(X, Y)
    #use your test sample in this iteration to make the class prediction. For instance:
    #class_predicted = clf.predict([[1, 2]])[0]
    #--> add your Python code here
    testSample.pop()
    class_predicted = clf.predict([testSample])[0]

    #compare the prediction with the true label of the test instance to start calculating the error rate.
    #--> add your Python code here
    true_result = 1 if test[2] == '+' else 2
    if class_predicted == true_result:
        correct_count += 1
    else:
        wrong_count += 1
#print the error rate
#--> add your Python code here
total = wrong_count + correct_count
print('error rate = ' + str(wrong_count) + '/' + str(total) + ' = ' + str(wrong_count/total))






