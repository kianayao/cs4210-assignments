#-------------------------------------------------------------------------
# AUTHOR: kiana yao
# FILENAME: decision_tree.py
# SPECIFICATION: reads in file contact_lens1.csv, contact_lens2.csv, and contact_lens3.csv and outputs a decision tree
# FOR: CS 4210- Assignment #2
# TIME SPENT: 11:11 -  =  min
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']

csv_count = 0;
for ds in dataSets:
    csv_count += 1
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    dbTraining = []
    X = []
    Y = []

    #reading the training data in a csv file
    with open(ds, 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
             if i > 0: #skipping the header
                dbTraining.append (row)

    #transform the original categorical training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
    # so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    #--> add your Python code here
    for i in dbTraining:
        temp = []
        for j in range(0, len(i) - 1, 1):
            if (j == 0):                # Age: Young, Prepresbyopic, or Presbyopic
                if(i[j] == "Young"):
                    temp.append(1)
                elif (i[j] == "Prepresbyopic"):
                    temp.append(2)
                else:
                    temp.append(3)
            elif (j == 1):              # Prescription: Myope or Hypermetrope
                if (i[j] == "Myope"):
                    temp.append(1)
                else:
                    temp.append(2)
            elif (j == 2):              # Astigmatism: Yes or No
                if (i[j] == "Yes"):
                    temp.append(1)
                else:
                    temp.append(2)
            else:                       # Tear Production: Normal or Reduced
                if (i[j] == "Reduced"):
                    temp.append(1)
                else:
                    temp.append(2)
        X.append(temp)

    #transform the original categorical training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    #--> add your Python code here
    for x in dbTraining:    # Reccomended Lenses
        if (x[len(x) - 1] == "Yes"):
            Y.append(1)
        else:
            Y.append(2)

    # counters for accuracy
    correct_count = 0
    wrong_count = 0
    #loop your training and test tasks 10 times here
    for i in range (10):
        #fitting the decision tree to the data setting max_depth=3
        clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=3)
        clf = clf.fit(X, Y)

        #read the test data and add this data to dbTest
        #--> add your Python code here
        dbTest = []
        with open('contact_lens_test.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for i, row in enumerate(reader):
                if i > 0: #skipping the header
                    dbTest.append(row)

        for data in dbTest:
            temp = []
            for j in range(0, len(data), 1):
                if (j == 0):                # Age: Young, Prepresbyopic, or Presbyopic
                    if(data[j] == "Young"):
                        temp.append(1)
                    elif (data[j] == "Prepresbyopic"):
                        temp.append(2)
                    else:
                        temp.append(3)
                elif (j == 1):              # Prescription: Myope or Hypermetrope
                    if (data[j] == "Myope"):
                        temp.append(1)
                    else:
                        temp.append(2)
                elif (j == 2):              # Astigmatism: Yes or No
                    if (data[j] == "Yes"):
                        temp.append(1)
                    else:
                        temp.append(2)
                elif (j == 3):              # Tear Production: Normal or Reduced
                    if (data[j] == "Reduced"):
                        temp.append(1)
                    else:
                        temp.append(2)
                else:                       # Reccomended Lenses
                    if (data[j] == "Yes"):
                        temp.append(1)
                    else:
                        temp.append(2)
            

            #transform the features of the test instances to numbers following the same strategy done during training,
            #and then use the decision tree to make the class prediction. For instance: class_predicted = clf.predict([[3, 1, 2, 1]])[0]
            #where [0] is used to get an integer as the predicted class label so that you can compare it with the true label
            #--> add your Python code here
            temp_t = temp[4]
            temp.pop()
            class_predicted = clf.predict([temp])[0]
            #compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
            #--> add your Python code here
            if class_predicted == temp_t:
                correct_count += 1
            else:
                wrong_count += 1


    #find the average of this model during the 10 runs (training and test set)
    #--> add your Python code here
    total = wrong_count + correct_count
    avg = correct_count / total
    #print the average accuracy of this model during the 10 runs (training and test set).
    #your output should be something like that: final accuracy when training on contact_lens_training_1.csv: 0.2
    #--> add your Python code here
    print('final accuracy when training on contact_lens_training_' + str(csv_count) + '.csv = ' + str(correct_count) + '/' + str(total) + ' = ' + str(avg))




