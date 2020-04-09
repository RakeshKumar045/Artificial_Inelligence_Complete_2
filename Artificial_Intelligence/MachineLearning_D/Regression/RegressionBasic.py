# coding: utf-8

# In[5]:


import pandas as pd
from matplotlib import rcParams as rc
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

# get_ipython().run_line_magic('matplotlib', 'inline')
rc["figure.figsize"] = 10, 6

import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

# # Step : 1) Load Data

# In[49]:


# 1) Load Data
data = pd.read_csv("hp_data.csv")


# # Step : 2) Read and Analysis Data

# In[7]:


def getDataAllDetails(data):
    print("Return a tuple representing the dimensionality of the DF.  :   ", data.shape)
    print("Count of Each Data                                          :  ", data.count())
    print("Start,End,Column,Step                                       :  ", data.axes)
    print("Column                                                      :  ", data.columns)
    print("First 5 items                                               :  ", data.head(2))
    print("Missing Vlaue                                               :  ", data.isnull().sum())
    print("information                                                 :  ", data.info())
    print("Description                                                 :  ", data.describe())
    print("Size(Row*Column) represent the no of elements in this object:  ", data.size)
    print("Return unbiased skew over requested axis                    :  ", data.skew())
    print("std err of mean                                             :  ", data.sem())
    print("Return sample standard deviation over requested axis        :  ", data.std())
    print("sum of every data                                           :  ", data.sum())
    print("Copy Data to other                                          :  ", data.copy())
    print("Correlation of Data                                         :  ", data.corr())
    print("Covariance of Columns                                       :  ", data.cov())
    print("cumulative sum over data                                    :  ", data.cumsum())
    print("cumulative min or max                                       :  ", data.cummin())
    print("Remove duplicate row                                        :  ", data.drop_duplicates())
    print("Romove missing Value                                        :  ", data.dropna())
    print("Drop Specify Label                                          :  ", data.drop(labels=[2, 49, 78, 88]))
    print("Drop Specify Label(Plz check inplace true means)            :  ",
          data.drop(labels=[2, 49, 78, 88], inplace=True))
    print("Tell about Data Types                                       :  ", data.dtypes)
    print("Find the Duplicate Row                                      :  ", data.duplicated())
    print("DataFrame is Empty(True) or not(False)                      :  ", data.empty)
    print("Expanding                                                   :  ", data.expanding())
    print("Fill Na/Nan Value using Specify metho                       :  ", data.fillna)
    # print("rows/columns of DF A/c to labels in specified index   :  ",data.filter)
    # print(" check it(fill backward)          :  ",data.bfill())
    # print(" check it(fill forward)         :  ",data.ffill())
    # print("    check it ?      :  ",data.from_csv)
    # print("       check it ?   :  ",data.from_dict,data.from_items,data.from_records)
    print("Return(indication of sparse/dense and dtype) in Df          :  ", data.from_records)
    print("Tell about Data Types(check abobe ftypes)                   :  ", data.dtypes)
    print("Return counts of unique dtypes in this object               :  ", data.get_dtype_counts())
    print("Return counts of unique dtypes in this object(dense)        :  ", data.get_ftype_counts())
    print("Return ndarray after convert sparse values to dense         :  ", data.get_values())
    # print("   check it       :  ",data.groupby)
    print("RangeIndex(start=0,stop=data size, step=1)                  :  ", data.index)
    print("concise summary of DF,Dtypes,Memory,Shape,Many Info         :  ", data.info)
    # print("    check it      :  ",data.insert)
    # print("  check it        :  ",data.interpolate)
    # print("   check it       :  ",data.is_copy)
    print("Detect the Missing Value(Both Same isna & isnull )           :  ", data.isna().sum(), data.isnull().sum())
    # print("    check it      :  ",data.join)
    print("Get the 'info axis(same as columns : data.columns)           :  ", data.keys, data.columns)
    print("unbiased kurt over requested axis using Fisher's def         :  ", data.kurt, data.kurtosis)
    print("both are same data.kurt & data.kurtosis                      :  ", data.kurt, data.kurtosis)
    print("Return index for last non-NA/null value                      :  ", data.last_valid_index())
    print("mean absolute deviation value for the requested axis         :  ", data.mad())
    print("Returns the maximum of the values in the object              :  ", data.max())
    print("Returns the minimum of the values in the object              :  ", data.min())
    print("Return the mean of the values for the requested axis         :  ", data.mean())
    print("Return the median of the values for the request axis         :  ", data.median())
    # print("   check it       :  ",data.melt())
    print("Return the memory usage of each column in bytes.             :  ", data.memory_usage())
    # print("  check it        :  ",data.merge)
    # print("    check it (mod, mul,multiply)      :  ",data,mod,data.mul,data.multiply)
    print("Return an int representing the no of axes/array dims         :  ", data.ndim)
    print("row's DF sorted by the n smallest values of `columns         :  ", data.nsmallest(n=10, columns="price"))
    print("row's DF sorted by the n largest values of `columns          :  ", data.nlargest(n=10, columns="price"))
    print("Find existing(non-missing) values(Same:notna,notnull)        :  ", data.notna(), data.notnull())
    print("Series with no of distinct observations over requested axis  :  ", data.nunique(axis=0))
    # print("     check it     :  ",data.pct_change)
    # print(" check it(pivot,pivot_table)         :  ",data.pivot,data.pivot_table)
    print("Return item & drop/delete from frame.Raise Error,if not found:  ", data.pop("price"))
    # print("  check it        :  ",data.pow)
    print("product/prod same of the value for the request(default axis=0):  ", data.prod(axis=0), data.product(axis=0))
    print("values quantile over requested axis, a la numpy.percentile.   :  ", data.quantile())
    # print("    check it      :  ",data.query)
    # print("       check it   :  ",data.radd)
    print("Compute numerical data rank(1 through n)along axis.Equal values:  ", data.rank(numeric_only=True, axis=0))
    print("Conform DF to new index with optional filling logic,placing    :  ", data.reindex().sum())
    # print("check it  :  ",data.rename,data.rename_axis,data.reorder_levels,data.replace,data.resample,data.resample)
    # print("   check it :  ",data.reset_index(),data.rmod,data.rmul,data.rolling,data.rpow,data.rsub,data.rtruediv)
    print("Round a DataFrame to a variable number of decimal places.      :  ", data.round())
    print("Return a random sample of items from an axis of object.        :  ", data.sample())
    print("check it      :  ", data.select, data.set_index, data.set_value)
    print("Return unbiased standard error of the mean over requested axis.:  ", data.sem())
    print("Shift index by desired no of periods with an optional time freq:  ", data.shift(axis=0, periods=3))
    print("Equivalent to `shift` without copying data                     :  ", data.slice_shift(axis=0, periods=5))
    print("Sort object by labels (along an axis=0, default)               :  ",
          data.sort_index(axis=1, ascending=False))
    print("Sort by the values along either axis                           :  ",
          data.sort_values(by=["price", "yearsOld"], axis=0, ascending=False))
    print("Sort multilevel index by chosen axis level(sort based on words):  ",
          data.sortlevel(level=0, axis=1, ascending=True))
    # print("Check it  :  ",data.stack(),data.sub,data.subtract())
    print("Display All Items(same as head(total no of items))             :  ", data.style)
    print("Interchange axes & swap values axes(swap rows to columns)      :  ",
          data.swapaxes(axis1=0, axis2=1, copy=False))
    print("Interchange axes & swap values axes appropriately              :  ", data.swaplevel(i=0, j=0, axis=0))
    # print(" check it    :  ",data.unstack,data.update())
    print("Return unbiased variance over requested axis.                  :  ", data.var(axis=0))
    # print("   check it       :  ",data.where,data.xs())


