FROM python:3.12
LABEL authors="jeronimo"

WORKDIR /hireNow
COPY requirements.txt /hireNow/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /hireNow/requirements.txt

COPY . /hireNow

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0" ]
