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
@Summary <br />
route: `/summary` <br />
description: describes the leaf (dataset) <br />
parameters: <br />
   *    data: the values to be described <br />
   *    scale: the level of measurement of the data **( nominal, ordinal, interval, ratio )** <br />
<br />

### Inferential Statistics ###
___
### T-Test ###
@One Sample T-test <br />
route: `/oneSampleTTest` <br/>
description: performs one sample t-test on a specified interval or ratio leaf <br />
parameters: <br />
   *   numericData: interval or ratio scale values to be tested on <br />
   *   popMean: population mean to be compared at <br />
   *   alternative: the inequality symbol of the alternative hypothesis (two-sided, less, greater) <br />
<br />

@Independent Samples T-test <br />
route: `/indSampleTTest` <br/>
description: performs independent samples t-test on a specified interval or ratio leaf grouped by a nominal or ordinal leaf <br />
parameters: <br />
   *   categoricalData: nominal or ordinal scale values to be tested on <br />
   *   numericData: interval or ratio scale values to be tested on <br />
   *   categories: the two groups from group values to be compared <br />
   *   equalVariance: defines if the two groups to be compared has equal variance <br />
   *   alternative: the inequality symbol of the alternative hypothesis (two-sided, less, greater) <br />
<br />

@Paired Samples T-test <br />
route: `/indSampleTTest` <br/>
description: performs independent samples t-test on a specified interval or ratio leaf grouped by a nominal or ordinal leaf <br />
parameters: <br />
   *   preNumericData: interval or ratio scale values to be tested on <br />
   *   postNumericData: interval or ratio scale values to be tested on <br />
   *   alternative: the inequality symbol of the alternative hypothesis (two-sided, less, greater) <br />
<br />




