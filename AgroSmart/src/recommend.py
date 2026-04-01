import pickle
import os

_model = None

def _load_model():
    global _model
    if _model is None:
        base = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "models")
        _model = pickle.load(open(os.path.join(base, "crop_model.pkl"), "rb"))

def recommend_crop(data):
    _load_model()
    prediction = _model.predict([data])
    return prediction[0]