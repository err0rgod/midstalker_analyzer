FROM python:3.10-slim

# working directory
WORKDIR /app

# copy files
COPY . /app

# for dependencies
RUN pip install --no-cache-dir -r requirements.txt

# exposing stream lit port
EXPOSE 8501

# Running app

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=
