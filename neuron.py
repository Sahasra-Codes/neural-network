
# My First Neural Network
# Goal: Teach a neuron that 3 -> 6

# Step 1: Training data
x = 3
correct_answer = 6

# Step 2: Starting values
weight = 0.0
bias = 0.0

# Step 3: Learning settings
learning_rate = 0.05
epochs = 30

# Step 4: Training loop
for step in range(epochs):

    # TODO 1: Calculate the prediction
    prediction = (x * weight) + bias

    # TODO 2: Calculate the error
    error = prediction - correct_answer
    # TODO 3: Calculate gradients
    weight_gradient = 2 * error * x
    bias_gradient = 2 * error

    # TODO 4: Update weight and bias
    weight = weight - learning_rate * weight_gradient
    bias = bias - learning_rate * bias_gradient


    # Show progress
    print("Step:", step, "Prediction:", prediction)

# Final results
print("Final weight:", weight)
print("Final bias:", bias)
