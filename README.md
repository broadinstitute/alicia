# Alicia
Key/value store service for Firecloud. 
Alicia is a Google Endpoints application written in Python 2.7.

# Dependencies 
In order to run tests or run the local development app server, you need to install Python 2.7, Pip, and [Google Cloud SDK](https://cloud.google.com/sdk/install).

# Running Locally
### Virtualenv

Virtualenv is a tool that helps you manage multiple Python versions and your project dependencies. We recommend you setup Virtualenv for development and testing of Bond.

* Verify that you have Python 2.7 installed: `python --version` (Note: The name of your Python 2.7 command may be something different like python2 if you have multiple versions of Python installed)
* Install virtualenv: `pip install virtualenv`
* `cd` to the Alicia root directory
* Set up virtualenv for Alicia: `virtualenv -p python env` (Note: Ensure that you pass the correct Python 2.7 executable to the -p parameter)
* Activate virtualenv: `source env/bin/activate`
* Install project dependencies: `pip install -r requirements.txt -t lib --ignore-installed`
You may now run tests or run the application server normally.

When you are ready to exit or deactivate your Alicia virtualenv, just type the command `deactivate` on your command line.

### Starting the Server

The first time you run the server, you will need to run the following command to generate the OpenAPI config:
```aidl
python lib/endpoints/endpointscfg.py get_openapi_spec main.AliciaAPI --hostname broad-alicia-dev.appspot.com
```

Then to start the server, run:
```
dev_appserver.py ./app.yaml
```
