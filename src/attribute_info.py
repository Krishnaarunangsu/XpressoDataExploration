import pandas as pd
import numpy as np
from enum import Enum


class DataType(Enum):
    """
    Enum class to standardize all the datatype
    """
    ORDINAL = "ordinal"
    NOMILAL = "nominal"
    NUMERIC = "numeric"
    STRING = "string"
    TEXT = "text"
    DATE = "date"
    FLOAT = "float"
    INT = "int"
    OBJECT = "object"
    BOOL = "bool"
    PD_DATETIME = "datetime"

    def __str__(self):
        """
        String Representation
        :return:
        """
        return self.value


class AttributeInfo:
    """
    Handles Information About Attribute
    """
    DECIMAL_PRECISION = 2

    def __init__(self, attribute_name):
        """
        Initialization
        :param attribute_name:
        """
        self.name = attribute_name
        self.metrics = dict()

    @staticmethod
    def na_analysis(data):
        """
        performs na_analysis
        :param data:
        :return: na_count, na_count_percentage, missing_count, missing_count_percentage

        """

        num_rows = float(data.size)
        na_count = float(data.isna().sum())
        na_count_percentage = round((na_count/num_rows)*100, AttributeInfo.DECIMAL_PRECISION)
        missing_count = float((data == "").sum())
        missing_count_percentage = round((missing_count/num_rows)*100,AttributeInfo.DECIMAL_PRECISION)

        return na_count, na_count_percentage, missing_count, missing_count_percentage

    @staticmethod
    def numeric_analysis(data, outlier_margin=10, probability_dist_bins=100):
        """

        :param data:
        :param outlier_margin:
        :param probability_dist_bins:
        :return:
        """

        summary = data.describe().round(AttributeInfo.DECIMAL_PRECISION)

        min = summary["min"]
        max = summary["max"]
        mean = summary["mean"]
        std = summary["std"]
        quartiles = [summary["25%"], summary["50%"], summary["75%"]]

        try:
            quartiles = pd.qcut(data, 4, retbins=True)[1].round(
                AttributeInfo.DECIMAL_PRECISION)
        except ValueError as e:
            print("Dropping duplicated for calculating deciles for {"
                  "}".format(data.name))
            quartiles = pd.qcut(data, 4, duplicates='drop', retbins=True)[
                1].round(AttributeInfo.DECIMAL_PRECISION)

        try:
            deciles = pd.qcut(data, 10, retbins=True)[1].round(
                AttributeInfo.DECIMAL_PRECISION)
        except ValueError as e:
            print("Dropping duplicated for calculating deciles for {"
                  "}".format(data.name))
            deciles = pd.qcut(data, 10, duplicates='drop', retbins=True)[
                1].round(AttributeInfo.DECIMAL_PRECISION)
        outliers = round(data[(np.abs(data - mean) > (
                outlier_margin * std))], AttributeInfo.DECIMAL_PRECISION).to_numpy()

        pdf = pd.cut(data, probability_dist_bins).value_counts()
        pdf.index = pdf.index.astype(str)
        pdf = pdf.to_dict()
        kurtosis = round(data.kurtosis(), AttributeInfo.DECIMAL_PRECISION)
        return min, max, mean, std, quartiles, deciles, outliers, pdf, \
               kurtosis

    @staticmethod
    def categorical_analysis(data, threshold=2):
        '''
        :param data: Input pandas categorical series data
        :param threshold: Count percentage value for defining Outlier Categories
        :return:
        '''
        num_rows = float(data.size)
        print(f'Categorical Data Set-Number of Rows:{num_rows}')
        freq_count = data.value_counts().to_dict()
        print(f'Categorical Data Set-Frequency count:{freq_count}')
        outliers = list()
        print(f'Outliers of Categorical DataSet during start:{np.array(outliers)}')
        print(freq_count.keys())
        for label in freq_count.keys():
            print(f'Label:{label}')
            if (freq_count[label] / num_rows) * 100 < threshold:
                outliers.append(label)
        print(f'Outliers of Categorical DataSet during Finish:{np.array(outliers)}')
        return np.array(outliers), freq_count

    @staticmethod
    def date_analysis(data):
        return data.min(), data.max()

    def populate(self, data):
        """
        populate statistical values
        :param data:
        :return:
        """
        print('Coming in Populate')
        na_count, na_count_percentage, missing_count, missing_count_percentage = self.na_analysis(data)

        print(f'NA Count:{na_count}')
        print(f'NA Count Percentage :{na_count_percentage}')
        print(f'Missing Count:{missing_count}')
        print(f'Missing Count Percentage:{missing_count_percentage}')

        self.metrics["na_count"] = na_count
        self.metrics["na_count_percentage"] = na_count_percentage
        self.metrics["missing_count"] = missing_count
        self.metrics["missing_count_percentage"] = missing_count_percentage

        if str(self.type) is "numeric":
            min, max, mean, std, quartiles, deciles,outliers, pdf, kurtosis = self.numeric_analysis(data)
            print(f'Min:{min}')
            print(f'Mean:{mean}')
            print(f'Standard Deviation:{std}')
            print(f'Quatiles:{quartiles}')
            print(f'Outliers:{outliers}')
            print(f'PDF:{pdf}')
            print(f'Deciles:{deciles}')
            print(f'Max:{max}')
            print(f'Kurtosis:{kurtosis}')

            self.metrics["min"] = min
            self.metrics["max"] = max
            self.metrics["mean"] = mean
            self.metrics["std"] = std
            self.metrics["quartiles"] = quartiles
            self.metrics["deciles"] = deciles
            self.metrics["outliers"] = outliers
            self.metrics["pdf"] = pdf
            self.metrics["kurtosis"] = kurtosis

        elif str(self.type) is "ordinal" or self.type is "nominal":
            print('Coming in Ordinal/Nominal Block')
            outliers,freq_count = self.categorical_analysis(data)
            self.metrics["outliers"] = outliers
            self.metrics["freq_count"] = freq_count

        elif str(self.type) is "string":
            print('Coming in String Block')
            self.metrics["tobedone"] = "Exploration of string type data"
            print(f'Structured Data-String Type Metrics:{self.metrics}')

        elif str(self.type) is "text":
            print('Coming in Text Block')
            self.metrics["tobedone"] = "Exploration of text type data"

        elif str(self.type) is "date":
            print('Coming in Date Block')
            min_date,max_date = self.date_analysis(data)
            self.metrics["min"] = min_date
            self.metrics["max"] = max_date
