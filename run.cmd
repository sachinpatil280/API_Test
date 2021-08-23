REM set PYTHONPATH=%PYTHONPATH%;C:\Coding\API-Test-Automation

REM set PYTHONPATH=%PYTHONPATH%;os.path.dirname(os.getcwd())

SET SEARCHPATH=%~dp0%\tests\
cd %SEARCHPATH%

pytest -m "regression" --html=..\\Reports\\report.html
REM python -m pytest