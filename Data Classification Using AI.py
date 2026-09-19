# Import required libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
iris = load_iris()
X = iris.data          # Features
y = iris.target        # Target / Classes
print("Iris Dataset Loaded Successfully!")
print("Number of samples:", len(X))
print("Number of features:", X.shape[1])
print("Classes:", iris.target_names)
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)
print("\nKNN Model trained successfully!")
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("\nModel Accuracy:", accuracy * 100, "%")
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred,
    target_names=iris.target_names
))
new_flower = [[
    5.1,    # Sepal Length
    3.5,    # Sepal Width
    1.4,    # Petal Length
    0.2     # Petal Width
]]
new_flower_scaled = scaler.transform(new_flower)
prediction = model.predict(new_flower_scaled)

print("\nNew Flower Prediction:")
print("Predicted Class:", iris.target_names[prediction[0]])
