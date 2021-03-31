@ECHO OFF
@REM .\.scripts\post-video.bat 
@REM .\.scripts\post-video.bat "localhost:5000"
@REM .\.scripts\post-video.bat "youtube.downloader.local/api"

set URL=%1
if "%URL%" == "" (
    set URL=youtube.downloader.local/api
) 

@REM ECHO -XPOST "%URL%/videos/new" -H "Content-Type: application/json" -d"{\"url\": \"https://www.youtube.com/watch?v=7IS7gigunyI\", \"resolution\":720, \"tags\":[\"nginx\"]}"
curl -XPOST "%URL%/zip" -H "Content-Type: application/json" -d@"%~dp0zip-videos.json" -v