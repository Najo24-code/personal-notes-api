from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import init_db
from auth import router as auth_router, User
from routes.jwt import router as jwt_router

app = FastAPI(title="API_de_notas_personales_con_Fa")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    init_db()

@app.get("/")
def root():
    return {"status": "ok", "project": "API_de_notas_personales_con_Fa", "auth": "/auth/login, /auth/register, /auth/me"}

app.include_router(auth_router)
app.include_router(jwt_router, prefix='/jwt')