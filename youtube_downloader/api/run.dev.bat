@ECHO OFF


ECHO Set environment variables
CD app
SET FLASK_APP=api.py
SET FLASK_DEBUG=1
CD 

ECHO Running Flask Application
..\venv\Scripts\python -m flask run
CD ..