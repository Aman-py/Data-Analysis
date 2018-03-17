Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 
================ RESTART: /home/aman-py/Desktop/DSA/DFS_2.py ================
[1, 4]
[0, 4, 2, 3]
[1, 3]
[1, 4, 2]
[1, 0, 3]
dict_keys([0, 1, 2, 3, 4])
{0: [1, 4], 1: [0, 4, 2, 3], 2: [1, 3], 3: [1, 4, 2], 4: [1, 0, 3]}
0
1
4
3
2
>>> Date = [1,2,3,4,5]
>>> city = ['a','b','c','d','e']
>>> Alp = ['A','B','C','D','E']
>>> column = ['Date','City','Alp']
>>> Column_data = [Date,city,Alp]
>>> zipped = zip(column,column_data)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    zipped = zip(column,column_data)
NameError: name 'column_data' is not defined
>>> zipped = zip(column,Column_data)
>>> zipped
<zip object at 0x7f8cbe6a4bc8>
>>> print(zipped)
<zip object at 0x7f8cbe6a4bc8>
>>> dic = dict(zipped)
>>> dic
{'Date': [1, 2, 3, 4, 5], 'Alp': ['A', 'B', 'C', 'D', 'E'], 'City': ['a', 'b', 'c', 'd', 'e']}
>>> heights = [1,2,3,4,5,6,7,8,9]
>>> data = {'Heights':heights,'Sex':'M'}
>>> from pandas import *
>>> data = DataFrame(data)
>>> data
   Heights Sex
0        1   M
1        2   M
2        3   M
3        4   M
4        5   M
5        6   M
6        7   M
7        8   M
8        9   M
>>> data.
SyntaxError: invalid syntax
>>> data.Heights
0    1
1    2
2    3
3    4
4    5
5    6
6    7
7    8
8    9
Name: Heights, dtype: int64
>>> data.Sex
0    M
1    M
2    M
3    M
4    M
5    M
6    M
7    M
8    M
Name: Sex, dtype: object
>>> data.T
         0  1  2  3  4  5  6  7  8
Heights  1  2  3  4  5  6  7  8  9
Sex      M  M  M  M  M  M  M  M  M
>>> data.abs
<bound method NDFrame.abs of    Heights Sex
0        1   M
1        2   M
2        3   M
3        4   M
4        5   M
5        6   M
6        7   M
7        8   M
8        9   M>
>>> data.as_matrix
<bound method NDFrame.as_matrix of    Heights Sex
0        1   M
1        2   M
2        3   M
3        4   M
4        5   M
5        6   M
6        7   M
7        8   M
8        9   M>
>>> data.columns
Index(['Heights', 'Sex'], dtype='object')
>>> data.index = ['!','@',' ',' ',' ',' ',' ',' ',' ']
>>> data
   Heights Sex
!        1   M
@        2   M
         3   M
         4   M
         5   M
         6   M
         7   M
         8   M
         9   M
>>> data.columns = ['H']
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    data.columns = ['H']
  File "/usr/local/lib/python3.5/dist-packages/pandas/core/generic.py", line 3627, in __setattr__
    return object.__setattr__(self, name, value)
  File "pandas/_libs/properties.pyx", line 69, in pandas._libs.properties.AxisProperty.__set__
  File "/usr/local/lib/python3.5/dist-packages/pandas/core/generic.py", line 559, in _set_axis
    self._data.set_axis(axis, labels)
  File "/usr/local/lib/python3.5/dist-packages/pandas/core/internals.py", line 3074, in set_axis
    (old_len, new_len))
ValueError: Length mismatch: Expected axis has 2 elements, new values have 1 elements
>>> data.columns = ['H','S']
>>> data
   H  S
!  1  M
@  2  M
   3  M
   4  M
   5  M
   6  M
   7  M
   8  M
   9  M
>>> 
=========== RESTART: /home/aman-py/Desktop/Data Science/sunspot.py ===========
>>> 
=========== RESTART: /home/aman-py/Desktop/Data Science/sunspot.py ===========
>>> 
=========== RESTART: /home/aman-py/Desktop/Data Science/sunspot.py ===========
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 71860 entries, 0 to 71859
Data columns (total 6 columns):
1818        71860 non-null int64
01          71860 non-null int64
01.1        71860 non-null int64
1818.004    71860 non-null float64
 -1         71860 non-null int64
1           71860 non-null int64
dtypes: float64(1), int64(5)
memory usage: 3.3 MB
>>> 
=========== RESTART: /home/aman-py/Desktop/Data Science/sunspot.py ===========
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 71860 entries, 0 to 71859
Data columns (total 6 columns):
1818        71860 non-null int64
01          71860 non-null int64
01.1        71860 non-null int64
1818.004    71860 non-null float64
 -1         71860 non-null int64
