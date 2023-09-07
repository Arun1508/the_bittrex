import argparse
from contextlib import asynccontextmanager

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

from routes import main


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Loading configuration files
    Args: app : Pass in Fastapi object
    """
    load_dotenv(r"./config.env")
    yield


app = FastAPI(lifespan=lifespan)

# Adding routes to Fastapi
app.include_router(main.routes)


if __name__ == "__main__":
    arg = argparse.ArgumentParser()
    # Adding arg -p/--p to setup port no
    arg.add_argument("-p", "--port", required=False, help="Server port number")
    # Adding arg -d/--d to if develop is set to true server will restart on files change.
    arg.add_argument(
        "-d",
        "--develop",
        required=False,
        action="store_true",
        help="Start server with developer mode.",
    )
    # Adding arg -ip/--ip to setup host ip
    arg.add_argument("-ip", "--ip", required=False, help="Start server at ip")
    args_passed, unknown = arg.parse_known_args()

    PORT = int(args_passed.port) if args_passed.port else 8001
    RELOAD = args_passed.develop
    HOST = args_passed.ip if args_passed.ip else "0.0.0.0"
    uvicorn.run("main:app", host=HOST, port=PORT, reload=RELOAD)
