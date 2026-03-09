from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense
import os

if not os.path.exists("model"):
    os.makedirs("model")

dummy_model = Sequential([
    Flatten(input_shape=(224, 224, 3)),
    Dense(1, activation='sigmoid')       
])

dummy_model.save("model/defective_model.h5")
print("Dummy model created successfully!")
