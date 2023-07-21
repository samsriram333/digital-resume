import subprocess

def streamlit_handler(request):
    response = subprocess.check_output(["streamlit", "run", "main.py"])
    return {"statusCode": 200, "body": response}
