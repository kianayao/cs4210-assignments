#-------------------------------------------------------------------------
# AUTHOR: kiana yao
# FILENAME: decision_tree.py
# SPECIFICATION: reads in file contact_lens.csv and outputs a decision tree
# FOR: CS 4210- Assignment #1
# TIME SPENT: 10:32 - 11:16 = 44 min
#-----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE
# SUCH AS numpy OR pandas. You have to work here only with standard dictionaries,
# lists, and arrays

# importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

# reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

# transform the original categorical training features into numbers and add to the 4D array X.
# For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
# so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
# --> add your Python code here
for i in db:
    temp = []
    for j in range(0, len(i) - 1, 1):
        if (j == 0):
            if(i[j] == "Young"):
                temp.append(1)
            elif (i[j] == "Prepresbyopic"):
                temp.append(2)
            else:
                temp.append(3)
        elif (j == 1):
            if (i[j] == "Myope"):
                temp.append(1)
            else:
                temp.append(2)
        elif (j == 2):
            if (i[j] == "Yes"):
                temp.append(1)
            else:
                temp.append(2)
        else:
            if (i[j] == "Reduced"):
                temp.append(1)
            else:
                temp.append(2)

    X.append(temp)

# transform the original categorical training classes into numbers and add to the vector Y.
# For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
# --> add your Python code here
for x in db:
    if (x[len(x) - 1] == "Yes"):
        Y.append(1)
    else:
        Y.append(2)

# fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)

# plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()
