# Shrub
A free, student-friendly, statistical tool.

## Prerequisites ##
1. Python
2. Flask

## Setup ##
1.  Go to project directory and install virtualenv <br />
    `py -m pip install virtualenv .` <br />
2.  Create virtual environment <br />
    `py -m virtualenv venv` <br />
3.  Active virtual environment <br />
    `venv\scripts\activate` <br />
4.  Install dependencies <br />
    `pip install flask` <br />
    `pip install pandas` <br />
    `pip install scipy` <br />

## Routes ##
### Descriptive Statistics ###
<br />
@Summary <br />

route: `/summary` <br />
description: displays the summary of a leaf (dataset) <br />
parameters: <br />
   *    values: the values to be described
   *    scale: the level of measurement of the data **( nominal, ordinal, interval, ratio )**

<br />

### Inferential Statistics ###






