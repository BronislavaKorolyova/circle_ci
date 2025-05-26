# Stage 1: install and test
FROM python:3.11-slim AS test

WORKDIR /app

COPY server/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir pytest httpx

COPY server/ server/
COPY client/ client/

RUN PYTHONPATH=/app pytest server/tests

# Stage 2: production image
FROM python:3.11-slim

WORKDIR /app

# Copy everything from test stage
COPY --from=test /app /app

#  Reinstall requirements in the final image
RUN pip install --no-cache-dir -r server/requirements.txt

EXPOSE 8000

CMD ["uvicorn", "server.main:app", "--host", "0.0.0.0", "--port", "8000"]

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD curl --fail http://localhost:8000/moods || exit 1


