# Timealive

WebPage of a scheduling system for hospitals.

## Installation

You'll need to create a python environment for running the Django webserver. It has only been tested on MacOS and Windows. These are the instructions to install on MacOS:

```
git clone https://github.com/Jerry-Master/timealive.git
python3.10 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py. runserver
```

For Windows just change the third command to `.venv\Scripts\activate`. The server will be running at `http://127.0.0.1:8000/`.
