
FROM python:latest

RUN mkdir /pasta_python_AS2

WORKDIR /pasta_python_AS2


COPY *.py ./
#COPY *.* ./
#COPY AS_principal.py ./

CMD ["python","AS_principal2.py"]
#CMD python exemplo.py



#docker pull python:latest
#ADD file:ff01c6dedb67cf22e9b0735e099b9b6367770c4880941862cc7ec0e979b4118b in /
#python:latest

#docker build -t imagem-teste:latest .
#docker run -it imagem-teste:latest

# PARAR O DOCKER, no CMD => wsl --shutdown