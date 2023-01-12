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

@app.get("/attendees")
async def retrieve_attendees() -> dict:
    return {
        "attendees" : attendes
    }

@app.get('/attendees/{name}')
async def retrieve_attendees_by_name(name: str) -> dict:
    if name in attendes:
        return {
            "Attendees": name
        }
    return {
        "messages": "There is no attendee maching this name"
    }