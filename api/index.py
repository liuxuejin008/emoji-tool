import traceback
from os.path import join

import requests
from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    join(dir, '..', 'data', 'example.db')
    return 'About'


@app.route('/list',methods=['GET', 'POST'])
def list():
    try:
        word = request.args.get("word")
        if word is None:
            return jsonify({"message": "empty input","rcode":1})
        url = "https://api.together.xyz/v1/chat/completions"
        headers = {
            "Authorization": "Bearer 0c26a4544f9d3e83835161e853a79fc5f82c4ccb156a423f339af516ed11fe24",
            "Content-Type": "application/json"
        }
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
        response_1 = requests.post(url, headers=headers, json=data)
        if response_1.status_code == 200:
            print("Request successful. Response:")
            print(response_1.json())
            message = response_1.json()["choices"][0]["message"]["content"]
        else:
            print(f"Request failed with status code: {response_1.status_code}")
            print(response_1.text)

        return jsonify({'message': message})
    except Exception as e:
        traceback.print_exc()
    # 发生异常时执行回滚操作
        print(f"An error occurred: {e}")
    return jsonify({"message": message,"rcode":0})