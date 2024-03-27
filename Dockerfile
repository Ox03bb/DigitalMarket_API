FROM python:3.11

RUN apt update && apt upgrade 
WORKDIR /app
RUN pip install --upgrade pip

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
# RUN pip install -r requirements.txt 
# RUN python3 manage.py makemigrations
# RUN python3 manage.py migrate

# CMD ["python3"]
# CMD [ "echo","complet" ]



# Copy project code


# Expose port for Django application (default: 8000)

