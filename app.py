from flask import Flask
# import request
# import os
# import json
# import requests
# from dotenv import load_dotenv

# Load .env values
# load_dotenv()

app = Flask(__name__)

# API_KEY = os.getenv("CRON_JOB_API_KEY")
# CRON_JOB_ID = "12345"  # <-- put your real job ID here
# ENDPOINT = "https://api.cron-job.org"

# def update_cron_job():
#     """Updates cron-job.org job settings."""
#     headers = {
#         "Authorization": API_KEY,
#         "Content-Type": "application/json"
#     }

#     payload = {
#         "job": {
#             "enabled": True
#         }
#     }

#     try:
#         response = requests.patch(
#             f"{ENDPOINT}/jobs/{CRON_JOB_ID}",
#             headers=headers,
#             json=payload   # cleaner than json.dumps()
#         )
#         return response.json()
#     except Exception as e:
#         return {"error": str(e)}

# def run_task():
#     print("The scheduled task is running!")
#     # your actual task here

# @app.route("/run", methods=["GET"])
# def trigger():
#     key = request.headers.get("X-API-Key")

#     if key != API_KEY:
#         return {"error": "Unauthorized"}, 401

#     run_task()
#     return {"status": "Task executed"}

# @app.route("/update-job", methods=["GET"])
# def update_job():
#     key = request.headers.get("X-API-Key")
    
#     if key != API_KEY:
#         return {"error": "Unauthorized"}, 401

#     result = update_cron_job()
#     return result


@app.route("/", methods=["GET"])
def home():
    return {"message": "Hello, Vercel!"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
