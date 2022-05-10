import pandas as pd

list = [{'laptop':'charger', 'milk':'cereal'},{'printer':'paper','crayon':'Paper'},{'tablet':'roku','desk':'chair'}]

df = pd.DataFrame (list, columns = ['product_name'])
print (df)