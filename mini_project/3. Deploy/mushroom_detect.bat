@echo off
:: 한글 깨짐 방지
chcp 65001 > nul
title Mushroom AI Diagnosis Service

echo ==================================================
echo [시스템] 표고버섯 AI 진단 서비스를 시작합니다...
echo ==================================================

:: 1. 배치 파일이 있는 폴더(3. Deploy)로 확실하게 이동
cd /d "%~dp0"

:: 2. 가상환경 확인 (사용자님의 폴더 구조에 가상환경이 없다면 이 부분은 건너뜁니다)
:: 만약 아나콘다(py310) 환경을 쓰신다면 아래 명령어는 필요 없습니다.
if exist ".v17_mini_project\Scripts\activate" (
    echo [정보] 가상환경 활성화 중...
    call ".v17_mini_project\Scripts\activate"
)

:: 3. Streamlit 실행
echo [진행] 웹 브라우저를 실행합니다. 잠시만 기다려 주세요...
echo [정보] 현재 실행 경로: %cd%

:: python -m streamlit 형식을 사용하면 환경 변수 문제를 방지할 수 있습니다.
python -m streamlit run mushroom_detect_app.py

:: 에러 발생 시 창이 바로 닫히지 않게 유지
if %errorlevel% neq 0 (
    echo.
    echo ❌ [에러] 프로그램 실행 중 문제가 발생했습니다.
    echo 💡 CMD창에서 직접 'streamlit run mushroom_detect_app.py'를 입력해 보세요.
    pause
)