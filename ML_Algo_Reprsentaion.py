Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> a = ['aman','agarwal','loves','pooja']
>>> print(''.join(a))
amanagarwallovespooja
>>> print(' '.join(a))
aman agarwal loves pooja
>>> import sklearn
>>> print(sklearn)
<module 'sklearn' from '/usr/local/lib/python3.5/dist-packages/sklearn/__init__.py'>
>>> n = 10
>>> re = 1<n<9
>>> print(re)
False
>>> b = ' '.join(a)
>>> print(b[::-1])
ajoop sevol lawraga nama
>>> def x():
	return 1,2,3,4

>>> a,b,c = x()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a,b,c = x()
ValueError: too many values to unpack (expected 3)
>>> a,b,c,d = x()
>>> print(a,b,c,d)
1 2 3 4
>>> test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
>>> print(max(set(test),key=test.count))
4
>>> import sys
>>> x = 10000
>>> print(sys.getsizeof(x))
28
>>> import pandas
>>> import pandas as pd
>>> data = pd.read_csv('/home/aman-py/Desktop/Data Science/breast_cancer.csv')
>>> data1 = pd.DataFrame(data)
>>> data1
     Sample code number  Clump Thickness  Uniformity of Cell Size  \
0               1000025                5                        1   
1               1002945                5                        4   
2               1015425                3                        1   
3               1016277                6                        8   
4               1017023                4                        1   
5               1017122                8                       10   
6               1018099                1                        1   
7               1018561                2                        1   
8               1033078                2                        1   
9               1033078                4                        2   
10              1035283                1                        1   
11              1036172                2                        1   
12              1041801                5                        3   
13              1043999                1                        1   
14              1044572                8                        7   
15              1047630                7                        4   
16              1048672                4                        1   
17              1049815                4                        1   
18              1050670               10                        7   
19              1050718                6                        1   
20              1054590                7                        3   
21              1054593               10                        5   
22              1056784                3                        1   
23              1057013                8                        4   
24              1059552                1                        1   
25              1065726                5                        2   
26              1066373                3                        2   
27              1066979                5                        1   
28              1067444                2                        1   
29              1070935                1                        1   
..                  ...              ...                      ...   
669             1350423                5                       10   
670             1352848                3                       10   
671             1353092                3                        2   
672             1354840                2                        1   
673             1354840                5                        3   
674             1355260                1                        1   
675             1365075                4                        1   
676             1365328                1                        1   
677             1368267                5                        1   
678             1368273                1                        1   
679             1368882                2                        1   
680             1369821               10                       10   
681             1371026                5                       10   
682             1371920                5                        1   
683              466906                1                        1   
684              466906                1                        1   
685              534555                1                        1   
686              536708                1                        1   
687              566346                3                        1   
688              603148                4                        1   
689              654546                1                        1   
690              654546                1                        1   
691              695091                5                       10   
692              714039                3                        1   
693              763235                3                        1   
694              776715                3                        1   
695              841769                2                        1   
696              888820                5                       10   
697              897471                4                        8   
698              897471                4                        8   

     Uniformity of Cell Shape  Marginal Adhesion  Single Epithelial Cell Size  \
0                           1                  1                            2   
1                           4                  5                            7   
2                           1                  1                            2   
3                           8                  1                            3   
4                           1                  3                            2   
5                          10                  8                            7   
6                           1                  1                            2   
7                           2                  1                            2   
8                           1                  1                            2   
9                           1                  1                            2   
10                          1                  1                            1   
11                          1                  1                            2   
12                          3                  3                            2   
13                          1                  1                            2   
14                          5                 10                            7   
15                          6                  4                            6   
16                          1                  1                            2   
17                          1                  1                            2   
18                          7                  6                            4   
19                          1                  1                            2   
20                          2                 10                            5   
21                          5                  3                            6   
22                          1                  1                            2   
23                          5                  1                            2   
24                          1                  1                            2   
25                          3                  4                            2   
26                          1                  1                            1   
27                          1                  1                            2   
28                          1                  1                            2   
29                          3                  1                            2   
..                        ...                ...                          ...   
669                        10                  8                            5   
670                         7                  8                            5   
671                         1                  2                            2   
672                         1                  1                            2   
673                         2                  1                            3   
674                         1                  1                            2   
675                         4                  1                            2   
676                         2                  1                            2   
677                         1                  1                            2   
678                         1                  1                            2   
679                         1                  1                            2   
680                        10                 10                            5   
681                        10                 10                            4   
682                         1                  1                            2   
683                         1                  1                            2   
684                         1                  1                            2   
685                         1                  1                            2   
686                         1                  1                            2   
687                         1                  1                            2   
688                         1                  1                            2   
689                         1                  1                            2   
690                         1                  3                            2   
691                        10                  5                            4   
692                         1                  1                            2   
693                         1                  1                            2   
694                         1                  1                            3   
695                         1                  1                            2   
696                        10                  3                            7   
697                         6                  4                            3   
698                         8                  5                            4   

    Bare Nuclei  Bland Chromatin  Normal Nucleoli  Mitoses  Class  
