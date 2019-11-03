import pandas as pd

# Step 1: Importing the required libraries
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import model_selection
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

# https://www.geeksforgeeks.org/30-minutes-to-machine-learning/
# https://www.geeksforgeeks.org/how-to-approach-a-machine-learning-project-a-step-wise-guidance/

# Step 2: Loading the Data
# dataset (csv file) path
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"

# selectng necessary feature
features = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'species']

# reading the csv
data = pd.read_csv('iris.csv')

# Step 3: Summarizing the Data

# This step typically involves the following steps-
# a) Taking a peek at the Data

print(data.head(5))

# b) Finding the dimensions of the Data
print(data.shape)

# c) Statistical summary all attributes

print(data.describe())

# d) Class distribution of the Data
print((data.groupby('species')).size())

# Step 4: Visualising the Data
# This step typically involves the following steps –

# a) Plotting Univariate plots
# This is done to understand the nature of each attribute.

sns.set_style('darkgrid')
data.plot(kind='box', subplots=True, layout=(2, 2),
          sharex=False, sharey=False)

plt.show()

data.hist()
plt.show()


# b) Plotting Multivariate plots
# This is done to understand the relationships between different features.

scatter_matrix(data)
plt.show()

# Step 5: Training and Evaluating our models
# This step typically contains the following steps –

# a) Splitting the training and testing data
# This is done so that some part of the data is hidden from the learning algorithm

y = data['species']
X = data.drop('species', axis=1 )
X_train, X_test, y_train , y_test = model_selection.train_test_split(
    X, y, test_size=0.25, random_state=0)

print(X.head())
print('')
print(y.head())

# b) Building and Cross-Validating the model
algorithms = []
scores = []
names = []

algorithms.append(('Logisitic Regression', LogisticRegression()))
algorithms.append (('K-Nearest Neighbours', KNeighborsClassifier()) )
algorithms.append ( ('Decision Tree Classifier' , DecisionTreeClassifier()) )

for name, algo in algorithms:
    k_fold = model_selection.KFold(n_splits=10 , random_state=0 )

    # Applying k-cross validation
    cvResults = model_selection.cross_val_score( algo, X_train, y_train ,
                                                  cv=k_fold, scoring='accuracy')

    scores.append(cvResults)
    names.append(name)
    print(str(name) + ' : ' + str(cvResults.mean()))


# c) Visually comparing the results of the different algorithms
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(scores)
ax.set_xticklabels(names)
plt.show()

# Step 6: Making predictions and evaluating the predicitons
for name , algo in algorithms:
    clf = algo
    clf.fit ( X_train, y_train)
    y_pred = clf.predict(X_test )
    pred_score = accuracy_score(y_test, y_pred)

    print(str(name) + ' : ' + str(pred_score))
    print('')
    print('Confusion Matrix: ' + str(confusion_matrix(y_test, y_pred)))
    print(classification_report(y_test, y_pred))

# Reference – https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
# https://www.geeksforgeeks.org/how-to-approach-a-machine-learning-project-a-step-wise-guidance/