from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class WebhookMessage(BaseModel):
    text: str
    sender: Optional[str] = None
    timestamp: Optional[str] = None

@app.post("/webhook")
async def webhook_endpoint(message: WebhookMessage):
    try:
        # Log or process the message here
        print(f"Received message: {message.message}")
        print(f"From: {message.sender}")
        print(f"At: {message.timestamp}")
        
        return {
            "status": "success",
            "message": "Webhook received successfully",
            "data": message.dict()
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/")
async def root():
    return {"message": "Webhook server is running"}