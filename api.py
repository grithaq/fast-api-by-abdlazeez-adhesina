from fastapi import FastAPI

# Instance fast api object
app = FastAPI()

@app.get("/")
async def welcome_to_the_webinar() -> dict:
    return {
        "message": "Welcome to the webinar!"
    }