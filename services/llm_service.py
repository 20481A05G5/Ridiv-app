import requests
import os
import json
from fastapi import HTTPException

def get_gemini_response(question: str) -> str:
    api_key = "AIzaSyAIUQGTuSDX0X-JmgzWMZBCcyqt0j7V9Ow"
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key={api_key}"
    
    headers = {'Content-Type': 'application/json'}
    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [
                    {
                        "text": question
                    }
                ]
            }
        ]
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        try:
            # Parsing the content from the Gemini response
            return response.json()['content']
        except KeyError:
            raise HTTPException(status_code=500, detail="Malformed response from Gemini API")
    else:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch response from Gemini API")