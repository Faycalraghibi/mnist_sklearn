import pickle

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_openml

mnist = fetch_openml('mnist_784', version=1)

X, y = mnist['data'], mnist['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

random_forest = RandomForestClassifier(n_estimators=100, n_jobs=-1)

random_forest.fit(X_train, y_train)

print(random_forest.score(X_test, y_test))

with open('mnist_model.pkl', 'wb') as f:
    pickle.dump(random_forest, f)