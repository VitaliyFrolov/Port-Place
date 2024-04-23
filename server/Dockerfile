FROM python:3.12 as builder

WORKDIR /app/server

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

FROM python:3.12

WORKDIR /app/server

COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/server/requirements.txt .

RUN pip install --no-cache /wheels/*

COPY . .