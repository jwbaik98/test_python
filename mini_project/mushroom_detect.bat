@echo off
chcp 65001 > nul
title Mushroom AI Diagnosis Service

:: 1. 현재 배치 파일 위치로 이동
cd /d "%~dp0"

:: 2. 가상환경의 파이썬 경로 설정
:: py310 폴더가 배치파일과 같은 곳에 있다면 아래 경로가 맞습니다.
set PYTHON_EXE=%~dp0py310\Scripts\python.exe

:: 만약 가상환경이 다른 곳에 있다면 실제 경로로 수정하세요.
:: 예: set PYTHON_EXE=C:\Users\Administrator\anaconda3\envs\py310\python.exe

echo ==================================================
echo [시스템] 가상환경을 사용하여 서비스를 시작합니다...
echo ==================================================

:: 3. 가상환경의 파이썬으로 streamlit 실행
:: 'app' 폴더 안의 'mushroom_detect_app.py'를 실행합니다.
"%PYTHON_EXE%" -m streamlit run app\mushroom_detect_app.py

if %errorlevel% neq 0 (
    echo.
    echo ❌ [에러] 실행에 실패했습니다. 라이브러리가 설치되었는지 확인하세요.
    pause
)