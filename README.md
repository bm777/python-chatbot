# chatbot for e-Commerce using django

This repo provide a clean implementation of chatbot using django and web stuff and using all the best practices.
This chatbot could be used for online ecommerce website(specially for iphone, samsung and redmi phone). This is just prototype. you can contribute and fork it to change as you want.

## Key Features

- [x] `TensorFlow 1.x` downloaded with pre-trained [model](https://drive.google.com/file/d/1mVWFScBHFeA7oVxQzWb8QbKfTi3TToUr/view?usp=sharing)
- [x] `Django` framework
- [x] `Jquery` used
- [x] `bootstrap` used
- [x] `CSS` used
- [x] [Pymongo](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/) for ubuntu 18.04
- [ ] GPU accelerated, but not necessary
- [x] MIT License


## Usage

### Installation

#### Pip
you should have pip installed on your machine. To do so, the guide is : [HERE](https://youtu.be/Tl3q8Wm0jvI)
```bash
#
pip install -r requirements.txt

```
You should have a virtual environment installed on your machine.
```bash
# random generation of data on mongo Batabase.
cd chatbot_app
python test.py
add 'sudo service mongod start' on .bashrc or 'service mongod start' to avoid password on bashrc file. :)
```

### migrtion of database
```bash
# python3
python manages.py makemigrations chatbot_app
python manages.py makemigrations chatbot_app
python manages.py runserver
```
