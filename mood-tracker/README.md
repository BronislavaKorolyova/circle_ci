#  Mood Tracker App

A simple web app that allows users to track their mood daily with optional notes.  
Built with **FastAPI** (backend) and **HTML + JavaScript** (frontend).

---

##  Features

- Select your mood from a list
- Add an optional personal note
- See a list of all past entries with timestamps
- Data stored in memory (no DB required)
- Easily extensible to include database, charts, or user login

---

##  Project Structure

mood-tracker/
├── client/
│ └── index.html # Frontend page
├── server/
│ ├── main.py # FastAPI backend
│ └── requirements.txt # Python dependencies
└── .circleci/
└── config.yml # CircleCI pipeline config


---

##  Requirements

- Python 3.10+
- pip

---

##  Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/mood-tracker.git
cd mood-tracker

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r server/requirements.txt


Start the FastAPI server:

uvicorn server.main:app --reload

Then open your browser and visit:
 http://localhost:8000


