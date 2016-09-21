RbGomoku
===

This Project is the result of study during graduation.  


## Requirements
- make
- Python 3.4+

## Install

In root project run:

```bash
$ make install
```

To view make instructions run:
```bash
$ make help
```

Should be returns the follow result:
 
```bash
clean - remove all build and Python artifacts
install - install the package to the active Python's site-packages
help - print help
run - run rbgomoku game
test - run tests quickly with the default Python
```

## To develop

### Requirements
- make
- Python 3.4+
- virtualenv or pyvenv

### Create environment
```bash
# 1. create virtualenv
$ pyvenv env # or use `virtualenv env`

# 2. run follow command to active python virtual environment created above 
$ source env/bin/activate

# 3. Them install dependencies 
$ pip install -r requirements.txt


# To Playing run: 
$ python main
```