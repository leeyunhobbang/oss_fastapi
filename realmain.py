from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/") #주소(0.0.0.0/)
async def welcome() -> dict:
  return {
        "msg" : "Hello world!"
    } #json파일 형태
     
if __name__ == '__main__':
    uvicorn.run("main:app", host= "0.0.0.0", port = 8000, reload = True) # host  = local주소
