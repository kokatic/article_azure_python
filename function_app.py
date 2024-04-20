import azure.functions as func

import fastapi

fastapi_app = fastapi.FastAPI()

@fastapi_app.get("/hello/{name}")
async def get_name(name: str):
    return f'Hello {name}'

app = func.AsgiFunctionApp(app=fastapi_app, http_auth_level=func.AuthLevel.ANONYMOUS)