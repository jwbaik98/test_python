# v12_4_ang_web.py

from flask import Flask, render_template, request, jsonify
from huggingface_hub import InferenceClient
import webbrowser
import threading
import re

app = Flask(__name__)

# 타임아웃 설정 (기본값: 30초 → 120초로 증가)
client = InferenceClient(
    api_key="",
    timeout=120.0  # 120초로 설정
)

def remove_markdown(text):
    """마크다운 형식 제거"""
    if not text:
        return text
    
    # ** 제거 (굵은 텍스트)
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
    
    # * 제거 (이탤릭)
    text = re.sub(r'\*(.*?)\*', r'\1', text)
    
    # _ 제거
    text = re.sub(r'_(.*?)_', r'\1', text)
    
    # __ 제거
    text = re.sub(r'__(.*?)__', r'\1', text)
    
    # # 제거 (제목)
    text = re.sub(r'^#+\s', '', text, flags=re.MULTILINE)
    
    # ` 제거 (코드)
    text = re.sub(r'`(.*?)`', r'\1', text)
    
    # --- 또는 *** 제거 (수평선)
    text = re.sub(r'[-*]{3,}', '', text)
    
    # > 제거 (인용)
    text = re.sub(r'^>\s', '', text, flags=re.MULTILINE)
    
    # [ ]( ) 제거 (링크)
    text = re.sub(r'\[(.*?)\]\((.*?)\)', r'\1', text)
    
    # == 제거
    text = re.sub(r'==(.*?)==', r'\1', text)
    
    return text

def format_response(text):
    """답변을 깔끔하게 포맷팅"""
    if not text:
        return text
    
    # 1. 마크다운 형식 제거
    text = remove_markdown(text)
    
    # 2. 과도한 공백 제거
    text = re.sub(r'\n\n+', '\n', text)  # 여러 줄바꿈을 하나로
    text = re.sub(r'  +', ' ', text)     # 여러 공백을 하나로
    
    # 3. 불필요한 특수문자 정리
    text = text.replace('\\n', '\n')
    text = text.replace('\\t', '\t')
    
    # 4. 앞뒤 공백 제거
    text = text.strip()
    
    # 5. 문장 끝에 이상한 문자 제거
    text = re.sub(r'([.!?])\s*$', r'\1', text)
    
    return text

def clean_response(text):
    """AI 답변에서 불필요한 부분 제거"""
    lines = text.split('\n')
    cleaned_lines = []
    
    for line in lines:
        line = line.strip()
        # 너무 짧은 줄 스킵 (단순 이모지나 기호만 있는 경우)
        if len(line) < 2 and line in ['', ' ', '\t']:
            continue
        cleaned_lines.append(line)
    
    result = '\n'.join(cleaned_lines)
    return result

@app.route('/')
def index():
    return render_template('ang_index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')
    
    if not user_message:
        return jsonify({'error': '메시지를 입력해주세요'}), 400
    
    try:
        print(f"📤 요청 중: {user_message}")
        
        completion = client.chat.completions.create(
            model="MLP-KTLim/llama-3-Korean-Bllossom-8B",
            messages=[
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            temperature=0.7,
            max_tokens=1024  # 512 → 1024로 증가 (더 긴 답변)
        )
        
        response = completion.choices[0].message
        
        if hasattr(response, 'content'):
            answer_text = response.content
        else:
            answer_text = str(response)
        
        # 답변 정리
        answer_text = clean_response(answer_text)
        answer_text = format_response(answer_text)
        
        print(f"✅ 응답 완료: {answer_text[:50]}...")
        
        return jsonify({'response': answer_text})
    
    except Exception as e:
        print(f"❌ 오류: {e}")
        error_message = str(e)
        
        # 타임아웃 오류 처리
        if "504" in error_message or "timeout" in error_message.lower():
            return jsonify({
                'error': '⏱️ 서버 응답이 늦어졌습니다. 다시 시도해주세요.'
            }), 504
        else:
            return jsonify({'error': error_message}), 500

def open_browser():
    import time
    time.sleep(1)
    webbrowser.open('http://localhost:5002')

if __name__ == '__main__':
    threading.Thread(target=open_browser, daemon=True).start()
    
    print("\n🚀 한국어 LLM 서버 시작됨!")
    print("📱 브라우저가 자동으로 열립니다...")
    print("❌ 종료하려면: Ctrl+C\n")
    
    app.run(debug=True, port=5002)