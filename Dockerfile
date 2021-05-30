FROM centos

RUN yum install python3 git -y 
RUN pip3 install flask joblib numpy sklearn

RUN git clone https://github.com/pewxh/salary-prediction-flask 

WORKDIR /salary-prediction-flask/FLASK

EXPOSE 5000


CMD [ "python3" , "./app.py"]