1           71860 non-null int64
dtypes: float64(1), int64(5)
memory usage: 3.3 MB
>>> 
=========== RESTART: /home/aman-py/Desktop/Data Science/sunspot.py ===========
>>> 
=========== RESTART: /home/aman-py/Desktop/Data Science/sunspot.py ===========
   1818  01  01.1  1818.004   -1  1
0  1818   1     2  1818.007   -1  1
1  1818   1     3  1818.010   -1  1
2  1818   1     4  1818.012   -1  1
3  1818   1     5  1818.015   -1  1
4  1818   1     6  1818.018   -1  1
5  1818   1     7  1818.021   -1  1
6  1818   1     8  1818.023   39  1
7  1818   1     9  1818.026   -1  1
8  1818   1    10  1818.029   -1  1
9  1818   1    11  1818.031   -1  1
>>> 
=========== RESTART: /home/aman-py/Desktop/Data Science/sunspot.py ===========
   1818  01  01.1  1818.004   -1  1
0  1818   1     2  1818.007   -1  1
1  1818   1     3  1818.010   -1  1
2  1818   1     4  1818.012   -1  1
3  1818   1     5  1818.015   -1  1
4  1818   1     6  1818.018   -1  1
5  1818   1     7  1818.021   -1  1
6  1818   1     8  1818.023   39  1
7  1818   1     9  1818.026   -1  1
8  1818   1    10  1818.029   -1  1
9  1818   1    11  1818.031   -1  1
Traceback (most recent call last):
  File "/home/aman-py/Desktop/Data Science/sunspot.py", line 4, in <module>
    sunspot.shape()
TypeError: 'tuple' object is not callable
>>> 
>>> 
=========== RESTART: /home/aman-py/Desktop/Data Science/sunspot.py ===========
   1818  01  01.1  1818.004   -1  1
0  1818   1     2  1818.007   -1  1
1  1818   1     3  1818.010   -1  1
2  1818   1     4  1818.012   -1  1
3  1818   1     5  1818.015   -1  1
4  1818   1     6  1818.018   -1  1
5  1818   1     7  1818.021   -1  1
6  1818   1     8  1818.023   39  1
7  1818   1     9  1818.026   -1  1
8  1818   1    10  1818.029   -1  1
9  1818   1    11  1818.031   -1  1
>>> 
=========== RESTART: /home/aman-py/Desktop/Data Science/sunspot.py ===========
   1818  01  01.1  1818.004   -1  1
0  1818   1     2  1818.007   -1  1
1  1818   1     3  1818.010   -1  1
2  1818   1     4  1818.012   -1  1
3  1818   1     5  1818.015   -1  1
4  1818   1     6  1818.018   -1  1
5  1818   1     7  1818.021   -1  1
6  1818   1     8  1818.023   39  1
7  1818   1     9  1818.026   -1  1
8  1818   1    10  1818.029   -1  1
9  1818   1    11  1818.031   -1  1
>>> 
=========== RESTART: /home/aman-py/Desktop/Data Science/sunspot.py ===========
      0  1   2         3   4  5
0  1818  1   1  1818.004  -1  1
1  1818  1   2  1818.007  -1  1
2  1818  1   3  1818.010  -1  1
3  1818  1   4  1818.012  -1  1
4  1818  1   5  1818.015  -1  1
5  1818  1   6  1818.018  -1  1
6  1818  1   7  1818.021  -1  1
7  1818  1   8  1818.023  39  1
8  1818  1   9  1818.026  -1  1
9  1818  1  10  1818.029  -1  1
>>> 
=========== RESTART: /home/aman-py/Desktop/Data Science/sunspot.py ===========
      0  1   2         3   4  5
0  1818  1   1  1818.004  -1  1
1  1818  1   2  1818.007  -1  1
2  1818  1   3  1818.010  -1  1
3  1818  1   4  1818.012  -1  1
4  1818  1   5  1818.015  -1  1
5  1818  1   6  1818.018  -1  1
6  1818  1   7  1818.021  -1  1
7  1818  1   8  1818.023  39  1
8  1818  1   9  1818.026  -1  1
9  1818  1  10  1818.029  -1  1
>>> 
=========== RESTART: /home/aman-py/Desktop/Data Science/sunspot.py ===========
   Year  Month  Day  Decimal date  Daily sunspot number  \
0  1818      1    1      1818.004                    -1   
1  1818      1    2      1818.007                    -1   
2  1818      1    3      1818.010                    -1   
3  1818      1    4      1818.012                    -1   
4  1818      1    5      1818.015                    -1   
5  1818      1    6      1818.018                    -1   
6  1818      1    7      1818.021                    -1   
7  1818      1    8      1818.023                    39   
8  1818      1    9      1818.026                    -1   
9  1818      1   10      1818.029                    -1   

   Definitive/provisional indicator  
0                                 1  
1                                 1  
2                                 1  
3                                 1  
4                                 1  
5                                 1  
6                                 1  
7                                 1  
8                                 1  
9                                 1  
>>> 
=========== RESTART: /home/aman-py/Desktop/Data Science/sunspot.py ===========
   Year  Month  Day  Decimal date  Daily sunspot number  \
