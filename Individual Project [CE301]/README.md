# Selfish Mining Simulator

![CieranBlockchainlogo1_optimized](/uploads/8fa2a9c3c990468b09ccba9f89c5049d/CieranBlockchainlogo1_optimized.jpg)

An end-to-end simulator programmed in Python to demonstrate theoretical concepts discussed in the paper 'Majority is not enough: Bitcoin mining is vulnerable' by Ittay Eyal and Emin Gün Sirer


This simulator aims to demonstrate a well documented 'strategy' within the Cryptocurrency community named 'selfish mining'. By the end of this reading, you will develop an understanding of what exactly 'selfish mining' is, and how the Selfish Mining Simulator is used to demonstrate the model behind this concept, and more importantly, strategies derived from this original model as developed by myself.


# Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

# Prerequisits

1. Download an IDE suited to the project - in this instance I would recommend [Pycharm](https://www.jetbrains.com/pycharm/). This will allow you to run the project.
2. [Python version 3.7](https://www.python.org/downloads/) will be required, as without an interpreter you are unable to create a runnable Pycharm project.


### Installation

Let’s start our project: if you’re on the Welcome screen, click Create New Project. If you’ve already got a project open, choose File | New Project.

PyCharm suggests several project templates for the creation of the various types of applications (Django, Google AppEngine,, and so on). When PyCharm creates a new project from a project template, it produces the corresponding directory structure and specific files, and any needed run configurations or settings.

In this tutorial we’ll create a simple Python script, so we’ll choose Pure Python. This template will create an empty project for us.

Choose the project location. To do that, click the Browse button button next to the Location field, and specify the directory for your project.

Python best practice is to create a virtualenv for each project. To do that, expand the Project Interpreter: New Virtualenv Environment node and select a tool used to create a new virtual environment. Let's choose Virtualenv tool, and specify the location and base interpreter used for the new virtual environment. Select the two check boxes below if necessary.

- Create a new project
Then click the Create button at the bottom of the New Project dialog.

If you’ve already got a project open, after clicking Create PyCharm will ask you whether to open a new project in the current window or in a new one. Choose Open in current window - this will close the current project, but you'll be able to reopen it later. See the page Opening Multiple Projects for details.

- Creating a Python file
Select the project root in the Project tool window, then select File | New ... from the main menu or press Alt+Insert.

- Create a Python file
Choose the option Python file from the popup, and then type the new filename.

- Creating a new Python file
PyCharm creates a new Python file and opens it for editing.

Once you have created a Python file ready for editing - paste the source code from the following directory into your new project: 

ce301_almond_c > attacks_on_blockchain : selfish_mine_simulator

# Running tests (optional developer option)
This is only to demonstrate code coverage - it's not necessary for running the simulator

- To run tests in a project, use the nose2 script that is installed with nose2:
- The recommended way to install nose2 is with pip
- Pip is a tool for installing and managing Python packages, such as those used in the [Python Package Index](https://pypi.org/).

First, install pip.

Install a package from [PyPI](https://pypi.org/):
    
Then enter into command line
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```
Then run the following:
```
python get-pip.py
```
Now, to run tests in a project, use the nose2 script that is installed with nose2:
```
nose2
```

This module allowed me to see my test code coverage at a more meaningful measure (as d%) when performing unit testing on the functions within my selfish mining simulator. 

## Author


Cieran Almond
 
 
## References 

- https://cseegit.essex.ac.uk/snippets/8
- https://github.com/erasmus-without-paper/ewp-specs-architecture/tree/v1.10.0
- https://github.com/erasmus-without-paper/ewp-specs-sec-intro/tree/v2.0.2
- https://guides.github.com/features/mastering-markdown/


License
----

University of Essex

