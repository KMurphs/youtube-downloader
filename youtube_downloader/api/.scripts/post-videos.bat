@echo off


set URL=%1
if "%URL%" == "" (
    set URL=youtube.downloader.local/api
) 

curl -XPOST "%URL%/videos/new/bulk" -H "Content-Type: application/json" -d@"%~dp0post-videos.json"
echo.