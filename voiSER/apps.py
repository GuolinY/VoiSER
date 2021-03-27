from django.apps import AppConfig
import html
from pathlib import Path
import os

from fast_bert.prediction import BertClassificationPredictor

class WebappConfig(AppConfig):
    name = 'voiSER'
