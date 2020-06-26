import numpy as np
from hummingbird.ml import convert
from sklearn.ensemble import RandomForestClassifier

# Create some random data for binary classification
num_classes = 2
X = np.array(np.random.rand(100000, 28), dtype=np.float32)
y = np.random.randint(num_classes, size=100000)

# Create and train a model (scikit-learn RandomForestClassifier in this case)
skl_model = RandomForestClassifier(n_estimators=10, max_depth=10)
skl_model.fit(X, y)

# Use Hummingbird to convert the model to PyTorch
model = convert(skl_model, 'pytorch')

# Run predictions on CPU
model.predict(X)

# Run predictions on GPU
model.to('cuda')
pred_y = model.predict(X)

print(pred_y)