# # Rename Column Name

# In[8]:


# dic = { "KEY" : "VALUE"}
def renameColumn(dic, data):
    # DICTIONARY : KEY AND VALUE , KEY IS OLD COLUMN NAME , VALUE IS NEW COLUMN NAME
    data = data.rename(columns=dic)
    return data


# # Step : 3) Visualization the Data
# There are 2 types of library to visualization.
# ##1) Matplot 2) Seaborn(use attractive and looking good and more features)
# #Draw the Graph (Histogram, Straight Line, Pie, Bar, Scatter, ETC)

# In[9]:


def graphDetail():
    print("Prints the values to a stream, or to sys.stdout by default boxplot      :  ", data.boxplot())
    print("Prints the values to a stream, or to sys.stdout by default hist         :  ", data.hist())
    print("Prints the values to a stream, or to sys.stdout by default plot         :  ", data.plot())
    # print("Prints the values to a stream, or to sys.stdout by default              :  ",data.boxplot())
    # print("Prints the values to a stream, or to sys.stdout by default              :  ",data.boxplot())


# # Step : 4) Data Preprocessing
# used to convert the raw data into a clean data set

# # A) Data Cleaning

# In[10]:


# getDataAllDetails(data=data)


# In[11]:


# data.head(3) # before label encoding


