import fastapi
import uvicorn

api = fastapi.FastAPI()

@api.get("/")
def endpoint():
    return {"msg": "a"}


uvicorn.run(api, port=9000)

