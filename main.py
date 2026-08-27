from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return {"mensaje": "Mi API esta funcionando"}

@app.get("/eventos")
def listar_eventos():
    return{"eventos": ["CONNITI 2024", "Taller React", "Charla AI"]}