0  1818      1    1      1818.004                   NaN   
1  1818      1    2      1818.007                   NaN   
2  1818      1    3      1818.010                   NaN   
3  1818      1    4      1818.012                   NaN   
4  1818      1    5      1818.015                   NaN   
5  1818      1    6      1818.018                   NaN   
6  1818      1    7      1818.021                   NaN   
7  1818      1    8      1818.023                  39.0   
8  1818      1    9      1818.026                   NaN   
9  1818      1   10      1818.029                   NaN   

   Definitive/provisional indicator  
0                                 1  
1                                 1  
2                                 1  
3                                 1  
4                                 1  
5                                 1  
6                                 1  
7                                 1  
8                                 1  
9                                 1  
>>> 
=========== RESTART: /home/aman-py/Desktop/Data Science/sunspot.py ===========
   Year  Month  Day  Decimal date  Daily sunspot number  \
0  1818      1    1      1818.004                    -1   
1  1818      1    2      1818.007                    -1   
2  1818      1    3      1818.010                    -1   
3  1818      1    4      1818.012                    -1   
4  1818      1    5      1818.015                    -1   
5  1818      1    6      1818.018                    -1   
6  1818      1    7      1818.021                    -1   
7  1818      1    8      1818.023                    39   
8  1818      1    9      1818.026                    -1   
9  1818      1   10      1818.029                    -1   

   Definitive/provisional indicator  
0                               NaN  
1                               NaN  
2                               NaN  
3                               NaN  
4                               NaN  
5                               NaN  
6                               NaN  
7                               NaN  
8                               NaN  
9                               NaN  
>>> 
=========== RESTART: /home/aman-py/Desktop/Data Science/sunspot.py ===========
   Year  Month  Day  Decimal date  Daily sunspot number  \
0  1818      1    1      1818.004                   NaN   
1  1818      1    2      1818.007                   NaN   
2  1818      1    3      1818.010                   NaN   
3  1818      1    4      1818.012                   NaN   
4  1818      1    5      1818.015                   NaN   
5  1818      1    6      1818.018                   NaN   
6  1818      1    7      1818.021                   NaN   
7  1818      1    8      1818.023                  39.0   
8  1818      1    9      1818.026                   NaN   
9  1818      1   10      1818.029                   NaN   

   Definitive/provisional indicator  
0                                 1  
1                                 1  
2                                 1  
3                                 1  
4                                 1  
5                                 1  
6                                 1  
7                                 1  
8                                 1  
9                                 1  
>>> 
=========== RESTART: /home/aman-py/Desktop/Data Science/sunspot.py ===========
   Year  Month  Day  Decimal date  Daily sunspot number  \
0  1818      1    1      1818.004                   NaN   
1  1818      1    2      1818.007                   NaN   
2  1818      1    3      1818.010                   NaN   
3  1818      1    4      1818.012                   NaN   
4  1818      1    5      1818.015                   NaN   
5  1818      1    6      1818.018                   NaN   
6  1818      1    7      1818.021                   NaN   
7  1818      1    8      1818.023                  39.0   
8  1818      1    9      1818.026                   NaN   
9  1818      1   10      1818.029                   NaN   

   Definitive/provisional indicator  
0                                 1  
1                                 1  
2                                 1  
3                                 1  
4                                 1  
5                                 1  
6                                 1  
7                                 1  
8                                 1  
9                                 1  
>>> 
=========== RESTART: /home/aman-py/Desktop/Data Science/sunspot.py ===========
   Year  Month  Day  Decimal date  Daily sunspot number  \
0  1818      1    1      1818.004                   NaN   
1  1818      1    2      1818.007                   NaN   
2  1818      1    3      1818.010                   NaN   
3  1818      1    4      1818.012                   NaN   
4  1818      1    5      1818.015                   NaN   
5  1818      1    6      1818.018                   NaN   
6  1818      1    7      1818.021                   NaN   
7  1818      1    8      1818.023                  39.0   
8  1818      1    9      1818.026                   NaN   
9  1818      1   10      1818.029                   NaN   

   Definitive/provisional indicator  
0                                 1  
1                                 1  
2                                 1  
3                                 1  
4                                 1  
5                                 1  
6                                 1  
7                                 1  
8                                 1  
9                                 1  
>>> 
=========== RESTART: /home/aman-py/Desktop/Data Science/sunspot.py ===========
   Year  Month  Day  Decimal date  Daily sunspot number  \
0  1818      1    1      1818.004                   NaN   
1  1818      1    2      1818.007                   NaN   
2  1818      1    3      1818.010                   NaN   
3  1818      1    4      1818.012                   NaN   
4  1818      1    5      1818.015                   NaN   
5  1818      1    6      1818.018                   NaN   
6  1818      1    7      1818.021                   NaN   
7  1818      1    8      1818.023                  39.0   
8  1818      1    9      1818.026                   NaN   
9  1818      1   10      1818.029                   NaN   

   Definitive/provisional indicator  
