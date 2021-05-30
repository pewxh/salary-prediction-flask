# Salary Prediction Using Flask

## Some "high" level intro:

<p align="center">
<h3>    <b>Jupyter Notebook</b> provided was used to train this model, and the model is then saved in a binary file. <br>
    <b>Flask App</b> uses the binary file to load the model, gets the input through user, then <b>RESTful API</b> is used to transfer the request to the Flask Server, where data is processed and result is then forwarded using <b>HTML</b> templates.
</h3>
</p>
<p align="center"><a href="#" target="_blank"><img src="https://forthebadge.com/images/badges/uses-html.svg" alt="html" /></a>&nbsp;&nbsp;<a href="# target="_blank"><img src="https://forthebadge.com/images/badges/made-with-python.svg" alt="python" /></a>&nbsp;
<a href="# target="_blank"><img src="https://forthebadge.com/images/badges/no-ragrets.svg" alt="no ragrets" /></a>&nbsp;</a>&nbsp;
<a href="# target="_blank"><img src="https://forthebadge.com/images/badges/fo-sho.svg" alt="foso" /></a>&nbsp;
</p>

## ⚡️ Quick start

<hr>

First of all, [download](https://www.python.org/downloads/) and install **Python**. <br>
Install flask , joblib , numpy and sklearn modules using pip/pip3.

```pip
pip3 install flask joblib numpy sklearn
```

Next, change directory to /FLASK and run the file (called `app.py`) using python/python3 to start your **Flask Server**. <br>
Use **localhost:5000** to visit the app.

```bash
python3 ./FLASK/app.py
```

### 🐳 Docker

You can use docker container to launch the app.
Feel free to use this [Docker image](https://hub.docker.com/repository/docker/pewxh/salary-prediction-flask) and run CLI from isolated container:

```bash
docker run -d -p 5000:5000 pewxh/salary-prediction-flask
```

<i><b>- p</b> is used to publish the port number 5000 of the container to that of our hostmachine.</i>

## 📖 Detailed Explaination

Read this [Article](https://pewxh.medium.com/deploying-an-ml-model-inside-a-docker-container-using-flask-17c895b1285e) for better understanding.
