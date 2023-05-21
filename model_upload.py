import boto3
import io
import pickle
from transformers import BlipProcessor, BlipForConditionalGeneration

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")

pickle.dump(processor,open('processor.pkl','wb'))
pickle.dump(model,open('model.pkl','wb'))