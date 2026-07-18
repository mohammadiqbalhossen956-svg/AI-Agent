from fastapi import FastAPI, Request # Request ইমপোর্ট করা জরুরি

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "AI Agent is running"}

# ডাটা রিসিভ করার জন্য নতুন রুট
@app.post("/webhook")
async def handle_webhook(request: Request):
    data = await request.json() # মেক থেকে আসা ডাটা রিসিভ করা
    print(data) # লগ-এ ডাটা দেখাবে
    return {"status": "success", "received": data}
