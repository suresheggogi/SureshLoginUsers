#!/bin/bash

echo "=========================================="
echo "Starting Django Application"
echo "=========================================="

echo "Step 1: Applying database migrations..."
python -u manage.py migrate --noinput || echo "Migration note: tables may already exist"

echo "Step 2: Marking existing tables as migrated..."
python -u manage.py migrate --fake postgresApp 0001 --noinput || echo "Fake migration note: already applied"

echo "Step 3: Applying remaining migrations..."
python -u manage.py migrate --noinput || echo "No additional migrations"

echo "=========================================="
echo "READY: Starting Django development server"
PORT=${PORT:-8000}
echo "Server will run on http://0.0.0.0:$PORT/"
echo "=========================================="

python -u manage.py runserver 0.0.0.0:$PORT
