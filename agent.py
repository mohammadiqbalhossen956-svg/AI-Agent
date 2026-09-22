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
    
    # এখানে রিকোয়েস্টের ডেটাগুলো রিসিভ করা হচ্ছে (নাম, ইমেল, ফোন, জন্মতারিখ এবং মেসেজ)
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    email = data.get("email")
    phone_number = data.get("phone_number")
    date_of_birth = data.get("date_of_birth")
    message = data.get("message")
    
    # রেসপন্সে ফিল্ডগুলো ব্যাক পাঠানো হচ্ছে, যাতে Make.com সেটি হাবস্পটে নিতে পারে
    return {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone_number": phone_number,
        "date_of_birth": date_of_birth,
        "message": message
    }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run("agent:app", host="0.0.0.0", port=port)
