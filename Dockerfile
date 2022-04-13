# init a base image (Alpine is small Linux distro)
FROM python:3.7.3-alpine
# define the present working directory
WORKDIR /rtu_sc
# copy the contents into the working dir
ADD . /docker-rtu_sc-test
# run pip to install the dependencies of the flask app
RUN pip install -r requirements.txt
# define the command to start the container
CMD ["python","rtu-sc.py"]


#comandos para docker
#crear imagen
#docker image build -t docker-rtu_sc-test .
