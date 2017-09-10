from sklearn import tree
X = [[100,200,300],[200,300,400]]
Y= ['male','female']
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)
prediction =clf.predict([[190,70,200]])
print(prediction)
