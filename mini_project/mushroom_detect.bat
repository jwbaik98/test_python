@echo off
:: 한글 깨짐 방지를 위해 인코딩을 UTF-8(65001)로 설정
chcp 65001 > nul

title Mushroom AI Diagnosis Service
echo ==================================================
echo [시스템] 표고버섯 AI 진단 서비스를 시작합니다...
echo ==================================================

:: 1. 현재 배치 파일이 있는 폴더로 경로 이동
cd /d %~dp0

:: 2. 가상환경 확인 및 활성화
if exist .v17_mini_project\Scripts\activate (
    echo [정보] 가상환경을 활성화하는 중입니다.
    call .v17_mini_project\Scripts\activate
) else (
    echo [경고] .v17_mini_project폴더를 찾을 수 없습니다. 파이썬 환경을 확인하세요.
    pause
    exit
)

:: 3. Streamlit 실행
echo [진행] 웹 브라우저가 곧 실행됩니다. 잠시만 기다려 주세요...
streamlit mushroom_detect_app.py

:: 만약 바로 꺼진다면 에러 확인을 위해 일시정지
if %errorlevel% neq 0 (
    echo [에러] 프로그램 실행 중 문제가 발생했습니다.
    pause
)