0                                 1  
1                                 1  
2                                 1  
3                                 1  
4                                 1  
5                                 1  
6                                 1  
7                                 1  
8                                 1  
9                                 1  
>>> 
=========== RESTART: /home/aman-py/Desktop/Data Science/sunspot.py ===========
  Year_Month_Day  Decimal date  Daily sunspot number  \
0     1818-01-01      1818.004                   NaN   
1     1818-01-02      1818.007                   NaN   
2     1818-01-03      1818.010                   NaN   
3     1818-01-04      1818.012                   NaN   
4     1818-01-05      1818.015                   NaN   
5     1818-01-06      1818.018                   NaN   
6     1818-01-07      1818.021                   NaN   
7     1818-01-08      1818.023                  39.0   
8     1818-01-09      1818.026                   NaN   
9     1818-01-10      1818.029                   NaN   

   Definitive/provisional indicator  
0                                 1  
1                                 1  
2                                 1  
3                                 1  
4                                 1  
5                                 1  
6                                 1  
7                                 1  
8                                 1  
9                                 1  
>>> 
=========== RESTART: /home/aman-py/Desktop/Data Science/sunspot.py ===========
  Year_Month_Decimal date  Day  Daily sunspot number  \
0        1818 01 1818.004    1                   NaN   
1        1818 01 1818.007    2                   NaN   
2        1818 01 1818.010    3                   NaN   
3        1818 01 1818.012    4                   NaN   
4        1818 01 1818.015    5                   NaN   
5        1818 01 1818.018    6                   NaN   
6        1818 01 1818.021    7                   NaN   
7        1818 01 1818.023    8                  39.0   
8        1818 01 1818.026    9                   NaN   
9        1818 01 1818.029   10                   NaN   

   Definitive/provisional indicator  
0                                 1  
1                                 1  
2                                 1  
3                                 1  
4                                 1  
5                                 1  
6                                 1  
7                                 1  
8                                 1  
9                                 1  
>>> 
=========== RESTART: /home/aman-py/Desktop/Data Science/sunspot.py ===========
  Year_Month_Day  Decimal date  Daily sunspot number  \
0     1818-01-01      1818.004                   NaN   
1     1818-01-02      1818.007                   NaN   
2     1818-01-03      1818.010                   NaN   
3     1818-01-04      1818.012                   NaN   
4     1818-01-05      1818.015                   NaN   
5     1818-01-06      1818.018                   NaN   
6     1818-01-07      1818.021                   NaN   
7     1818-01-08      1818.023                  39.0   
8     1818-01-09      1818.026                   NaN   
9     1818-01-10      1818.029                   NaN   

   Definitive/provisional indicator  
0                                 1  
1                                 1  
2                                 1  
3                                 1  
4                                 1  
5                                 1  
6                                 1  
7                                 1  
8                                 1  
9                                 1  
>>> 
=========== RESTART: /home/aman-py/Desktop/Data Science/sunspot.py ===========
  Year_Month_Day  Decimal date  Daily sunspot number  \
0     1818-01-01      1818.004                   NaN   
1     1818-01-02      1818.007                   NaN   
2     1818-01-03      1818.010                   NaN   
3     1818-01-04      1818.012                   NaN   
4     1818-01-05      1818.015                   NaN   
5     1818-01-06      1818.018                   NaN   
6     1818-01-07      1818.021                   NaN   
7     1818-01-08      1818.023                  39.0   
8     1818-01-09      1818.026                   NaN   
9     1818-01-10      1818.029                   NaN   

   Definitive/provisional indicator  
0                                 1  
1                                 1  
2                                 1  
3                                 1  
4                                 1  
5                                 1  
6                                 1  
7                                 1  
8                                 1  
9                                 1  
>>> 
=========== RESTART: /home/aman-py/Desktop/Data Science/sunspot.py ===========
  Year_Month_Day  Decimal date  Daily sunspot number  \
0     1818-01-01      1818.004                   NaN   
1     1818-01-02      1818.007                   NaN   
2     1818-01-03      1818.010                   NaN   
3     1818-01-04      1818.012                   NaN   
4     1818-01-05      1818.015                   NaN   
5     1818-01-06      1818.018                   NaN   
6     1818-01-07      1818.021                   NaN   
7     1818-01-08      1818.023                  39.0   
8     1818-01-09      1818.026                   NaN   
9     1818-01-10      1818.029                   NaN   

   Definitive/provisional indicator  
0                                 1  
1                                 1  
2                                 1  
3                                 1  
4                                 1  
5                                 1  
6                                 1  
7                                 1  
8                                 1  
9                                 1  
       Decimal date  Definitive/provisional indicator
