import pickle
import pandas as pd
import os

# Get the path relative to the project root
model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')

# import the ml model
with open(model_path, 'rb') as f:
    insurance_model = pickle.load(f)

# MLFlow
MODEL_VERSION = '1.0.0'

# Get class labels from model (important for matching probabilities to class names)
class_labels = insurance_model.classes_.tolist()

def predict_insurance_premium(user_input: dict):

    df = pd.DataFrame([user_input])

    # Predict the class
    predicted_class = insurance_model.predict(df)[0]

    # Get probabilities for all classes
    probabilities = insurance_model.predict_proba(df)[0]
    confidence = max(probabilities)
    # Create mapping: {class_name: probability}
    class_probs = dict(zip(class_labels, map(lambda p: round(p, 4), probabilities)))
    return {
        "predicted_category": predicted_class,
        "confidence": round(confidence, 4),
        "class_probabilities": class_probs
    }
