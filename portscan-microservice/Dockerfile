FROM ubuntu
WORKDIR /app
COPY . /app
RUN apt-get update -yq \
    && apt-get install curl gnupg -yq \
    && apt-get install python2.7 python-pip  -yq \
    && python -m pip install -r requirements.txt\
    && apt-get install nmap -yq
EXPOSE 4000 
# RUN groupadd -g 999 appuser && \
#     useradd -r -u 999 -g appuser appuser
# USER appuser
CMD [ "python", "portscan.py" ]