from fastapi import FastAPI, Body, status
from fastapi.responses import JSONResponse, FileResponse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from parser import manage_parser
from dto import Base, Message, URL
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
    # message_list = manage_parser(url)
    
    # for message in message_list: # FYI: add_all() wouldn't work for some reason.
    #     db.add(message)
    #     db.commit()
    #     db.refresh(message)

    content = "Legacy method. Access restricted."
    return JSONResponse(content=content)

@app.get("/api/fetch_parse/")
async def fetch_parse():
    # messages = db.query(Message).all()
    # return json.dumps(serialize_complex(messages), indent=4)

    content = "Legacy method. Access restricted."
    return JSONResponse(content=content)

@app.post("/api/add-url")
async def add_url(url: str = DEFAULT_PARSER_URL):
    url_obj = URL(url = url)
    db.add(url_obj)
    db.commit()
    db.refresh(url_obj)

    content = "200 OK."
    return JSONResponse(content=content)

@app.get("/api/get-urls/")
async def get_urls():
    urls = db.query(URL).all()
    return json.dumps(serialize_complex(urls), indent=2)