0          1818.004                                 1
1          1818.007                                 1
2          1818.010                                 1
3          1818.012                                 1
4          1818.015                                 1
5          1818.018                                 1
6          1818.021                                 1
7          1818.023                                 1
8          1818.026                                 1
9          1818.029                                 1
10         1818.031                                 1
11         1818.034                                 1
12         1818.037                                 1
13         1818.040                                 1
14         1818.042                                 1
15         1818.045                                 1
16         1818.048                                 1
17         1818.051                                 1
18         1818.053                                 1
19         1818.056                                 1
20         1818.059                                 1
21         1818.062                                 1
22         1818.064                                 1
23         1818.067                                 1
24         1818.070                                 1
25         1818.073                                 1
26         1818.075                                 1
27         1818.078                                 1
28         1818.081                                 1
29         1818.083                                 1
...             ...                               ...
71831      2014.667                                 0
71832      2014.669                                 0
71833      2014.672                                 0
71834      2014.675                                 0
71835      2014.678                                 0
71836      2014.680                                 0
71837      2014.683                                 0
71838      2014.686                                 0
71839      2014.689                                 0
71840      2014.691                                 0
71841      2014.694                                 0
71842      2014.697                                 0
71843      2014.699                                 0
71844      2014.702                                 0
71845      2014.705                                 0
71846      2014.708                                 0
71847      2014.710                                 0
71848      2014.713                                 0
71849      2014.716                                 0
71850      2014.719                                 0
71851      2014.721                                 0
71852      2014.724                                 0
71853      2014.727                                 0
71854      2014.730                                 0
71855      2014.732                                 0
71856      2014.735                                 0
71857      2014.738                                 0
71858      2014.741                                 0
71859      2014.743                                 0
71860      2014.746                                 0

[71861 rows x 2 columns]
>>> import pandas as pd
>>> import matplotlib.pyplot as plt
>>> data = pd.read_csv('/home/aman-py/Desktop/Data Science/aapl.csv',index_col='date',parse_dates=True)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    data = pd.read_csv('/home/aman-py/Desktop/Data Science/aapl.csv',index_col='date',parse_dates=True)
  File "/usr/local/lib/python3.5/dist-packages/pandas/io/parsers.py", line 709, in parser_f
    return _read(filepath_or_buffer, kwds)
  File "/usr/local/lib/python3.5/dist-packages/pandas/io/parsers.py", line 449, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/usr/local/lib/python3.5/dist-packages/pandas/io/parsers.py", line 818, in __init__
    self._make_engine(self.engine)
  File "/usr/local/lib/python3.5/dist-packages/pandas/io/parsers.py", line 1049, in _make_engine
    self._engine = CParserWrapper(self.f, **self.options)
  File "/usr/local/lib/python3.5/dist-packages/pandas/io/parsers.py", line 1749, in __init__
    self._set_noconvert_columns()
  File "/usr/local/lib/python3.5/dist-packages/pandas/io/parsers.py", line 1830, in _set_noconvert_columns
    _set(k)
  File "/usr/local/lib/python3.5/dist-packages/pandas/io/parsers.py", line 1807, in _set
    x = names.index(x)
ValueError: 'date' is not in list
>>> data
       Decimal date  Definitive/provisional indicator
0          1818.004                                 1
1          1818.007                                 1
2          1818.010                                 1
3          1818.012                                 1
4          1818.015                                 1
5          1818.018                                 1
6          1818.021                                 1
7          1818.023                                 1
8          1818.026                                 1
9          1818.029                                 1
10         1818.031                                 1
11         1818.034                                 1
12         1818.037                                 1
13         1818.040                                 1
14         1818.042                                 1
15         1818.045                                 1
16         1818.048                                 1
17         1818.051                                 1
18         1818.053                                 1
19         1818.056                                 1
20         1818.059                                 1
21         1818.062                                 1
22         1818.064                                 1
23         1818.067                                 1
24         1818.070                                 1
25         1818.073                                 1
26         1818.075                                 1
27         1818.078                                 1
28         1818.081                                 1
29         1818.083                                 1
...             ...                               ...
71831      2014.667                                 0
71832      2014.669                                 0
71833      2014.672                                 0
71834      2014.675                                 0
71835      2014.678                                 0
71836      2014.680                                 0
71837      2014.683                                 0
71838      2014.686                                 0
71839      2014.689                                 0
71840      2014.691                                 0
71841      2014.694                                 0
71842      2014.697                                 0
71843      2014.699                                 0
71844      2014.702                                 0
71845      2014.705                                 0
71846      2014.708                                 0
71847      2014.710                                 0
71848      2014.713                                 0
71849      2014.716                                 0
71850      2014.719                                 0
71851      2014.721                                 0
71852      2014.724                                 0
71853      2014.727                                 0
71854      2014.730                                 0
71855      2014.732                                 0
71856      2014.735                                 0
71857      2014.738                                 0
71858      2014.741                                 0
71859      2014.743                                 0
71860      2014.746                                 0

[71861 rows x 2 columns]
>>> data = pd.read_csv('/home/aman-py/Desktop/Data Science/aapl.csv')
>>> data
            Date    Open    High     Low   Close    Volume  Adj Close
