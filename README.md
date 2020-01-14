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

There 3 different modules, that solve 3 diffent tasks(test1, test2 and test3). To execute them, just copy the command below, replacing the test name with the test you want to execute. The output file(output.json) will be placed inside a folder with the name of the test.

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
