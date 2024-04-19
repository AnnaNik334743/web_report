from fastapi import FastAPI
import yaml

app = FastAPI()


def custom_openapi():
    with open("api_spec.yaml", "r") as file:
        openapi_schema = yaml.load(file, Loader=yaml.FullLoader)
    return openapi_schema


app.openapi = custom_openapi


# GET endpoint to retrieve a greeting message
@app.get("/hello")
async def hello():
    return {"message": "Hello, world!"}


# POST endpoint to create a new greeting message
@app.post("/hello")
async def create_hello(name: str):
    return {"message": f"Hello, {name}! Greeting message created"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