0     2008-10-14  116.26  116.40  103.14  104.08  70749800     104.08
1     2008-10-13  104.55  110.53  101.02  110.26  54967000     110.26
2     2008-10-10   85.70  100.00   85.00   96.80  79260700      96.80
3     2008-10-09   93.35   95.80   86.60   88.74  57763700      88.74
4     2008-10-08   85.91   96.33   85.68   89.79  78847900      89.79
5     2008-10-07  100.48  101.50   88.95   89.16  67099000      89.16
6     2008-10-06   91.96   98.78   87.54   98.14  75264900      98.14
7     2008-10-03  104.00  106.50   94.65   97.07  81942800      97.07
8     2008-10-02  108.01  108.79  100.00  100.10  57477300     100.10
9     2008-10-01  111.92  112.36  107.39  109.12  46303000     109.12
10    2008-09-30  108.25  115.00  106.30  113.66  58095800     113.66
11    2008-09-29  119.62  119.68  100.59  105.26  93581400     105.26
12    2008-09-26  124.91  129.80  123.00  128.24  40208700     128.24
13    2008-09-25  129.80  134.79  128.52  131.93  35865600     131.93
14    2008-09-24  127.27  130.95  125.15  128.71  37393400     128.71
15    2008-09-23  131.85  135.80  126.66  126.84  45727300     126.84
16    2008-09-22  139.94  140.25  130.66  131.05  30577300     131.05
17    2008-09-19  142.60  144.20  136.31  140.91  51102700     140.91
18    2008-09-18  130.57  135.43  120.68  134.09  59819300     134.09
19    2008-09-17  138.49  138.51  127.83  127.83  42847200     127.83
20    2008-09-16  133.86  142.50  132.15  139.88  42804800     139.88
21    2008-09-15  142.03  147.69  140.36  140.36  32852600     140.36
22    2008-09-12  150.91  150.91  146.50  148.94  28322400     148.94
23    2008-09-11  148.18  152.99  146.00  152.65  34666800     152.65
24    2008-09-10  152.32  154.99  148.80  151.61  34755100     151.61
25    2008-09-09  156.86  159.96  149.79  151.68  44442500     151.68
26    2008-09-08  164.57  164.89  151.46  157.92  37356400     157.92
27    2008-09-05  158.59  162.40  157.65  160.18  28083800     160.18
28    2008-09-04  165.86  167.91  160.81  161.22  26549500     161.22
29    2008-09-03  166.84  168.68  164.00  166.96  26244100     166.96
...          ...     ...     ...     ...     ...       ...        ...
6051  1984-10-18   25.62   25.75   25.62   25.62   8842400       2.92
6052  1984-10-17   24.87   25.00   24.87   24.87   5636000       2.84
6053  1984-10-16   24.00   24.12   23.87   23.87   4246400       2.72
6054  1984-10-15   24.00   24.25   24.00   24.00   8715200       2.74
6055  1984-10-12   23.75   23.87   22.50   22.75   9522400       2.60
6056  1984-10-11   23.87   24.50   23.75   23.75   6553600       2.71
6057  1984-10-10   24.62   24.62   23.87   23.87  13070400       2.72
6058  1984-10-09   24.87   25.00   24.62   24.62   4515200       2.81
6059  1984-10-08   24.87   25.00   24.87   24.87   1721600       2.84
6060  1984-10-05   25.37   25.37   24.75   24.87   3510400       2.84
6061  1984-10-04   25.37   25.62   25.37   25.37   4482400       2.89
6062  1984-10-03   25.12   25.50   25.12   25.12   4335200       2.87
6063  1984-10-02   24.75   25.62   24.75   24.75   4258400       2.82
6064  1984-10-01   25.00   25.00   24.50   24.50   3521600       2.80
6065  1984-09-28   25.75   25.75   24.62   25.12   8344800       2.87
6066  1984-09-27   25.75   25.87   25.75   25.75   3796000       2.94
6067  1984-09-26   26.12   27.25   25.75   25.75   3987200       2.94
6068  1984-09-25   26.50   26.50   26.12   26.12   5977600       2.98
6069  1984-09-24   26.87   27.00   26.62   26.62   2833600       3.04
6070  1984-09-21   27.12   27.87   26.50   26.87   3591200       3.07
6071  1984-09-20   27.12   27.37   27.12   27.12   2387200       3.09
6072  1984-09-19   27.62   27.87   27.00   27.00   3816000       3.08
6073  1984-09-18   28.62   28.87   27.62   27.62   3495200       3.15
6074  1984-09-17   28.62   29.00   28.62   28.62   6886400       3.27
6075  1984-09-14   27.62   28.50   27.62   27.87   8826400       3.18
6076  1984-09-13   27.50   27.62   27.50   27.50   7429600       3.14
6077  1984-09-12   26.87   27.00   26.12   26.12   4773600       2.98
6078  1984-09-11   26.62   27.37   26.62   26.87   5444000       3.07
6079  1984-09-10   26.50   26.62   25.87   26.37   2346400       3.01
6080  1984-09-07   26.50   26.87   26.25   26.50   2981600       3.02

