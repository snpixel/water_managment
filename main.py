import google.generativeai as genai
import PIL.Image as Ig
from IPython.display import Markdown

sf_1 = Ig.open("ward_water_comparison.png")

genai.configure(api_key='AIzaSyB8Yb0YB-xFV3vZYOTsgefzRQVfNn3RMLQ')

model = genai.GenerativeModel(model_name="gemini-1.5-pro")
prompt = "describe the image of this grpah and gives us the anlysis of the data and how we can minimize the supply or increase the supply to adjust the wards requirements. only give redistribution of water supply to the wards explain all 84 wards redistribution of water supply to the wards. "

# chat = model.start_chat(enable_automatic_function_calling=True)

response = model.generate_content([prompt , sf_1])

# Markdown(">"+response.text)

print(response.text)



