폴더명 : v00_install_anaconda
파일명 : v00_install anaconda.md

<설치법>
1. 구글에서 [아나콘다 구버전] 검색
2. osg.kr 사이트 클릭
3. 아카이브 https://repo.anaconda.com/archive/ 접속
4. Anaconda3-2025.12-1-Windows-x86_64.exe 설치
5. 구글에서 [vs 코드] 검색
6. 최신 파일 설치
    설치시 모두 선택
7. 설치후 구글에서 [anaconda 환경변수 변경] 검색 후 실치
 7-1. 윈도우 검색창에서 [시스템 환경 변수 편집] 검색 후 클릭
 7-2. [환경변수] 클릭
 7-3.  시스템변수창의 [path] 두번 클릭
 7-4. 새로 만들기
      C:\Users\Administrator\anaconda3
      C:\Users\Administrator\anaconda3\Library\bin
      C:\Users\Administrator\anaconda3\Library
      C:\Users\Administrator\anaconda3\Scripts
8. CMD 창에서 [conda] 입력
9. [conda create -n py39 python=3.9] 입력
   가상환경 만들기
10. 시작하기 명령어 : conda activate py39
    종료하기 명령어 : conda deactivate
11. 바탕화면에 [PTU]폴더 생서
12. [PTU]폴더를 오른쪽 클릭하여 추가옵션 선택
13. VS 코드 열기 선택
14. 열린 VS코드에 v00_install_anaconda폴더 생성
15. 폴더 내에 v00_install_anaconda.md 파일 생성