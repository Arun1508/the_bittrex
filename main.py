import argparse
from contextlib import asynccontextmanager

import uvicorn
from dotenv import load_dotenv
from fastapi import Depends, FastAPI

from routes import main
from utils.user_auth import get_current_username


@asynccontextmanager
async def lifespan(app: FastAPI):
    load_dotenv(r"./config.env")
    yield


app = FastAPI(lifespan=lifespan)


app.include_router(main.routes, dependencies=[Depends(get_current_username)])


if __name__ == "__main__":
    arg = argparse.ArgumentParser()

    arg.add_argument("-p", "--port", required=False, help="Server port number")
    arg.add_argument(
        "-d",
        "--develop",
        required=False,
        action="store_true",
        help="Start server with developer mode.",
    )
    arg.add_argument("-ip", "--ip", required=False, help="Start server at ip")
    args_passed, unknown = arg.parse_known_args()
    PORT = int(args_passed.port) if args_passed.port else 8001
    RELOAD = args_passed.develop
    HOST = args_passed.ip if args_passed.ip else "0.0.0.0"
    uvicorn.run("main:app", host=HOST, port=PORT, reload=RELOAD)
