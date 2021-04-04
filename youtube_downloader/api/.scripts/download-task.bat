@echo off
@REM CD ..
@REM CD %~dp0
@REM CD..
@REM venv\scripts\python app\downloader.py
@REM /bin/python3.9 /youtube_downloader/app/downloader.py


docker exec -t youtube_downloader_backend_app_1 /bin/python3.9 /youtube_downloader/app/downloader.py

explorer videos