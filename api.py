from fastapi import FastAPI

# Instance fast api object
app = FastAPI()

#attendes
attendes = []

@app.get("/")
async def welcome_to_the_webinar() -> dict:
    return {
        "message": "Welcome to the webinar!"
    }

@app.post("/attend")
async def register_for_the_webinar(name: str):
    attendes.append(name)
    return {
        "message" : f"Dear {name}, you have successfully registeredfor the webinar "
    }