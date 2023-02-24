#-------------------------------------------------------------------------
# AUTHOR: kiana yao
# FILENAME: naive_bayes.py
# SPECIFICATION: reads in file weather_trining.csv to train model, then classifies weather_test.csv
# FOR: CS 4210 - Assignment #2
# TIME SPENT: 2:30 - 3:15 = 45 min
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv

dbTraining = []
#reading the training data in a csv file
#--> add your Python code here
with open('weather_training.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0: #skipping the header
            dbTraining.append(row)
#transform the original training features to numbers and add them to the 4D array X.
#For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
#--> add your Python code here
X = []
for i in dbTraining:
    temp = []
    for j in range(1, len(i) - 1, 1):
        if (j == 0):                # Outlook: Sunny, Overcast, or Rain
            if(i[j] == "Sunny"):
                temp.append(1)
            elif (i[j] == "Overcast"):
                temp.append(2)
            else:
                temp.append(3)
        elif (j == 1):              # Temperature: Hot, Mild, or Cool
            if (i[j] == "Hot"):
                temp.append(1)
            elif (i[j] == "Mild"):
                temp.append(2)
            else:
                temp.append(3)
        elif (j == 2):              # Humidity: High or Normal
            if (i[j] == "High"):
                temp.append(1)
            else:
                temp.append(2)
        else:                       # Wind: Weak or Strong
            if (i[j] == "Weak"):
                temp.append(1)
            else:
                temp.append(2)
    X.append(temp)

#transform the original training classes to numbers and add them to the vector Y.
#For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> add your Python code here
Y = []
for x in dbTraining:    # Reccomended Lenses
    if (x[len(x) - 1] == "Yes"):
        Y.append(1)
    else:
        Y.append(2)

#fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

#reading the test data in a csv file
#--> add your Python code here
dbTest = []
headers = []
with open('weather_test.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i == 0:
            headers.append(row)
        if i > 0: #skipping the header
            dbTest.append(row)

#printing the header is the solution
#--> add your Python code here
(headers[0]).append('Confidence')
for h in headers[0]:
    print(h.center(16), end = " ")
print()
for i in dbTest:
    temp = []
    for j in range(1, len(i) - 1, 1):
        if j == 1:                # Outlook: Sunny, Overcast, or Rain
            if i[j] == "Sunny":
                temp.append(1)
            elif i[j] == "Overcast":
                temp.append(2)
            else:
                temp.append(3)
        elif j == 2:              # Temperature: Hot, Mild, or Cool
            if i[j] == "Hot":
                temp.append(1)
            elif i[j] == "Mild":
                temp.append(2)
            else:
                temp.append(3)
        elif j == 3:              # Humidity: High or Normal
            if i[j] == "High":
                temp.append(1)
            else:
                temp.append(2)
        else:                       # Wind: Weak or Strong
            if (i[j] == "Weak"):
                temp.append(1)
            else:
                temp.append(2)
    #use your test samples to make probabilistic predictions. For instance: clf.predict_proba([[3, 1, 2, 1]])[0]
    #--> add your Python code here
    class_predicted = clf.predict_proba([temp])[0]
    confidence = 0
    playTennis = 'n/a'
    print_con = False
    if class_predicted[0] >= .75:
        print_con = True
        playTennis = 'Yes'
        confidence = class_predicted[0]
    elif class_predicted[1] >= .75:
        print_con = True
        playTennis = 'No'
        confidence = class_predicted[1]
    if print_con:
        i.pop()
        i.append(playTennis)
        i.append(confidence)
        for f in i:
            print(str(f).center(16), end = " ")
        print()


