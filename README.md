# cicd_v1
CI/CD Generic Template/Pattern for Quick Production Deployments

## 1. Structure
Create domain driven project structure

### 1.1 Example
[Backend-Entrypoint-Template](https://github.com/eugen-hoppe/cicd_v1/blob/739e9688ba6b186842c86933e0a5b816b7e60d94/backend.py)

## 2. Local App Development
### 2.1 Requirements
#### 2.1.1 App Requirements
- your base framework Django, FastAPI, Flask, etc. 
- Probably an ORM
- Example: [backend/container](https://github.com/eugen-hoppe/cicd_v1/blob/7a3e033a81290abeb7314b84c549bd5adaada981/backend/container/requirements.txt)

#### 2.1.2 Local Dev Dependencies
- dev utils, etc.
- Example: [backend/container/development](https://github.com/eugen-hoppe/cicd_v1/blob/7a3e033a81290abeb7314b84c549bd5adaada981/backend/container/development/requirements.txt)

#### 2.1.3 Production Requirenents Template/Draft
- Example: [backend/container/production](https://github.com/eugen-hoppe/cicd_v1/blob/7a3e033a81290abeb7314b84c549bd5adaada981/backend/container/production/requirements.txt)

### 2.2 Local Environment Setup (Python)

```shell
python3 -m venv .venv
```

```shell
source .venv/bin/activate
```

```shell
pip install -r backend/container/requirements.txt
```

```shell
pip install -r backend/container/development/requirements.txt
```

### 2.3 Add your App to Project Structure

[Example App](https://github.com/eugen-hoppe/cicd_v1/commit/a438b6a17e3a9b5314301aad27cd328882019e20)

```shell
python backend.py
```

- a. [open browser](http://localhost:8008/docs)
- b. Create user
- c. MVC is working?: [check get-request](http://localhost:8008/users/)


## 3. Local Docker Compose Deployment

### 3.1 Container Config
- a. create [docker configuration files](https://github.com/eugen-hoppe/cicd_v1/commit/5d95070d85b6b844b1017fb48d165ea47d160034)
- b. create `.env` in root folder with this [variables](https://github.com/eugen-hoppe/cicd_v1/blob/5d95070d85b6b844b1017fb48d165ea47d160034/env_templates/local/env.txt)
- c. run `docker-compose up -d --build`
- e. open [/users/](http://localhost/users/)
- f. open [/dashboard/](http://localhost/dashboard/#/)
- g. enter user:`USERNAME` and pass:`PASSWORD` (see: [create password](https://github.com/eugen-hoppe/cicd_v1/blob/5d95070d85b6b844b1017fb48d165ea47d160034/env_templates/local/env.txt#L11))
- h. open [/docs](http://localhost/docs)
- i. open [/redoc](http://localhost/redoc)

## 4. Production

### 4.1 Setup server
#### 4.1.1 Configure SSH
- create SSH key (see. [SSH Cheet Sheet](https://gist.github.com/eugen-hoppe/ed1af4aecfac6fe0e322905eb4e7052b))
- with passphrase
- add public key to server
#### 4.1.2 Create GitHub Actions Secrets

##### 4.1.2.1 Pipeline Secrets

```txt
DDCS_DOCKER_USER
```

```txt
DDCS_DOCKER_PW
```

```txt
DDCS_SERVER_USER
```

```txt
DDCS_SERVER_HOST
```

```txt
DDCS_SERVER_SSH_KEY
```

```txt
DDCS_SERVER_SSH_PASSPHRASE
```

###### 4.1.2.1.1 Job Variables

```txt
DDCS_SERVICE_ENV_EP_APP_1_IMAGE
```

> Example format: '???/???:latest'

##### 4.1.2.2 Application Secrets

###### 4.1.2.2.1 Multiple Variables as Single Secret

```txt
DDCS_SERVICE_ENV_CONFIG
```
###### 4.1.2.2.2 Template for DDCS_SERVICE_ENV_CONFIG

```txt
EP_DC_YML='entrypoint/https/'
EP_DOMAIN='???'
EP_LE_EMAIL='???'
EP_PROTOCOL_LABEL='websecure'
EP_APP_1_AUTH_PATH_PREFIX_1='docs'
EP_APP_1_AUTH_PATH_PREFIX_2='redoc'
EP_APP_1_AUTH_PATH_PREFIX_3='openapi.json'
EP_APP_1_PORT='8010'
EP_APP_1_DB_NAME='postgres'
EP_APP_1_DB_USER='postgres'
```

###### 4.1.2.2.3 Single Sensitive Application Secrets

```txt
DDCS_SERVICE_ENV_SECRET_EP_APP_1_DB_PASSWORD
```

```txt
DDCS_SERVICE_ENV_SECRET_EP_AUTH_USER_AND_HASH
```

### 4.2 Configure CICD Workflow

#### 4.2.1 Template

Create [cicd.yml](https://github.com/eugen-hoppe/cicd_v1/blob/d009de68a5ebe4dd6d0d45f5b11d59ba565e5136/.github/workflows/cicd.yml)

#### 4.2.2 Set up jobs

#### 4.2.2.1 Tests
- add [backend/container/workflow/requirements.txt](https://github.com/aiuminet/ddcs/blob/main/backend/container/workflow_tests/requirements.txt)
- check why [job is failed](https://github.com/eugen-hoppe/cicd_v1/actions/runs/7467832148/job/20322100898)
- add [test_example.py](https://github.com/eugen-hoppe/cicd_v1/blob/e7e8cf366c059a2cc957a8cf9a4f2f3c35128941/backend/application/tests/test_example.py) to test folder