0             1                3                1        1      2  
1            10                3                2        1      2  
2             2                3                1        1      2  
3             4                3                7        1      2  
4             1                3                1        1      2  
5            10                9                7        1      4  
6            10                3                1        1      2  
7             1                3                1        1      2  
8             1                1                1        5      2  
9             1                2                1        1      2  
10            1                3                1        1      2  
11            1                2                1        1      2  
12            3                4                4        1      4  
13            3                3                1        1      2  
14            9                5                5        4      4  
15            1                4                3        1      4  
16            1                2                1        1      2  
17            1                3                1        1      2  
18           10                4                1        2      4  
19            1                3                1        1      2  
20           10                5                4        4      4  
21            7                7               10        1      4  
22            1                2                1        1      2  
23            ?                7                3        1      4  
24            1                3                1        1      2  
25            7                3                6        1      4  
26            1                2                1        1      2  
27            1                2                1        1      2  
28            1                2                1        1      2  
29            1                1                1        1      2  
..          ...              ...              ...      ...    ...  
669           5                7               10        1      4  
670           8                7                4        1      4  
671           1                3                1        1      2  
672           1                3                1        1      2  
673           1                1                1        1      2  
674           1                2                1        1      2  
675           1                1                1        1      2  
676           1                2                1        1      2  
677           1                1                1        1      2  
678           1                1                1        1      2  
679           1                1                1        1      2  
680          10               10               10        7      4  
681          10                5                6        3      4  
682           1                3                2        1      2  
683           1                1                1        1      2  
684           1                1                1        1      2  
685           1                1                1        1      2  
686           1                1                1        1      2  
687           1                2                3        1      2  
688           1                1                1        1      2  
689           1                1                1        8      2  
690           1                1                1        1      2  
691           5                4                4        1      4  
692           1                1                1        1      2  
693           1                2                1        2      2  
694           2                1                1        1      2  
695           1                1                1        1      2  
696           3                8               10        2      4  
697           4               10                6        1      4  
698           5               10                4        1      4  

[699 rows x 11 columns]
>>> data1.set_index('Sample code number',inplace=True)
>>> data1
                    Clump Thickness  Uniformity of Cell Size  \
Sample code number                                             
1000025                           5                        1   
1002945                           5                        4   
1015425                           3                        1   
1016277                           6                        8   
1017023                           4                        1   
1017122                           8                       10   
1018099                           1                        1   
1018561                           2                        1   
1033078                           2                        1   
1033078                           4                        2   
1035283                           1                        1   
1036172                           2                        1   
1041801                           5                        3   
1043999                           1                        1   
1044572                           8                        7   
1047630                           7                        4   
1048672                           4                        1   
1049815                           4                        1   
1050670                          10                        7   
1050718                           6                        1   
1054590                           7                        3   
1054593                          10                        5   
1056784                           3                        1   
1057013                           8                        4   
1059552                           1                        1   
1065726                           5                        2   
1066373                           3                        2   
1066979                           5                        1   
1067444                           2                        1   
1070935                           1                        1   
...                             ...                      ...   
1350423                           5                       10   
1352848                           3                       10   
1353092                           3                        2   
1354840                           2                        1   
1354840                           5                        3   
1355260                           1                        1   
1365075                           4                        1   
1365328                           1                        1   
1368267                           5                        1   
1368273                           1                        1   
1368882                           2                        1   
1369821                          10                       10   
1371026                           5                       10   
1371920                           5                        1   
466906                            1                        1   
466906                            1                        1   
534555                            1                        1   
536708                            1                        1   
566346                            3                        1   
603148                            4                        1   
654546                            1                        1   
654546                            1                        1   
695091                            5                       10   
714039                            3                        1   
763235                            3                        1   
776715                            3                        1   
841769                            2                        1   
888820                            5                       10   
897471                            4                        8   
897471                            4                        8   

                    Uniformity of Cell Shape  Marginal Adhesion  \
