import urllib             # URL 요청
import json               # JSON 데이터 처리용
import pandas as pd       #  데이터 프레임 생성 및 데이터 처리용
import urllib.request     # URL 요청 2

def its_cctv(cctv_index = 77, road_type = "its",  API_KEY = "", MIN_X = (120.95), MAX_X = (127.02), MIN_Y = (30.55), MAX_Y = (37.69)):
   
    # 1. 인증 키 설정
    key = API_KEY

    # 2. 도로 유형 지정
    Type = road_type
    # its : 일반도로
    # ex : 고속도로

    # 3. 관심 영역 설정(경도, 위도)
    minX = float(MIN_X)     # 최소 경도
    maxX = float(MAX_X)   # 최대 경도
    minY = float(MIN_Y)   # 최소 위도
    maxY = float(MAX_Y)   # 최대 위도

    # 4. 응답 데이터 형식 설정
    getType = "json"
        
    # 5. API 요청 URL 생성
    url_cctv = (
        f"https://openapi.its.go.kr:9443/cctvInfo?apiKey={key}&type={Type}&cctvType=1&minX={minX}&maxX={maxX}&minY={minY}&maxY={maxY}&getType={getType}"
        )

    # 6. API 요청 및 응답 받기
    response = urllib.request.urlopen(url_cctv)

    # 7. 응답 데이터 디코딩 -> bytes -> str
    json_str = response.read().decode("utf-8")
    # print(json_str)

    # 8. JSON 문자열 - >  파이썬 딕셔너리
    json_object = json.loads(json_str)
    print(json_object)

    # 9. 데이터 프레임 변환
    cctv_play = pd.json_normalize(json_object["response"]["data"], sep = '')
    # print(cctv_play)

    # 10. 특정 CCTV 선택
    test_url = cctv_play["cctvurl"][cctv_index]
    print(f"선택된 CCTV URL : {test_url}, CCTV 번호 : {cctv_index}")
    return test_url
    # 위 코드 내용을 함수화 시켜주세요
    # 함수화 매개변수로 CCTV 번호를 선택할 수 있게 해주세요.

# its_cctv(100)