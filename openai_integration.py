import openai
from decouple import config as decouple_config

openai.api_key = decouple_config('API_KEY', '')

def generate_response(message):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=message,
        max_tokens=100,
        temperature=0.7,
        n=1,
        stop=None
    )
    return response.choices[0].text.strip()

