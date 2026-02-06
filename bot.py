import requests
import os

token = os.getenv("GITHUB_TOKEN")
print(type(token))

OWNER = "octocat"
REPO = "Hello-World"
PR_NUMBER = "1"
headers = {"Authorization": f"Bearer {token}",
           "Accept": "application/vnd.github.v3.diff"}
github_url = f"https://api.github.com/repos/{OWNER}/{REPO}/pulls/{PR_NUMBER}"
response = requests.get(github_url, headers=headers)
print(response.status_code)

diff_text = response.text
full_prompt = f"Review this code for bugs :\n\n{diff_text}"

data = {
    "contents":[
        {
            "parts": [
                {"text": full_prompt}
            ]
        }
    ]
}

GEMINI_KEY = os.getenv("GEMINI_KEY")
gemini_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-pro:generateContent?key={GEMINI_KEY}"
response = requests.post(gemini_url, json = data)
print(response.status_code)
print(response.json())