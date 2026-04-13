# syntax=docker/dockerfile:1

# Use uv's Alpine image which includes Python
FROM ghcr.io/astral-sh/uv:alpine

WORKDIR /python-docker

COPY . .
RUN uv sync


CMD [ "uv", "run", "python", "-m" , "flask", "--app", "run",  "run", "--host=0.0.0.0" ]

