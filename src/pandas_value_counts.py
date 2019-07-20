import pandas as pd
import numpy as np

#data_series = pd.read_csv('Train.csv')
#print(f'Data:{data_series}')
#freq_count = data_series.value_counts().to_dict()


def categorical_analysis(data, threshold=2):
        '''
        :param data: Input pandas categorical series data
        :param threshold: Count percentage value for defining Outlier Categories
        :return:
        '''
        num_rows = float(data.size)
        print('Categorical Data Set-Number of Rows:{num_rows}')
        freq_count = data.value_counts().to_dict()
        print('Categorical Data Set-Frequency count:{freq_count}')
        outliers = list()
        print(f'Outliers of Categorical DataSet during start:{np.array(outliers)}')
        for label in freq_count.keys():
            print(f'Label:{label}')
            if (freq_count[label] / num_rows) * 100 < threshold:
                outliers.append(label)
        print(f'Outliers of Categorical DataSet during Finish:{np.array(outliers)}')
        return np.array(outliers), freq_count


if __name__ == "__main__":
    #data_series = pd.read_csv('Train.csv')
    #print((f'Data Type of the csv contents:{type(data_series)}'))
    #print(f'Data:{data_series}')
    #categorical_analysis(data_series, 2)
    import pandas as pd

    df = pd.read_csv("weather_1.csv")
    ok=[]
    #for name,group in df.groupby(["Age"]):
        #ok.append(group["Age"].value_counts(sort=True))



    '''for name, group in df.groupby(["Gender"]):
        ok.append(group["Gender"].value_counts(sort=True))
    print(ok)'''

    count = df.loc[:, 'temp'].value_counts()
    tuples = [tuple((x, y)) for x, y in count.items()]
    print(tuples)
    print(len(tuples))

