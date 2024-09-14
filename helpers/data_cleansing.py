def data_cleanup(data):

    return data

def age_cleanup(column,mean_age):
    
    if column.isnull():
        new_column = mean_age
    return int(new_column)