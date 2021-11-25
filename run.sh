#!/bin/bash
uvicorn main:api --host 0.0.0.0 --port 30010 --log-level info --reload
