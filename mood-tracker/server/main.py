from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from datetime import datetime
from pathlib import Path

# Define absolute path to the client directory
BASE_DIR = Path(__file__).resolve().parent.parent  # goes from server/ to mood-tracker/
CLIENT_DIR = BASE_DIR / "client"

app = FastAPI()
app.mount("/static", StaticFiles(directory=CLIENT_DIR), name="static")

mood_log = []

@app.get("/", response_class=HTMLResponse)
def serve_page():
    index_path = CLIENT_DIR / "index.html"
    with open(index_path, encoding="utf-8") as f:
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

