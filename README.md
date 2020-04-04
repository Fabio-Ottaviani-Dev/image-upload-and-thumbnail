# Flask image upload and thumbnail

## Overview
A basic Flask RESTful APIs implementation, design to upload and resize images.


## Setup

### Virtual Environment
Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### Venv on Ubuntu 18.04 LTS
```bash
# https://linuxize.com/post/how-to-create-python-virtual-environments-on-ubuntu-18-04/
sudo apt install python3-venv
# Within the directory
python3 -m venv env && source env/bin/activate

```

### Dependencies
```bash

# with active virtual environment
pip3 install -r requirements.txt

```

## Running the server

```bash

# flask run --help
export FLASK_APP=app &&
export FLASK_ENV=development &&
flask run --port 5001

```

## Test
To test the application you need:
1. Get [Postman](https://www.postman.com/downloads/).
2. Import the related [test file](test_postman.json).
3. Go to the Tab: Body / VALUE and select a file.
