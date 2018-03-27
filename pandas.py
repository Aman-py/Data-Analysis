Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> s = pd.Series()
>>> pr
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    pr
NameError: name 'pr' is not defined
>>> print(s)
Series([], dtype: float64)
>>> import numpy as np
>>> arr = np.array([1,2,3,4,5,6,7,8,9,0])
>>> s = pd.Series(arr)
>>> print(s)
0    1
1    2
2    3
3    4
4    5
5    6
6    7
7    8
8    9
9    0
dtype: int64
>>> s = pd.Series(arr,dtype=str,index=['a','b','c','d','e','f','g','h','i','j','k'])
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    s = pd.Series(arr,dtype=str,index=['a','b','c','d','e','f','g','h','i','j','k'])
  File "/usr/local/lib/python3.5/dist-packages/pandas/core/series.py", line 266, in __init__
    data = SingleBlockManager(data, index, fastpath=True)
  File "/usr/local/lib/python3.5/dist-packages/pandas/core/internals.py", line 4402, in __init__
    fastpath=True)
  File "/usr/local/lib/python3.5/dist-packages/pandas/core/internals.py", line 2957, in make_block
    return klass(values, ndim=ndim, fastpath=fastpath, placement=placement)
  File "/usr/local/lib/python3.5/dist-packages/pandas/core/internals.py", line 2082, in __init__
    placement=placement, **kwargs)
  File "/usr/local/lib/python3.5/dist-packages/pandas/core/internals.py", line 120, in __init__
    len(self.mgr_locs)))
ValueError: Wrong number of items passed 10, placement implies 11
>>> s= pd.Series(s,index=[100,101,102,103])
>>> s
100   NaN
101   NaN
102   NaN
103   NaN
dtype: float64
>>> s= pd.Series(arr,index=[100,101,102,103,1,2,3,4,5,5])
>>> s
100    1
101    2
102    3
103    4
1      5
2      6
3      7
4      8
5      9
5      0
dtype: int64
>>> s= pd.Series(arr,index=[100,101,102,103,1,2,3,4,5,5],dtype=str)
>>> s
100    1
101    2
102    3
103    4
1      5
2      6
3      7
4      8
5      9
5      0
dtype: object
>>> data = {'a' : 0., 'b' : 1., 'c' : 2.}
>>> s = pd.Series(data)
>>> s
a    0.0
b    1.0
c    2.0
dtype: float64
>>> s['a']
0.0
>>> s = pd.Series(data,index=[1,2,3,4])
>>> s
1   NaN
2   NaN
3   NaN
4   NaN
dtype: float64
>>> s = pd.Series(data,index=['a','b','c','d'])
>>> s
a    0.0
b    1.0
c    2.0
d    NaN
dtype: float64
>>> s = pd.Series(5, index=[0, 1, 2, 3])
>>> s
0    5
1    5
2    5
3    5
dtype: int64
>>> s[0]
5
>>> print(s[:3])
0    5
1    5
2    5
dtype: int64
>>> data[['a','b','c']]
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    data[['a','b','c']]
TypeError: unhashable type: 'list'
>>> df = pd.DataFrame()
>>> df
Empty DataFrame
Columns: []
Index: []
>>> data = [['Alex',10],['Bob',12],['Clarke',13]];df = pd.DataFrame(data,columns=['Name','Age']);print(df)
     Name  Age
0    Alex   10
1     Bob   12
2  Clarke   13
>>> data = [{1:2,2:3},{1:1,2:2,3:3}]
>>> df = pd.DataFrame(data)
>>> df
   1  2    3
0  2  3  NaN
1  1  2  3.0
>>> df=pd.DataFrame(data,index=['First','Second'],columns=[1,2])
>>> df
        1  2
First   2  3
Second  1  2
>>> #Create a DataFrame from Dict of Series
>>> daw={'Name':pd.Series([1,2,3,4,5],index=['a','b','c','d','e']),'Marks':pd.Series([90,91,92,93,100])}
>>> daw
{'Name': a    1
b    2
c    3
d    4
e    5
dtype: int64, 'Marks': 0     90
1     91
2     92
3     93
4    100
dtype: int64}
>>> da = pd.DataFrame(daw)
>>> da
   Marks  Name
0   90.0   NaN
1   91.0   NaN
2   92.0   NaN
3   93.0   NaN
4  100.0   NaN
a    NaN   1.0
b    NaN   2.0
c    NaN   3.0
d    NaN   4.0
e    NaN   5.0
>>> daw={'Name':pd.Series([1,2,3,4,5],index=['a','b','c','d','e']),'Marks':pd.Series([90,91,92,93,100],index=['a','b','c','d','e'])}
>>> daw
{'Name': a    1
b    2
c    3
d    4
e    5
dtype: int64, 'Marks': a     90
b     91
c     92
d     93
e    100
dtype: int64}
>>> ad = pd.DataFrame(daw)
>>> ad
   Marks  Name
