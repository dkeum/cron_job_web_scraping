import os

def run_task(api_key):
    print("Running task with API key:", api_key)
    # your logic here

def main():
    api_key = os.getenv("CRON_JOB_API_KEY")

    if not api_key:
        raise ValueError("CRON_JOB_API_KEY not found in environment variables")

    run_task(api_key)

if __name__ == "__main__":
    main()
