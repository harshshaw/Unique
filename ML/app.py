import os,io 
from google.cloud import vision

os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r'ku-hack-6b534f8e99ac.json'
client=vision.ImageAnnotatorClient()