a     90     1
b     91     2
c     92     3
d     93     4
e    100     5
>>> ad['Name']
a    1
b    2
c    3
d    4
e    5
Name: Name, dtype: int64
>>> ad['Class'] = pd.Series([10,11,12,9,8])
>>> ad
   Marks  Name  Class
a     90     1    NaN
b     91     2    NaN
c     92     3    NaN
d     93     4    NaN
e    100     5    NaN
>>> ad['Class']
a   NaN
b   NaN
c   NaN
d   NaN
e   NaN
Name: Class, dtype: float64
>>> ad['Class'] = pd.Series([10,11,12,9,8],index=['a','b','c','d','e'])
>>> ad
   Marks  Name  Class
a     90     1     10
b     91     2     11
c     92     3     12
d     93     4      9
e    100     5      8
>>> ad['Section']=ad['Class']+ad['Name']
>>> ad
   Marks  Name  Class  Section
a     90     1     10       11
b     91     2     11       13
c     92     3     12       15
d     93     4      9       13
e    100     5      8       13
>>> ad['Sex'] = ["Male"]
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    ad['Sex'] = ["Male"]
  File "/usr/local/lib/python3.5/dist-packages/pandas/core/frame.py", line 2519, in __setitem__
    self._set_item(key, value)
  File "/usr/local/lib/python3.5/dist-packages/pandas/core/frame.py", line 2585, in _set_item
    value = self._sanitize_column(key, value)
  File "/usr/local/lib/python3.5/dist-packages/pandas/core/frame.py", line 2760, in _sanitize_column
    value = _sanitize_index(value, self.index, copy=False)
  File "/usr/local/lib/python3.5/dist-packages/pandas/core/series.py", line 3121, in _sanitize_index
    raise ValueError('Length of values does not match length of ' 'index')
ValueError: Length of values does not match length of index
>>> ad.pop("Name")
a    1
b    2
c    3
d    4
e    5
Name: Name, dtype: int64
>>> ad
   Marks  Class  Section
a     90     10       11
b     91     11       13
c     92     12       15
d     93      9       13
e    100      8       13
>>> del ad['Marks']
>>> ad
   Class  Section
a     10       11
b     11       13
c     12       15
d      9       13
e      8       13
>>> ad['Fax'] = list(range(0,5))
>>> ad
   Class  Section  Fax
a     10       11    0
b     11       13    1
c     12       15    2
d      9       13    3
e      8       13    4
>>> #Row Selection, Addition, and Deletion
>>> d = {'one':pd.Series(list(range(1000,1010,2)),index=list(range(1,6))),'two':pd.Series(list(range(2000,2020,4)),index=list(range(1,5)))}
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    d = {'one':pd.Series(list(range(1000,1010,2)),index=list(range(1,6))),'two':pd.Series(list(range(2000,2020,4)),index=list(range(1,5)))}
  File "/usr/local/lib/python3.5/dist-packages/pandas/core/series.py", line 266, in __init__
    data = SingleBlockManager(data, index, fastpath=True)
  File "/usr/local/lib/python3.5/dist-packages/pandas/core/internals.py", line 4402, in __init__
    fastpath=True)
  File "/usr/local/lib/python3.5/dist-packages/pandas/core/internals.py", line 2957, in make_block
    return klass(values, ndim=ndim, fastpath=fastpath, placement=placement)
  File "/usr/local/lib/python3.5/dist-packages/pandas/core/internals.py", line 120, in __init__
    len(self.mgr_locs)))
ValueError: Wrong number of items passed 5, placement implies 4
>>> d = {'one':pd.Series(list(range(1000,1010,2)),index=list(range(1,6))),'two':pd.Series(list(range(2000,2020,4)),index=list(range(1,6)))}
>>> d
{'two': 1    2000
2    2004
3    2008
4    2012
5    2016
dtype: int64, 'one': 1    1000
2    1002
3    1004
4    1006
5    1008
dtype: int64}
>>> df = pd.DataFrame(d)
>>> df
    one   two
1  1000  2000
2  1002  2004
3  1004  2008
4  1006  2012
5  1008  2016
>>> print(df.loc['3'])
Traceback (most recent call last):
  File "/usr/local/lib/python3.5/dist-packages/pandas/core/indexing.py", line 1506, in _has_valid_type
    error()
  File "/usr/local/lib/python3.5/dist-packages/pandas/core/indexing.py", line 1501, in error
    axis=self.obj._get_axis_name(axis)))
KeyError: 'the label [3] is not in the [index]'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    print(df.loc['3'])
  File "/usr/local/lib/python3.5/dist-packages/pandas/core/indexing.py", line 1373, in __getitem__
    return self._getitem_axis(maybe_callable, axis=axis)
  File "/usr/local/lib/python3.5/dist-packages/pandas/core/indexing.py", line 1626, in _getitem_axis
    self._has_valid_type(key, axis)
  File "/usr/local/lib/python3.5/dist-packages/pandas/core/indexing.py", line 1514, in _has_valid_type
    error()
  File "/usr/local/lib/python3.5/dist-packages/pandas/core/indexing.py", line 1501, in error
    axis=self.obj._get_axis_name(axis)))
