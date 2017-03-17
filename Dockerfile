# VERSION 0.0.1

FROM ubuntu
MAINTAINER David Gwizdala "gwizdala@vt.edu"

#install dependencies
RUN apt-get update && apt-get install -y \
	git \
	python3.4 \
	python3-pip

#update pip
RUN pip3 install --upgrade pip

#download flask-server
RUN pip3 install Flask-API
RUN pip install Flask-API
RUN pip install flask
RUN pip3 install flask
RUN pip3 install markdown
RUN pip install python-firebase

#clone the git repository
RUN git clone https://github.com/ldevr2t1/RoboSim.git

#move into the server folder
WORKDIR "/RoboSim"

#move to the correct branch
RUN git checkout assignment_6

WORKDIR "python-flask-server"

#install the requirements for the server
RUN pip3 install -r requirements.txt

#Expose port 8080 for testing
EXPOSE 5050

#start the server
CMD python3 -m swagger_server

