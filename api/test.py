import requests
TOGETHER_API_KEY  = "0c26a4544f9d3e83835161e853a79fc5f82c4ccb156a423f339af516ed11fe24"
url = "https://api.together.xyz/v1/chat/completions"
headers = {
    "Authorization": "Bearer 0c26a4544f9d3e83835161e853a79fc5f82c4ccb156a423f339af516ed11fe24",
    "Content-Type": "application/json"
}

word = "devil emoji"
prompt = f"""
           假设你是一个emoji专家，我输入文字，你整理概括输出相关的emoji并输出unicode,并至少输出5个相关emoji。
           给定的文字: ```{word}```
           """
data = {
    "model": "teknium/OpenHermes-2p5-Mistral-7B",
    "messages": [
        {"role": "system", "content": "You are an expert emoji guide"},
        {"role": "user", "content": prompt}
    ]
}
response = requests.post(url, headers=headers, json=data)
print(response.json())
message = response.json()["choices"][0]["message"]["content"]
print(message)