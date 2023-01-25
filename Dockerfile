FROM python:3.10
COPY requirements.txt .
RUN pip install django
RUN pip install --no-cache-dir -r requirements.txt
RUN
RUN python -m spacy download en_core_web_md
WORKDIR /app
COPY . /app
EXPOSE 8000
ENTRYPOINT ["python", "Project_Django/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]