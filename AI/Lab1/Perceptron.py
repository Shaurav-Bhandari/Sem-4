import numpy as np

class perceptron:
    def __init__(self, LearningRate=0.1, epochs=1000):
        self.__epochs = epochs
        self.__LearningRate = LearningRate
        self.__weights = None
        self.__bias = None
    
    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.__weights = np.zeros(n_features)
        self.__bias = 0
        
        print(f"Initial weights: {self.__weights}, Initial bias: {self.__bias}")
        
        for epoch in range(self.__epochs):
            print(f"\nEpoch {epoch + 1}/{self.__epochs}")
            for idx, x_i in enumerate(X):
                linear_output = np.dot(x_i, self.__weights) + self.__bias
                y_predicted = self.step_function(linear_output)
                
                print(f"\n  Sample {idx + 1}: {x_i}, Target: {y[idx]}")
                print(f"  Linear output: {linear_output}, Prediction: {y_predicted}")
                
                update = self.__LearningRate * (y[idx] - y_predicted)
                print(f"  Update value: {update}")
                
                old_weights = self.__weights.copy()
                old_bias = self.__bias
                
                self.__weights += update * x_i
                self.__bias += update
                
                print(f"  Weights updated from {old_weights} to {self.__weights}")
                print(f"  Bias updated from {old_bias} to {self.__bias}")
                
                # This condition was outside the loop in original code - moved inside
                if y[idx] != y_predicted:
                    update = self.__LearningRate * (y[idx] - y_predicted)
                    self.__weights += update * x_i
                    self.__bias += update
    
    def predict(self, X):
        linear_output = np.dot(X, self.__weights) + self.__bias
        y_predicted = self.step_function(linear_output)
        return y_predicted
    
    def step_function(self, x):
        return np.where(x >= 0, 1, 0)

# AND gate data
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 1])  # Corrected expected output for AND gate

Lrate = float(input("Enter the learning rate (e.g., 0.01): "))
epochs = int(input("Enter the number of epochs (e.g., 4): "))

# Instantiate and train the Perceptron
print("Training the perceptron for AND gate...")
p = perceptron(LearningRate=Lrate, epochs=epochs)
p.fit(X, y)

# Prediction
print("\nFinal predictions:")
print("Inputs:", X)
print("Predictions:", p.predict(X))  # Expected: [0 0 0 1]