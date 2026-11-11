# -*- coding: utf-8 -*-
import math, os

# 1. 파일 이름을 반드시 index.html로 설정 (GitHub Pages용)
OUTPUT_FILE = "index.html"
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(OUT_DIR, OUTPUT_FILE)

# ============================================================
# 여기에 사용자님의 841줄짜리 전체 코드를 붙여넣으시면 됩니다!
# 제가 파일 저장 부분만 index.html로 바꿔놓을게요.
# ============================================================

def generate_html():
    # (사용자님의 기존 코드 로직이 들어가는 곳)
    # ...
    
    # 예시용 임시 내용 (실제 코드를 주시면 이 부분이 채워집니다)
    html_content = "<html><body><h1>포스터 생성 완료!</h1></body></html>"
    
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"✅ 생성 완료: {FILE_PATH}")

if __name__4 == "__main__":
    generate_html()