Sample code number                                                
1000025                                    1                  1   
1002945                                    4                  5   
1015425                                    1                  1   
1016277                                    8                  1   
1017023                                    1                  3   
1017122                                   10                  8   
1018099                                    1                  1   
1018561                                    2                  1   
1033078                                    1                  1   
1033078                                    1                  1   
1035283                                    1                  1   
1036172                                    1                  1   
1041801                                    3                  3   
1043999                                    1                  1   
1044572                                    5                 10   
1047630                                    6                  4   
1048672                                    1                  1   
1049815                                    1                  1   
1050670                                    7                  6   
1050718                                    1                  1   
1054590                                    2                 10   
1054593                                    5                  3   
1056784                                    1                  1   
1057013                                    5                  1   
1059552                                    1                  1   
1065726                                    3                  4   
1066373                                    1                  1   
1066979                                    1                  1   
1067444                                    1                  1   
1070935                                    3                  1   
...                                      ...                ...   
1350423                                   10                  8   
1352848                                    7                  8   
1353092                                    1                  2   
1354840                                    1                  1   
1354840                                    2                  1   
1355260                                    1                  1   
1365075                                    4                  1   
1365328                                    2                  1   
1368267                                    1                  1   
1368273                                    1                  1   
1368882                                    1                  1   
1369821                                   10                 10   
1371026                                   10                 10   
1371920                                    1                  1   
466906                                     1                  1   
466906                                     1                  1   
534555                                     1                  1   
536708                                     1                  1   
566346                                     1                  1   
603148                                     1                  1   
654546                                     1                  1   
654546                                     1                  3   
695091                                    10                  5   
714039                                     1                  1   
763235                                     1                  1   
776715                                     1                  1   
841769                                     1                  1   
888820                                    10                  3   
897471                                     6                  4   
897471                                     8                  5   

                    Single Epithelial Cell Size Bare Nuclei  Bland Chromatin  \
Sample code number                                                             
1000025                                       2           1                3   
1002945                                       7          10                3   
1015425                                       2           2                3   
1016277                                       3           4                3   
1017023                                       2           1                3   
1017122                                       7          10                9   
1018099                                       2          10                3   
1018561                                       2           1                3   
1033078                                       2           1                1   
1033078                                       2           1                2   
1035283                                       1           1                3   
1036172                                       2           1                2   
1041801                                       2           3                4   
1043999                                       2           3                3   
1044572                                       7           9                5   
1047630                                       6           1                4   
1048672                                       2           1                2   
1049815                                       2           1                3   
1050670                                       4          10                4   
1050718                                       2           1                3   
1054590                                       5          10                5   
1054593                                       6           7                7   
1056784                                       2           1                2   
1057013                                       2           ?                7   
1059552                                       2           1                3   
1065726                                       2           7                3   
1066373                                       1           1                2   
1066979                                       2           1                2   
1067444                                       2           1                2   
1070935                                       2           1                1   
...                                         ...         ...              ...   
1350423                                       5           5                7   
1352848                                       5           8                7   
1353092                                       2           1                3   
1354840                                       2           1                3   
1354840                                       3           1                1   
1355260                                       2           1                2   
1365075                                       2           1                1   
1365328                                       2           1                2   
1368267                                       2           1                1   
1368273                                       2           1                1   
1368882                                       2           1                1   
1369821                                       5          10               10   
1371026                                       4          10                5   
1371920                                       2           1                3   
466906                                        2           1                1   
466906                                        2           1                1   
534555                                        2           1                1   
536708                                        2           1                1   
566346                                        2           1                2   
603148                                        2           1                1   
654546                                        2           1                1   
654546                                        2           1                1   
695091                                        4           5                4   
714039                                        2           1                1   
763235                                        2           1                2   
776715                                        3           2                1   
841769                                        2           1                1   
888820                                        7           3                8   
897471                                        3           4               10   
897471                                        4           5               10   

                    Normal Nucleoli  Mitoses  Class  
