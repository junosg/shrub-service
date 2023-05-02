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
___
**@Summary** <br />
*Describes the leaf (dataset)* <br />
<font size="1.5">
route: `/summary` <br />
parameters: <br />
Name | Description
--- | ---
data | the data to be described <br />
scale | the level of measurement of the data **( nominal, ordinal, interval, ratio )** <br />

<br />
</font>

### Inferential Statistics ###
___
### T-Test ###
**@One Sample T-test** <br />
*Performs one sample t-test on a specified interval or ratio leaf* <br />
<font size="1.5">
route: `/oneSampleTTest` <br/> 
parameters: <br />
Name | Description
--- | ---
numericData| interval or ratio scale values to be tested on <br />
popMean| population mean to be compared at <br />
alternative| the inequality symbol of the alternative hypothesis (two-sided, less, greater) <br />

<br />
</font>

**@Independent Samples T-test** <br />
*Performs independent samples t-test on a specified interval or ratio leaf grouped by a nominal or ordinal leaf* <br />
<font size="1.5">
route: `/indSamplesTTest` <br/>
parameters: <br />
Name | Description
--- | ---
categoricalData | nominal or ordinal scale values to be tested on <br />
numericData | interval or ratio scale values to be tested on <br />
categories | the two groups from group values to be compared <br />
equalVariance | defines if the two groups to be compared has equal variance <br />
alternative | the inequality symbol of the alternative hypothesis (two-sided, less, greater) <br />

<br />
</font>

**@Paired Samples T-test** <br />
*Performs independent samples t-test on a specified interval or ratio leaf grouped by a nominal or ordinal leaf* <br />
<font size="1.5">
route: `/pairedSamplesTTest` <br/>
parameters: <br />
Name | Description
--- | ---
preNumericData | interval or ratio scale values to be tested on <br />
postNumericData | interval or ratio scale values to be tested on <br />
alternative | the inequality symbol of the alternative hypothesis (two-sided, less, greater) <br />

<br />
</font>





