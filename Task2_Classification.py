from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()

X = iris.data
y = iris.target

# Split dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create AI Classification Model
model = DecisionTreeClassifier()

# Train Model
model.fit(X_train, y_train)

# Make Predictions
predictions = model.predict(X_test)

# Check Accuracy
accuracy = accuracy_score(y_test, predictions)

print("AI Classification Project")
print("Accuracy:", round(accuracy * 100, 2), "%")

# Example Prediction
sample = [[5.1, 3.5, 1.4, 0.2]]
result = model.predict(sample)

flower_names = iris.target_names
print("Predicted Flower:", flower_names[result[0]])