@echo off
@REM cd ..
CD %~dp0
CD..
venv\scripts\python app\downloader.py
explorer videos