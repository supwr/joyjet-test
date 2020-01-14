## Joyjet Test

### Install

### Python 3.7.2

#### Clone repo
```sh 
git clone https://github.com/supwr/joyjet-test
```

#### Create virtualenv
```sh 
cd joyjet-test
virtualenv venv
```

#### Activate virtualenv
```sh 
.\venv\Scripts\activate (On Windows)
source env/bin/activate (On Linux)
```

#### Install packages
```sh 
pip install -r requirements.txt
```

### Executing the application

For Linux and Mac:

```sh
export FLASK_APP=app
export FLASK_ENV=development
flask run
```

For Windows cmd, use set instead of export:

```sh
set FLASK_APP=app
set FLASK_ENV=development
flask run
```
