from fastapi import FastAPI, Body, status
from fastapi.responses import JSONResponse, FileResponse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from parser import manage_parser
from dto import Base, Message
from jsonencode import serialize_complex
import json
 
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:example@localhost/postgres"
 
engine = create_engine(SQLALCHEMY_DATABASE_URL)

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autoflush=False, bind=engine)
db = SessionLocal()

app = FastAPI()

DEFAULT_PARSER_URL = 'https://forum.vgd.ru/1693/115157/0.htm'

@app.get("/")
def main():
    content = "Nothing to see here."
    return JSONResponse(content=content)

@app.post("/api/parse/")
async def parse(url: str = DEFAULT_PARSER_URL):
    message_list = manage_parser(url)
    
    for message in message_list: # FYI: add_all() wouldn't work for some reason.
        db.add(message)
        db.commit()
        db.refresh(message)

    content = "Let's just pretend it's positive \"200 OK\" response."
    return JSONResponse(content=content)

@app.get("/api/fetch_parse/")
async def fetch_parse():
    messages = db.query(Message).all()
    return json.dumps(serialize_complex(messages), indent=4)

# @app.get("/api/get_parsed")