# # B) Label Encoding : Convert Categorical Value to Integer Value

# In[12]:


# 1st Method
# char_cols = data.dtypes.pipe(lambda x: x[x == 'object']).index
# for c in char_cols:
#     data[c] = pd.factorize(data[c])[0]

# OR 2nd method
# enc = LabelEncoder()
# data["place"] = enc.fit_transform(data["place"])
# data["sale"] = enc.fit_transform(data["sale"])
# data["built"] = enc.fit_transform(data["built"])

# Do not try to change integer value
# data["price"] = enc.fit_transform(data["price"])


# # Label Encoding  and Inverse: Convert Categorical Value to Integer Value and Vice-versa

# In[13]:


from sklearn.preprocessing import LabelEncoder


def labelEncodingCategoryToIntergerViceVersa(dataset):
    '''
    @author Rakesh
    @see The function label encodes the object type columns and gives label      encoded and inverse tranform of the label encoded data
    @param dataset dataframe on whoes column the label encoding has to be done
    @return label encoded and inverse tranform of the label encoded data.
   '''
    data_original = dataset[:]
    data_tranformed = dataset[:]
    for y in dataset.columns:
        # check the dtype of the column object type contains strings or chars
        if (dataset[y].dtype == object):
            print("The string type features are  : " + y)
            le = LabelEncoder()
            le.fit(dataset[y].unique())
            # label encoded data
            data_tranformed[y] = le.transform(dataset[y])
            # inverse label transform  data
            data_original[y] = le.inverse_transform(data_tranformed[y])
    return data_tranformed, data_original


# # Rename Column name

# In[35]:


# dic = { "place" : "Places", "built" : "builts"}
dic = {"Unnamed: 0": "ID"}
data = renameColumn(dic, data)

# In[36]:


data_tranformed, data_original = labelEncodingCategoryToIntergerViceVersa(data)

# In[37]:


data_tranformed.head(3)  # after label encoding

# In[38]:


data_original.head(3)  # original data

# # 5) Feature Engineering

# In[1]:


# feature engineering
x = data_tranformed.loc[:, ["ID", "place", "built", "sqft", "sale", "yearsOld", "floor", "totalFloor", "bhk"]]
y = data_tranformed.price

# # 6) Split Dataset (x_train, x_test , y_train , y_test)

# In[57]:


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=10)

# In[58]:


names = ["Linear Regression", "Decision Tree Regression", "Random Forest Regression"]

algorithms = [LinearRegression(), DecisionTreeRegressor(), RandomForestRegressor()]

columns_name = ["Model_name", "Random_state", 'r2_score']

# In[59]:


rows = []


def addRandomStateForAlgorithm(x, y, names, algorithms, columns_name, random_state_list):
    for j in range(len(algorithms)):
        model = algorithms[j]
        for i in random_state_list:
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=i)
            model.fit(x_train, y_train)
            pred_test = model.predict(x_test)
            row = [names[j], i, r2_score(y_test, pred_test)]
            rows.append(row)
    models_df = pd.DataFrame(rows)
    models_df.columns = columns_name
    print(models_df)


# In[60]:


random_state_list_up_to_10 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random_state_list_10_up_to_20 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# In[61]:


addRandomStateForAlgorithm(x, y, names, algorithms, columns_name, random_state_list_up_to_10)

# In[43]:


# data[2:]
# data[:3]
# data.iloc[:,2:]
