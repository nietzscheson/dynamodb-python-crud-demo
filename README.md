[PynamoDB - ODM](https://pynamodb.readthedocs.io/en/latest/) (DynamoDB) Python CRUD Demo
==============

Make sure to use Docker and Python > 3.9

# Installation

1. First, clone this repository:

```bash
$ git clone git@github.com:nietzscheson/pynamodb-crud
```
2. Pull the DynamoDB Docker service and install project dependencies
```bash
$ make
```
***The before make command start all necesary containers to run the application.***

3. Show containers:
```bash
$ make ps
```
This results in the following running containers:

```bash
> $ docker-compose ps
NAME                COMMAND                  SERVICE             STATUS              PORTS
dynamodb            "java -jar DynamoDBL…"   dynamodb            running             0.0.0.0:8000->8000/tcp
```
___

4. If you love the automation testing, please run:
```bash
$ make test
```
