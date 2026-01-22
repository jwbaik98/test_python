@echo off
:: 한글 깨짐 방지를 위한 코드 페이지 변경 (UTF-8)
chcp 65001 >nul

echo 🍄 [알림] 필요한 라이브러리를 설치합니다...
echo.

python -m pip install --upgrade pip
if %errorlevel% neq 0 (
    echo ❌ pip 업그레이드 중 오류가 발생했습니다.
)

pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ❌ 라이브러리 설치 중 오류가 발생했습니다. 'requirements.txt' 파일을 확인해 주세요.
)

echo.
echo ✨ 설치가 완료되었습니다! 이제 'mushroom_detect.bat'을 실행하세요.
echo.
pause