import pandas
import scipy.stats as stats
from flask import jsonify
import logging

class TTest:
    def listValues(values):
        list = values.split(",")
        list = [eval(value) for value in list]
        
        return list

    def oneSample(numericData, popMean, alternative):
        valuesList = TTest.listValues(numericData)

        tStatistic, pValue = stats.ttest_1samp(a=valuesList, popmean=float(popMean), alternative=alternative)
        return jsonify(tStatistic = tStatistic, pValue = pValue) 
    
    def independent(categoricalData, numericData, categories, equalVariance, alternative):
        groupsList = categoricalData.split(',')
        groups = categories.split(',')

        valuesList = TTest.listValues(numericData)

        data = pandas.DataFrame({'group':groupsList, 'value':valuesList}) 

        group1 = data[data['group']==groups[0]]
        group2 = data[data['group']==groups[1]] 

        tStatistic, pValue = stats.ttest_ind(group1['value'], group2['value'], equal_var=equalVariance.lower()=='true', alternative=alternative)

        return jsonify(tStatistic = tStatistic, pValue = pValue, leftHand=groups[0], rightHand=groups[1])

    def paired(preNumericData, postNumericData, alternative):
        preNumericData = TTest.listValues(preNumericData)
        postNumericData = TTest.listValues(postNumericData)

        tStatistic, pValue = stats.ttest_rel(preNumericData, postNumericData, alternative=alternative)

        return jsonify(tStatistic = tStatistic, pValue = pValue)
