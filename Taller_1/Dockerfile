# 
FROM python:3.11

#
COPY requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
WORKDIR /code

# 
COPY models /code/models
COPY encoders /code/encoders
COPY penguins_api.py /code/penguins_api.py

# 
CMD ["uvicorn", "penguins_api:app", "--host", "0.0.0.0", "--port", "80"]