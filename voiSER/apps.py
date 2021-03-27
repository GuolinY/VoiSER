from django.apps import AppConfig
import html
from pathlib import Path
import os

from tensorflow.keras.models import model_from_json

class WebappConfig(AppConfig):
    name = 'voiSER'

    with open('model.json', 'r') as f:
        loaded_model = model_from_json(f.read())
    f.close()
    
    loaded_model.load_weights("saved_models/ser_model.h5")
