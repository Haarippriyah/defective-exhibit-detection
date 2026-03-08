from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense
import os

# Make sure the model folder exists
if not os.path.exists("model"):
    os.makedirs("model")

# Create a dummy model
dummy_model = Sequential([
    Flatten(input_shape=(224, 224, 3)),  # input size same as images
    Dense(1, activation='sigmoid')       # outputs a number between 0 and 1
])

# Save the model
dummy_model.save("model/defective_model.h5")
print("Dummy model created successfully!")