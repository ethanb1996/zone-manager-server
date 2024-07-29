FROM python:3.12-slim

ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN python -m venv $VIRTUAL_ENV

WORKDIR /app

COPY requirements.txt .

RUN /bin/bash -c "source $VIRTUAL_ENV/bin/activate && pip install --no-cache-dir -r requirements.txt"

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