Sample code number                                   
1000025                           1        1      2  
1002945                           2        1      2  
1015425                           1        1      2  
1016277                           7        1      2  
1017023                           1        1      2  
1017122                           7        1      4  
1018099                           1        1      2  
1018561                           1        1      2  
1033078                           1        5      2  
1033078                           1        1      2  
1035283                           1        1      2  
1036172                           1        1      2  
1041801                           4        1      4  
1043999                           1        1      2  
1044572                           5        4      4  
1047630                           3        1      4  
1048672                           1        1      2  
1049815                           1        1      2  
1050670                           1        2      4  
1050718                           1        1      2  
1054590                           4        4      4  
1054593                          10        1      4  
1056784                           1        1      2  
1057013                           3        1      4  
1059552                           1        1      2  
1065726                           6        1      4  
1066373                           1        1      2  
1066979                           1        1      2  
1067444                           1        1      2  
1070935                           1        1      2  
...                             ...      ...    ...  
1350423                          10        1      4  
1352848                           4        1      4  
1353092                           1        1      2  
1354840                           1        1      2  
1354840                           1        1      2  
1355260                           1        1      2  
1365075                           1        1      2  
1365328                           1        1      2  
1368267                           1        1      2  
1368273                           1        1      2  
1368882                           1        1      2  
1369821                          10        7      4  
1371026                           6        3      4  
1371920                           2        1      2  
466906                            1        1      2  
466906                            1        1      2  
534555                            1        1      2  
536708                            1        1      2  
566346                            3        1      2  
603148                            1        1      2  
654546                            1        8      2  
654546                            1        1      2  
695091                            4        1      4  
714039                            1        1      2  
763235                            1        2      2  
776715                            1        1      2  
841769                            1        1      2  
888820                           10        2      4  
897471                            6        1      4  
897471                            4        1      4  

[699 rows x 10 columns]
>>> features = pd.DataFrame([data1['Clump Thickness'],data1['Uniformity of Cell Size'],data1['Uniformity of Cell Shape'],data1['Marginal Adhesion'],data1['Single Epithelial Cell Size'],data1['Bare Nuclei'],data1['Bland Chromatin'],data1['Normal Nucleoli'],data1['Mitoses']])
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    features = pd.DataFrame([data1['Clump Thickness'],data1['Uniformity of Cell Size'],data1['Uniformity of Cell Shape'],data1['Marginal Adhesion'],data1['Single Epithelial Cell Size'],data1['Bare Nuclei'],data1['Bland Chromatin'],data1['Normal Nucleoli'],data1['Mitoses']])
  File "/usr/local/lib/python3.5/dist-packages/pandas/core/frame.py", line 369, in __init__
    arrays, columns = _to_arrays(data, columns, dtype=dtype)
  File "/usr/local/lib/python3.5/dist-packages/pandas/core/frame.py", line 6291, in _to_arrays
    dtype=dtype)
  File "/usr/local/lib/python3.5/dist-packages/pandas/core/frame.py", line 6383, in _list_of_series_to_arrays
    indexer = indexer_cache[id(index)] = index.get_indexer(columns)
  File "/usr/local/lib/python3.5/dist-packages/pandas/core/indexes/base.py", line 2687, in get_indexer
    raise InvalidIndexError('Reindexing only valid with uniquely'
pandas.core.indexes.base.InvalidIndexError: Reindexing only valid with uniquely valued Index objects
>>> features = pd.DataFrame(data1['Clump Thickness'],data1['Uniformity of Cell Size'],data1['Uniformity of Cell Shape'],data1['Marginal Adhesion'],data1['Single Epithelial Cell Size'],data1['Bare Nuclei'],data1['Bland Chromatin'],data1['Normal Nucleoli'],data1['Mitoses'])
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    features = pd.DataFrame(data1['Clump Thickness'],data1['Uniformity of Cell Size'],data1['Uniformity of Cell Shape'],data1['Marginal Adhesion'],data1['Single Epithelial Cell Size'],data1['Bare Nuclei'],data1['Bland Chromatin'],data1['Normal Nucleoli'],data1['Mitoses'])
TypeError: __init__() takes from 1 to 6 positional arguments but 10 were given
>>> x = data1.drop(['Class'])
>>> y = data1['Class']
>>> from sklearn.neighbors import KNNeighboursClassifire
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    from sklearn.neighbors import KNNeighboursClassifire
ImportError: cannot import name 'KNNeighboursClassifire'
>>> from sklearn.neighbors import KNeighborsClassifier
>>> from sklearn.cross_validation import train_test_split

Warning (from warnings module):
  File "/usr/local/lib/python3.5/dist-packages/sklearn/cross_validation.py", line 41
    "This module will be removed in 0.20.", DeprecationWarning)
