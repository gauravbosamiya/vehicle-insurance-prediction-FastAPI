import pickle
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

with open("model/pipeline.pkl","rb") as f:
    model = pickle.load(f)

MODEL_VERSION = '1.0.0'

class_labels = model.classes_.tolist()


def predict_output(user_input: dict):
    df = pd.DataFrame([user_input])
    
    predicted_class = model.predict(df)[0]
    predicted_class = int(predicted_class)
    
    probabilities = model.predict_proba(df)[0]
    confidence = max(probabilities)
    
    class_probs = dict(zip(class_labels, map(lambda p: round(p, 4), probabilities)))

    return {
        "predicted_class" : predicted_class,
        "confidence" : round(confidence, 4),
        "class_probabilities": class_probs
    }