[6081 rows x 7 columns]
>>> data = pd.read_csv('/home/aman-py/Desktop/Data Science/aapl.csv',index_col='Date',parse_dates=True)
>>> data
              Open    High     Low   Close    Volume  Adj Close
Date                                                           
2008-10-14  116.26  116.40  103.14  104.08  70749800     104.08
2008-10-13  104.55  110.53  101.02  110.26  54967000     110.26
2008-10-10   85.70  100.00   85.00   96.80  79260700      96.80
2008-10-09   93.35   95.80   86.60   88.74  57763700      88.74
2008-10-08   85.91   96.33   85.68   89.79  78847900      89.79
2008-10-07  100.48  101.50   88.95   89.16  67099000      89.16
2008-10-06   91.96   98.78   87.54   98.14  75264900      98.14
2008-10-03  104.00  106.50   94.65   97.07  81942800      97.07
2008-10-02  108.01  108.79  100.00  100.10  57477300     100.10
2008-10-01  111.92  112.36  107.39  109.12  46303000     109.12
2008-09-30  108.25  115.00  106.30  113.66  58095800     113.66
2008-09-29  119.62  119.68  100.59  105.26  93581400     105.26
2008-09-26  124.91  129.80  123.00  128.24  40208700     128.24
2008-09-25  129.80  134.79  128.52  131.93  35865600     131.93
2008-09-24  127.27  130.95  125.15  128.71  37393400     128.71
2008-09-23  131.85  135.80  126.66  126.84  45727300     126.84
2008-09-22  139.94  140.25  130.66  131.05  30577300     131.05
2008-09-19  142.60  144.20  136.31  140.91  51102700     140.91
2008-09-18  130.57  135.43  120.68  134.09  59819300     134.09
2008-09-17  138.49  138.51  127.83  127.83  42847200     127.83
2008-09-16  133.86  142.50  132.15  139.88  42804800     139.88
2008-09-15  142.03  147.69  140.36  140.36  32852600     140.36
2008-09-12  150.91  150.91  146.50  148.94  28322400     148.94
2008-09-11  148.18  152.99  146.00  152.65  34666800     152.65
2008-09-10  152.32  154.99  148.80  151.61  34755100     151.61
2008-09-09  156.86  159.96  149.79  151.68  44442500     151.68
2008-09-08  164.57  164.89  151.46  157.92  37356400     157.92
2008-09-05  158.59  162.40  157.65  160.18  28083800     160.18
2008-09-04  165.86  167.91  160.81  161.22  26549500     161.22
2008-09-03  166.84  168.68  164.00  166.96  26244100     166.96
...            ...     ...     ...     ...       ...        ...
1984-10-18   25.62   25.75   25.62   25.62   8842400       2.92
1984-10-17   24.87   25.00   24.87   24.87   5636000       2.84
1984-10-16   24.00   24.12   23.87   23.87   4246400       2.72
1984-10-15   24.00   24.25   24.00   24.00   8715200       2.74
1984-10-12   23.75   23.87   22.50   22.75   9522400       2.60
1984-10-11   23.87   24.50   23.75   23.75   6553600       2.71
1984-10-10   24.62   24.62   23.87   23.87  13070400       2.72
1984-10-09   24.87   25.00   24.62   24.62   4515200       2.81
1984-10-08   24.87   25.00   24.87   24.87   1721600       2.84
1984-10-05   25.37   25.37   24.75   24.87   3510400       2.84
1984-10-04   25.37   25.62   25.37   25.37   4482400       2.89
1984-10-03   25.12   25.50   25.12   25.12   4335200       2.87
1984-10-02   24.75   25.62   24.75   24.75   4258400       2.82
1984-10-01   25.00   25.00   24.50   24.50   3521600       2.80
1984-09-28   25.75   25.75   24.62   25.12   8344800       2.87
1984-09-27   25.75   25.87   25.75   25.75   3796000       2.94
1984-09-26   26.12   27.25   25.75   25.75   3987200       2.94
1984-09-25   26.50   26.50   26.12   26.12   5977600       2.98
1984-09-24   26.87   27.00   26.62   26.62   2833600       3.04
1984-09-21   27.12   27.87   26.50   26.87   3591200       3.07
1984-09-20   27.12   27.37   27.12   27.12   2387200       3.09
1984-09-19   27.62   27.87   27.00   27.00   3816000       3.08
1984-09-18   28.62   28.87   27.62   27.62   3495200       3.15
1984-09-17   28.62   29.00   28.62   28.62   6886400       3.27
1984-09-14   27.62   28.50   27.62   27.87   8826400       3.18
1984-09-13   27.50   27.62   27.50   27.50   7429600       3.14
1984-09-12   26.87   27.00   26.12   26.12   4773600       2.98
1984-09-11   26.62   27.37   26.62   26.87   5444000       3.07
1984-09-10   26.50   26.62   25.87   26.37   2346400       3.01
1984-09-07   26.50   26.87   26.25   26.50   2981600       3.02

