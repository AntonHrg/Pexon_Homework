FROM python:3.10

# ein neues Directory wird erstellt
RUN mkdir /usr/src/app/

# die Dateien aus der Schulungs Applikation werden in das Directory kopiert
COPY . /usr/src/app/

# das Directory wird als das working directory gesetzt
WORKDIR /usr/src/app/

# lässt den Port 5000 von außen erreichen
EXPOSE 5000

# die Requirements aus der requirements.txt werden installiert
RUN pip install -r requirements.txt

# die Applikation wird ausgeführt
CMD ["python", "app.py"]