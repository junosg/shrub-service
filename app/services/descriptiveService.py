import pandas

class Descriptive:
    def summary(values, scale):
        valuesList = values.split(",")

        if scale == 'ordinal' or scale == 'ratio':
            valuesList = [eval(value) for value in valuesList]

        x = pandas.Series(valuesList)
        return x.describe().to_json()