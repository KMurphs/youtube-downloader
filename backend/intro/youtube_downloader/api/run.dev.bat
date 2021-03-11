@ECHO OFF


CD /app
SET FLASK_APP=__init__.py
SET FLASK_DEBUG=1
flask run
CD ..