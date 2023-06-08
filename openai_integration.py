import os
import openai

openai.api_key = os.getenv('API_KEY', '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')

def generate_response(message):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=message,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None
    )
    return response.choices[0].text.strip()