KeyError: 'the label [3] is not in the [index]'
>>> df.loc[3]
one    1004
two    2008
Name: 3, dtype: int64
>>> df.loc[6]={'one':10001,'two':20001}
>>> df
     one    two
1   1000   2000
2   1002   2004
3   1004   2008
4   1006   2012
5   1008   2016
6  10001  20001
>>> df.iloc[3]
one    1006
two    2012
Name: 4, dtype: int64
>>> df.iloc[2]
one    1004
two    2008
Name: 3, dtype: int64
>>> data = [[1,1,1],[1,2,3]]
>>> i = ['a','b','c']
>>> dat = [[0,9,8],[11,12,13]]
>>> df = pd.DataFrame(data,columns=i)
>>> df
   a  b  c
0  1  1  1
1  1  2  3
>>> df2 = pd.DataFrame(dat,columns=i)
>>> df2
    a   b   c
0   0   9   8
1  11  12  13
>>> df.append(df2)
    a   b   c
0   1   1   1
1   1   2   3
0   0   9   8
1  11  12  13
>>> df
   a  b  c
0  1  1  1
1  1  2  3
>>> df3 = df.append(df2)
>>> df3
    a   b   c
0   1   1   1
1   1   2   3
0   0   9   8
1  11  12  13
>>> #Deletion of Rows
>>> df4 = df3
>>> df3.drop(0)
    a   b   c
1   1   2   3
1  11  12  13
>>> df3
    a   b   c
0   1   1   1
1   1   2   3
0   0   9   8
1  11  12  13
>>> df4
    a   b   c
0   1   1   1
1   1   2   3
0   0   9   8
1  11  12  13
>>> df3.axes
[Int64Index([0, 1, 0, 1], dtype='int64'), Index(['a', 'b', 'c'], dtype='object')]
>>> df3.dtypes
a    int64
b    int64
c    int64
dtype: object
>>> df3.empty
False
>>> df3.ndim
2
>>> df3.size
12
>>> df3.values()
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    df3.values()
TypeError: 'numpy.ndarray' object is not callable
>>> df3.values
array([[ 1,  1,  1],
       [ 1,  2,  3],
       [ 0,  9,  8],
       [11, 12, 13]])
>>> df3.T
   0  1  0   1
a  1  1  0  11
b  1  2  9  12
c  1  3  8  13
>>> df3
    a   b   c
0   1   1   1
1   1   2   3
0   0   9   8
1  11  12  13
>>> print(df3.axes)
[Int64Index([0, 1, 0, 1], dtype='int64'), Index(['a', 'b', 'c'], dtype='object')]
>>> df3.shape
(4, 3)
>>> df3.sum()
a    13
b    24
c    25
dtype: int64
>>> df3.sum(1)
0     3
1     6
0    17
1    36
dtype: int64
>>> df3.axis(2)
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    df3.axis(2)
  File "/usr/local/lib/python3.5/dist-packages/pandas/core/generic.py", line 3614, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'axis'
>>> df3.mean()
a    3.25
b    6.00
c    6.25
dtype: float64
>>> df3.mean(1)
0     1.000000
1     2.000000
0     5.666667
1    12.000000
dtype: float64
>>> df3.std()
a    5.188127
b    5.354126
c    5.377422
dtype: float64
>>> df3.count()
a    4
b    4
c    4
dtype: int64
>>> df3.count(1)
0    3
1    3
0    3
1    3
dtype: int64
>>> df3.median()
a    1.0
b    5.5
c    5.5
dtype: float64
>>> df3.mode()
     a   b   c
0  1.0   1   1
1  NaN   2   3
2  NaN   9   8
3  NaN  12  13
>>> df3
    a   b   c
0   1   1   1
1   1   2   3
0   0   9   8
1  11  12  13
>>> df3.mode(1)
      0     1     2
0   1.0   NaN   NaN
1   1.0   2.0   3.0
0   0.0   8.0   9.0
1  11.0  12.0  13.0
>>> df3.min()
a    0
b    1
c    1
dtype: int64
>>> df3.max()
a    11
b    12
c    13
dtype: int64
>>> df3.abs()
    a   b   c
0   1   1   1
1   1   2   3
0   0   9   8
1  11  12  13
>>> df3.prod()
a      0
b    216
c    312
dtype: int64
>>> df3.describe()
               a          b          c
count   4.000000   4.000000   4.000000
mean    3.250000   6.000000   6.250000
std     5.188127   5.354126   5.377422
min     0.000000   1.000000   1.000000
25%     0.750000   1.750000   2.500000
50%     1.000000   5.500000   5.500000
75%     3.500000   9.750000   9.250000
max    11.000000  12.000000  13.000000
>>> 
