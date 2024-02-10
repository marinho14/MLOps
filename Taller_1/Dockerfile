# 
FROM python:3.11

# 
WORKDIR /code

# 
COPY requirements.txt /code/requirements.txt
COPY models /code/models
COPY penguins_api.py /code/penguins_api.py

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
CMD ["uvicorn", "penguins_api:app", "--host", "0.0.0.0", "--port", "80"]