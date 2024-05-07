import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db
from fastapi import HTTPException
from sqlalchemy.orm import sessionmaker

from router import UserRouter
from router import ProjectRouter


import os
from dotenv import load_dotenv

import os
from dotenv import load_dotenv

load_dotenv('.env')


app = FastAPI()


# to avoid csrftokenError
app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])

app.include_router(UserRouter.router, prefix="/api")
app.include_router(ProjectRouter.router, prefix="/api")



# To run locally
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)