DeprecationWarning: This module was deprecated in version 0.18 in favor of the model_selection module into which all the refactored classes and functions are moved. Also note that the interface of the new CV iterators are different from that of this module. This module will be removed in 0.20.
>>> from sklearn import train_test_split
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    from sklearn import train_test_split
ImportError: cannot import name 'train_test_split'
>>> from sklearn import cross_validation
>>> x_train,x_test,y_train,y_test = cross_validation.train_test_split(x,y,train_size=0.75)
>>> knn = KNeighborsClassifier()
>>> knn.fit(x_train,y_train)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    knn.fit(x_train,y_train)
  File "/usr/local/lib/python3.5/dist-packages/sklearn/neighbors/base.py", line 765, in fit
    X, y = check_X_y(X, y, "csr", multi_output=True)
  File "/usr/local/lib/python3.5/dist-packages/sklearn/utils/validation.py", line 573, in check_X_y
    ensure_min_features, warn_on_dtype, estimator)
  File "/usr/local/lib/python3.5/dist-packages/sklearn/utils/validation.py", line 448, in check_array
    array = array.astype(np.float64)
ValueError: could not convert string to float: '?'
>>> x.replace('?',-9999,inplace=True)
>>> 
>>> x_train,x_test,y_train,y_test = cross_validation.train_test_split(x,y,train_size=0.75)
SyntaxError: invalid syntax
>>> x_train,x_test,y_train,y_test = cross_validation.train_test_split(x,y,train_size=0.75)
>>> knn.fit(x_train,y_train)
KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
           metric_params=None, n_jobs=1, n_neighbors=5, p=2,
           weights='uniform')
>>> knn.score(x_test,y_test)
0.9885714285714285
>>> from sklearn import *

Warning (from warnings module):
  File "/usr/local/lib/python3.5/dist-packages/sklearn/grid_search.py", line 42
    DeprecationWarning)
DeprecationWarning: This module was deprecated in version 0.18 in favor of the model_selection module into which all the refactored classes and functions are moved. This module will be removed in 0.20.

Warning (from warnings module):
  File "/usr/local/lib/python3.5/dist-packages/sklearn/learning_curve.py", line 22
    DeprecationWarning)
DeprecationWarning: This module was deprecated in version 0.18 in favor of the model_selection module into which all the functions are moved. This module will be removed in 0.20
>>> from sklearn.tree import *
>>> clf = DecisionTreeClassifier()
>>> clf.fit(x_train,y_train)
DecisionTreeClassifier(class_weight=None, criterion='gini', max_depth=None,
            max_features=None, max_leaf_nodes=None,
            min_impurity_decrease=0.0, min_impurity_split=None,
            min_samples_leaf=1, min_samples_split=2,
            min_weight_fraction_leaf=0.0, presort=False, random_state=None,
            splitter='best')
>>> clf.score(x_test,y_test)
1.0
>>> from sklearn.linear_model import *
>>> clf2 = LogisticRegression()
>>> clf2.fit(x_train,y_train)
LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
          intercept_scaling=1, max_iter=100, multi_class='ovr', n_jobs=1,
          penalty='l2', random_state=None, solver='liblinear', tol=0.0001,
          verbose=0, warm_start=False)
>>> clf2.score(x_test,y_test)
0.9942857142857143
>>> 
