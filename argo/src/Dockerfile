
FROM python:3.9

ADD __main__.py .
#LABEL contact="Chris Isayan"
#LABEL version="1.0"


# Keeps Python from generating .pyc files in the container
#ENV PYTHONDONTWRITEBYTECODE=1
# Turns off buffering for easier container logging
#ENV PYTHONUNBUFFERED=1
# set image working dir as a relative base
#WORKDIR /project
# copy working dir contents to image
#COPY . .


# copy file (via pip freeze) to image working dir & install image dependencies/requirements
#RUN pip install time sys datetime
#COPY requirements.txt .
#COPY src src/
#RUN python3 -m pip install --upgrade pip
#RUN python3 -m pip install --no-cache-dir -r requirements.txt

#RUN python3 -m venv ve

#CMD . ve/bin/activate && python3 -m
CMD ["python", "./__main__.py"]

