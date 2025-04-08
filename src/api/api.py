from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Message(BaseModel):
    query: str


@app.post("/")
def receber_mensagem(message: Message):
    print(message)
    return {"mensagem_recebida": message.query}
