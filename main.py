print ("안녕하세요")

from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
  return {
      "msg" : "Hello world!"
      }
     
if __name__ == '__main__':
  uvicorn.run("main:app", host= "0.0.0.0", port = 8000, reload = Ture)
