# serverless-flask-playground

Example of running python [Flask](https://flask.palletsprojects.com/) app on Lambda + API Gateway via [serverless framework](https://www.serverless.com/).  Based on [Build a Python REST API with Serverless, Lambda, and DynamoDB](https://www.serverless.com/blog/flask-python-rest-api-serverless-lambda-dynamodb).

## Architecture

![](https://s3-us-west-2.amazonaws.com/assets.site.serverless.com/guides/serverless-flask/serverless-flask-architecture.png)

## Prerequisites

* [serverless framework](https://www.serverless.com/)
* [Docker Desktop](https://www.docker.com/products/docker-desktop)
* Python 3.8
* [pipenv](https://github.com/pypa/pipenv)

## Running

```sh
# ensure python venv loaded in shell
pipenv shell

# install npm deps for serverless
npm install

# run flash app locally.  server reloads on file change.  still need to refresh page in browser
npm run dev

# deploy. (docker must be running to build python packages for linux target / lambda)
npm run deploy
```

## Resources

* [The Official Guide to Serverless Flask](https://www.serverless.com/flask)
* [Build a Python REST API with Serverless, Lambda, and DynamoDB](https://www.serverless.com/blog/flask-python-rest-api-serverless-lambda-dynamodb)