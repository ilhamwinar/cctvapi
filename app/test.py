from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import ast
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from passlib.context import CryptContext
import os

#variable declaration
app = FastAPI()
security = HTTPBasic()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
f = open('./temp.txt', 'r')
api=f.read()
dictapi = ast.literal_eval(api)
id_cctv=dictapi['id']
id_cctv_temp=id_cctv
g = open('./config.txt', 'r')
ip_api=g.read()
dictip = ast.literal_eval(ip_api)
ip_jetson=dictip['ip']

PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return PWD_CONTEXT.hash(password)
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return PWD_CONTEXT.verify(plain_password, hashed_password)

def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    current_username_bytes = credentials.username
    correct_username_bytes = "$2b$12$EZxJr9jH9UzeCUJ3Gz/NAOS1GWpY3RloaopyuK7lRhPSROONEN6uS"
    is_correct_username=verify_password(current_username_bytes, correct_username_bytes)
    current_password_bytes = credentials.password
    correct_password_bytes = "$2b$12$/TvmToFip27Gqnnv7xfareDeHD6MWp3J1sVn00joiTaR2vn/eT7Q2"
    is_correct_password=verify_password(current_password_bytes, correct_password_bytes) 
    
    if not (is_correct_username and is_correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

@app.get("/cctv/{id_cctv}")
async def read_current_user(id_cctv,username: str = Depends(get_current_username)):
    if id_cctv_temp != id_cctv:
        raise HTTPException(status_code=400, detail="Wrong CCTV Location") 
 
    f = open('./temp_result.txt', 'r')
    api=f.read()
    dictapi = ast.literal_eval(api)
    return dictapi

if __name__ == "__main__":
    uvicorn.run("test:app", host=ip_jetson, port=90,log_level="info",reload=True)
