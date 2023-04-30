import pandas

class Descriptive:
    def summary(data, scale):
        newData = data.split(",")
        
        if scale == 'ordinal' or scale == 'ratio':
            newData = [eval(value) for value in newData]

        x = pandas.Series(newData)
        return x.describe().to_json()