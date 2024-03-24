FROM python:3.11

RUN apt update && apt upgrade 
WORKDIR /app
RUN pip install --upgrade pip

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY wait-for-it.sh . 
RUN chmod +x wait-for-it.sh


COPY . .
 
RUN python manage.py makemigrations

CMD ["./wait-for-it.sh", "db:3306", "&&", "python", "manage.py", "migrate"]
# CMD [wait-for-it.sh     , "--", "python", "manage.py", "migrate"]
#5432
# CMD [ "python", "manage.py", "runserver"]