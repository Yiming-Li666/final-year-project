# UTILITIES

## Requirements
* **json**  
> pip3 install json  
* **openpyxl**  
> pip3 install openpyxl  
* **bs4**  
> pip3 install bs4  
* **requests**  
> pip3 install requests  

## html
### grab.py
Used to grab the categories of diseases from websites. Hard coding parameters are in *"../config/config.json"*. Each website is under one main category of disease and all the sub-categories are collected. These data will be saved into xlsx file in certain format. The correctness of processing data can be validated by saved json files.

## lstm
### sentiment_analysis.py
tensorflow==1.13.1
keras==2.2.4
Used to analysis the sympotom in plaintext form.

## Reference
* [Read and write xlsx files](https://blog.csdn.net/liuyingying0418/article/details/101066630?utm_medium=distribute.pc_aggpage_search_result.none-task-blog-2~all~first_rank_v2~rank_v25-3-101066630.nonecase&utm_term=python%20读写xlsx文件)
* [Formal documentation for openpyxl](https://openpyxl.readthedocs.io/en/stable/)
* [Usage for BeautifulSoup in bs4](https://www.cnblogs.com/scios/p/8652760.html)
* [lstm implementation](https://github.com/elliottssu/lstm-sentiment-analysis)