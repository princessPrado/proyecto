# Bring in lightweight dependencies

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def scoring_enpoint():
    return {"hello":"world"}