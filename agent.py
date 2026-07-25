from fastapi import FastAPI, Request

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
