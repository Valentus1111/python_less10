import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

one_hot_data = pd.concat([pd.get_dummies(data['whoAmI'], prefix='whoAmI')], axis=1)

one_hot_data.head()
