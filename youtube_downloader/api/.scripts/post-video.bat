@ECHO OFF
@REM .\.scripts\post-video.bat 
@REM .\.scripts\post-video.bat "youtube.downloader.local/api"

set URL=%1
if "%URL%" == "" (
    set URL=localhost:5000
) 

@REM ECHO -XPOST "%URL%/videos/new" -H "Content-Type: application/json" -d"{\"url\": \"https://www.youtube.com/watch?v=7IS7gigunyI\", \"resolution\":720, \"tags\":[\"nginx\"]}"
curl -XPOST "%URL%/videos/new" -H "Content-Type: application/json" -d@"%~dp0post-video.json" -v