rem Build exe file from Python code

rem cfr. https://pyinstaller.org/en/stable/spec-files.html#adding-data-files

rem https://qiita.com/bass_clef_/items/1d0f7b987223f9ddc9f6

@echo off

setlocal

rem 引数チェック

if "%~1"=="" (

    echo 引数がありません

    echo 引数にPythonコードを指定してください

    echo "py2exe.bat XXXX.py"

    exit /b

)

set pyinstaller=D:\python\python-3.9.7\Scripts\pyinstaller.exe

rem  引数No.1に .py コードを指定

rem %pyinstaller% --paths D:\Python\Python-3.9.7\Lib --add-data D:\Python\tools\extract_draw\Tesseract-OCR500;tesseract --collect-all pyocr --onefile -w %1

%pyinstaller% -i search.ico --collect-all pyocr --onedir getControl.spec

endlocal
