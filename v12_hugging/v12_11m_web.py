from flask import Flask, render_template, request, jsonify
from huggingface_hub import InferenceClient
import webbrowser
import threading

app = Flask(__name__)

client = InferenceClient(
    api_key="",
    provider="auto"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get('message')
    
    try:
        completion = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-V3.2:novita",
            messages=[
                {
                    "role": "user",
                    "content": user_input
                }
            ],
        )
        
        response = completion.choices[0].message
        
        if hasattr(response, 'content'):
            answer_text = response.content
        else:
            answer_text = str(response)
        
        return jsonify({'response': answer_text})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def open_browser():
    """1초 후 브라우저 자동 열기"""
    import time
    time.sleep(1)
    webbrowser.open('http://localhost:5000')

if __name__ == '__main__':
    # 브라우저 자동 열기
    threading.Thread(target=open_browser, daemon=True).start()
    
    print("\n🚀 서버 시작됨!")
    print("📱 브라우저가 자동으로 열립니다...")
    print("❌ 종료하려면: Ctrl+C\n")
    
    app.run(debug=True, port=5000)