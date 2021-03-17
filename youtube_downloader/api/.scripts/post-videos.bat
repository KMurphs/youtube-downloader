@echo off
curl -XPOST "localhost:5000/videos/new/bulk" -H "Content-Type: application/json" -d@"%~dp0post-videos.json"
echo.