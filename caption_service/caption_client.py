import requests
import pickle
import nltk
from nltk.corpus import stopwords
from PIL import Image
from caption_service.helpers import clean_caption
# from transformers import BlipProcessor, BlipForConditionalGeneration

class CaptionClient:

    def __init__(self):
        print("Here")
        nltk.download('stopwords')
        self.fillers = (stopwords.words('english'))
        print('Here 1')
        self.processor = pickle.load(open('processor.pkl','rb'))
        print("Here 2")
        self.model = pickle.load(open('model.pkl', 'rb'))
        print("Here 3")

    def caption_generator(self,data):
        raw_image = Image.open(requests.get(data.image_url, stream=True).raw).convert('RGB')

        inputs = self.processor(raw_image, return_tensors="pt")

        out = self.model.generate(**inputs,max_length=35)

        generated_caption = self.processor.decode(out[0], skip_special_tokens=True)

        generated_caption = clean_caption(generated_caption,self.fillers)

        return generated_caption