[6081 rows x 6 columns]
>>> close_arr = data['close'].values
Traceback (most recent call last):
  File "/usr/local/lib/python3.5/dist-packages/pandas/core/indexes/base.py", line 2525, in get_loc
    return self._engine.get_loc(key)
  File "pandas/_libs/index.pyx", line 117, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 139, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 1265, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 1273, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'close'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    close_arr = data['close'].values
  File "/usr/local/lib/python3.5/dist-packages/pandas/core/frame.py", line 2139, in __getitem__
    return self._getitem_column(key)
  File "/usr/local/lib/python3.5/dist-packages/pandas/core/frame.py", line 2146, in _getitem_column
    return self._get_item_cache(key)
  File "/usr/local/lib/python3.5/dist-packages/pandas/core/generic.py", line 1842, in _get_item_cache
    values = self._data.get(item)
  File "/usr/local/lib/python3.5/dist-packages/pandas/core/internals.py", line 3843, in get
    loc = self.items.get_loc(item)
  File "/usr/local/lib/python3.5/dist-packages/pandas/core/indexes/base.py", line 2527, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas/_libs/index.pyx", line 117, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 139, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 1265, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 1273, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'close'
>>> close_arr = data['Close'].values
>>> type(close_arr)
<class 'numpy.ndarray'>
>>> plt.plot(close_arr)
[<matplotlib.lines.Line2D object at 0x7fa7cea624e0>]
>>> plt.show()
>>> close_series = data['Close']
>>> plt.plot(close_series)
[<matplotlib.lines.Line2D object at 0x7fa7cea479e8>]
>>> plt.show()
>>> data.plot()
<matplotlib.axes._subplots.AxesSubplot object at 0x7fa7ce9f5da0>
>>> plt.show()
>>> data.plot()
<matplotlib.axes._subplots.AxesSubplot object at 0x7fa7ce92a320>
>>> plt.yscale('log10')
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    plt.yscale('log10')
  File "/usr/local/lib/python3.5/dist-packages/matplotlib/pyplot.py", line 1630, in yscale
    gca().set_yscale(*args, **kwargs)
  File "/usr/local/lib/python3.5/dist-packages/matplotlib/axes/_base.py", line 3503, in set_yscale
    ax.yaxis._set_scale(value, **kwargs)
  File "/usr/local/lib/python3.5/dist-packages/matplotlib/axis.py", line 768, in _set_scale
    self._scale = mscale.scale_factory(value, self, **kwargs)
  File "/usr/local/lib/python3.5/dist-packages/matplotlib/scale.py", line 568, in scale_factory
    raise ValueError("Unknown scale type '%s'" % scale)
ValueError: Unknown scale type 'log10'
>>> plt.yscale(log10)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    plt.yscale(log10)
NameError: name 'log10' is not defined
>>> plt.yscale('log')
>>> plt.show()
>>> aapl['Open'].plot(color='b',style ='.-',legend=True)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    aapl['Open'].plot(color='b',style ='.-',legend=True)
NameError: name 'aapl' is not defined
>>> data['Open'].plot(color='b',style ='.-',legend=True)
<matplotlib.axes._subplots.AxesSubplot object at 0x7fa7ce6f3f28>
>>> plt.show()
>>> data['Open'].plot(color='b',style ='.-',legend=True)
<matplotlib.axes._subplots.AxesSubplot object at 0x7fa7ce59cf28>
>>> data['Close'].plot(color='r',style ='.',legend=True)
<matplotlib.axes._subplots.AxesSubplot object at 0x7fa7ce59cf28>
>>> plt.axis('2001','2002',0,100)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    plt.axis('2001','2002',0,100)
  File "/usr/local/lib/python3.5/dist-packages/matplotlib/pyplot.py", line 1498, in axis
    return gca().axis(*v, **kwargs)
  File "/usr/local/lib/python3.5/dist-packages/matplotlib/axes/_base.py", line 1779, in axis
    self.set_xlim([v[0], v[1]], emit=emit, auto=False)
  File "/usr/local/lib/python3.5/dist-packages/matplotlib/axes/_base.py", line 3125, in set_xlim
    left, right = mtransforms.nonsingular(left, right, increasing=False)
  File "/usr/local/lib/python3.5/dist-packages/matplotlib/transforms.py", line 2937, in nonsingular
    if (not np.isfinite(vmin)) or (not np.isfinite(vmax)):
TypeError: ufunc 'isfinite' not supported for the input types, and the inputs could not be safely coerced to any supported types according to the casting rule ''safe''
>>> plt.axis(('2001','2002',0,100))
('2001', '2002', 0, 100)
>>> plt.show()
>>> 
