#!/bin/sh

uvicorn src.main:app \
    --host 0.0.0.0 \
    --port 8080 \
    --workers 4 \
    --log-level info