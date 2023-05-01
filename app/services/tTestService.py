import pandas
import scipy.stats as stats
from flask import jsonify
import logging

class TTest:
    def listValues(values):
        list = values.split(",")
        list = [eval(value) for value in list]
        
        return list

    def oneSample(dataValues, popMean, alternative):
        valuesList = TTest.listValues(dataValues)

        tStatistic, pValue = stats.ttest_1samp(a=valuesList, popmean=float(popMean), alternative=alternative)
        return jsonify(tStatistic = tStatistic, pValue = pValue) 
    
    def independent(groupValues, dataValues, groups, equalVariance, alternative):
        groupsList = groupValues.split(',')
        groups = groups.split(',')

        valuesList = TTest.listValues(dataValues)

        data = pandas.DataFrame({'group':groupsList, 'value':valuesList}) 

        group1 = data[data['group']==groups[0]]
        group2 = data[data['group']==groups[1]] 

        tStatistic, pValue = stats.ttest_ind(group1['value'], group2['value'], equal_var=equalVariance.lower()=='true', alternative=alternative)

        return jsonify(tStatistic = tStatistic, pValue = pValue, leftHand=groups[0], rightHand=groups[1])

    def paired(preDataValues, postDataValues, alternative):
        preDataValues = TTest.listValues(preDataValues)
        postDataValues = TTest.listValues(postDataValues)

        tStatistic, pValue = stats.ttest_rel(preDataValues, postDataValues, alternative=alternative)

        return jsonify(tStatistic = tStatistic, pValue = pValue)

        
        