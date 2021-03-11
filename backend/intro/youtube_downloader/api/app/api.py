# https://github.com/microsoft/pylance-release/issues/236#issuecomment-759828693
# import app
# from app import app

# from __init__ import app
# from __main__ import app
from app import app

print("*******************")
# print(dir(app))
@app.route('/')
def hello_world():
    print("----------------")
    return 'Hello, World! from API'