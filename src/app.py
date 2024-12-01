from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

@app.post("/webhook")
async def webhook_endpoint(request: Request):
    try:
        body = await request.body()
        # Log or process the message here
        print(f"Received message: {body}")
        
        return {
            "status": "success",
            "message": "Webhook received successfully"
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/")
async def root():
    return {"message": "Webhook server is running"}