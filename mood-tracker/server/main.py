from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from datetime import datetime

app = FastAPI()
app.mount("/static", StaticFiles(directory="client"), name="static")

mood_log = []

@app.get("/", response_class=HTMLResponse)
def serve_page():
    with open("client/index.html") as f:
        return f.read()

@app.post("/submit")
def submit_mood(mood: str = Form(...), note: str = Form("")):
    mood_log.append({
        "mood": mood,
        "note": note,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    return {"success": True}

@app.get("/moods")
def get_moods():
    return {"entries": mood_log}

