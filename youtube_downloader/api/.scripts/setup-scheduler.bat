@ECHO OFF
@REM Create Task

@REM Command must be run with administrator priviledges
SCHTASKS /CREATE /SC DAILY /TN "MyTasks\Youtube Downloader Task" /TR "%~dp0download-task.bat" /ST 01:00

@REM Setup venv
CD %~dp0
CD..
python -m venv venv
venv\scripts\pip install -r requirements.txt

@REM Open Task Scheduler
taskschd.msc