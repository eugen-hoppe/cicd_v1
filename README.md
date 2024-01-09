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


