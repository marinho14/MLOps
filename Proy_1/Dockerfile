# Docker python image
FROM tensorflow/tfx:1.12.0

# set working directory
WORKDIR /home/proy1/src

# copy requirements.txt file
# COPY requirements.txt /home/proy1/src/requirements.txt

# install requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# keep alive command
# CMD ["bash", "-c", "while true; do echo 'Container is running...'; sleep 10; done"]