from fastapi import FastAPI, Request
import os
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "online", "message": "AI Agent is running"}

@app.post("/webhook")
async def receive_webhook(request: Request):
    try:
        data = await request.json()
    except Exception:
        data = {}
    
    # Safely extract form fields from incoming webhook payload
    first_name = data.get("first_name", "")
    last_name = data.get("last_name", "")
    email = data.get("email", "")
    phone_number = data.get("phone_number", "")
    date_of_birth = data.get("date_of_birth", "")
    message = data.get("message", "")
    
    # Return structured fields to Make.com for HubSpot CRM mapping
    return {
        "status": "success",
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone_number": phone_number,
        "date_of_birth": date_of_birth,
        "message": message
    }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    # Change "agent:app" to "main:app" if your file is named main.py
    uvicorn.run("agent:app", host="0.0.0.0", port=port)
