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
    
    # Framer ফ্রমের ফিল্ড নেমগুলোর সাথে হুবহু ম্যাচ করা হলো
    full_name = data.get("full_name", "")
    work_email = data.get("work_email", "")
    company_name = data.get("company_name", "")
    budget_range = data.get("budget_range", "")
    message = data.get("message", "")
    
    return {
        "status": "success",
        "full_name": full_name,
        "work_email": work_email,
        "company_name": company_name,
        "budget_range": budget_range,
        "message": message
    }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run("agent:app", host="0.0.0.0", port=port)
