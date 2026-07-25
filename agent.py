from fastapi import FastAPI, Request
import os
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "AI Agent is running"}

@app.post("/webhook")
async def receive_webhook(request: Request):
    data = await request.json()
    
    # এখানে রিকোয়েস্টের ডেটাগুলো রিসিভ হচ্ছে
    name = data.get("name")
    email = data.get("email")
    message = data.get("message")
    
    # রেসপন্সে আবার নাম, ইমেইল এবং মেসেজ ব্যাক পাঠানো হচ্ছে, যাতে Make.com সেটি হাবস্পটে নিতে পারে
    return {
        "name": name,
        "email": email,
        "message": message
    }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run("agent:app", host="0.0.0.0", port=port)
