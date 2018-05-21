###############################################
# STEP: 1
# Verify pip3:
# pip3.6 list
# pip and setuptools shoudl be installed

###############################################
# STEP: 2
# sudo pip3.6 install virtualenv
#

###############################################
# STEP: 3   Make sure you use correcrt virtualenv
# whereis virtualenv



###############################################
# STEP: 4   Create a fake python installation
# 4.1 Create directory in HOME to store all your virtual environments
#    mkdir ~/.venvs
# 4.2 Buld virtual environment in ~/.venvs/lpthw , with including system-site-packages
#    virtualenv --system-site-packages ~/.venvs/lpthw
# 4.3 source virtual environment
#   . ~/.venvs/lpthw/bin/activate
# 4.4 Your prompt changed to (lpthw), and you know that you are using that virtual environment

###############################################
# STEP: 5   Install nose, a testing framework
# pip install nose


###############################################
# STEP: 6   Creating the Skeleton Project Directory
# 6.1:  mkdir skeleton
# 6.2:  cd skel eton
# 6.3:  mkdir bin ex47 tests docs
# 6.4: Setup some initial files:
#       touch ex47/__init__.py
#       touch tests/__init__.py
# 6.5: Then we need to create a setup.py file we can use to install our project later if we want:
#       touch setup.py
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'My Name',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
#
# 6.6: Finally, you will want a simple skeleton file for tests named tests/ex47_tests.py:
#   touch tests/ex47_tests.py
# 6.7: Run "nosetests" command from tests/.. directory  !!!

###############################################
# STEP 7:   Using the Skeleton
# Whenever you want to start a new project, just do this:
#   1. Make a copy of your skeleton directory. Name it after your new project.
#   2. Rename (move) the ex47 directory to be the name of your project or whatever you want to call your root module.
#   3. Edit your setup.py to have all the information for your project.
#   4. Rename tests/ex47_tests.py to also have your module name.
#   5. Double check it’s all working by using nosetests again.
#   6. Start coding.


###############################################
# TEST GUIDLINE
#
# 1.    Write one test file for each module you make
# 2.    Keep your test cases (functions) short, but do not worry if they are a bit messy. Test cases are usually kind of messy.
# 3.    Even though test cases are messy, try to keep them clean and remove any repetitive code you can.
# 4.    Finally, do not get too attached to your tests. Sometimes, the best way to redesign something is to just delete it and start over.


###############################################


