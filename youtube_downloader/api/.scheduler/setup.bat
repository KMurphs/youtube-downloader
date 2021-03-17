@REM Create Task
@REM Command must be run with administrator priviledges
SCHTASKS /CREATE /SC DAILY /TN "MyTasks\Youtube Downloader Task" /TR "C:\PersonalProjects\misc\YoutubeDownloader\app\scheduler\task.bat" /ST 01:00

@REM Open Task Scheduler
taskschd.msc