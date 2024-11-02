@@@ 1. 대문사진 

### 2022 Bigcontest data analysis field

Git-hub repository at:
https://github.com/NongShiN/2024_bigcontest_muju_festival_shuttle_bus

# Table of contents
1. [Introduction](#introduction)

2. [Description of the data set](#section2)
    1. [Initial steps](#sec2p1)
    2. [Visitor analysis](#sec2p2)
    3. [Movement analysis](#sec2p3)

3. [Problem definitions and solutions](#section3)
    1. [Hypothesis setting and cause analysis](#sec3p1)
    2. [Proposition of shuttle buses](#sec3p2)
    3. [Shuttle bus timetable](#sec3p3)
    4. [Shuttle bus route](#sec3p4)
       
4. [Conclusion](#section4)
    1. [Summary](#sec4p1)
    2. [Expectation effectiveness](#sec4p2)

5. [References](#references)

# 1. Introduction <a name="introduction"></a>
- The competition is a 2024 big contest data analysis field, and it is a competition that selects traditional markets or festivals as targets for analysis with data related to population movement provided by SKT.

- We chose **Muju Firefly Festival** and came up with measures to revitalize the festival.

- The Muju Firefly Festival marks the 28th anniversary of this year in Muju, Jeonbuk-do, South Korea which comes with local agricultural product experiences, cultural performances, and environmental education programs focusing on firefly observation.

- We analyzed the current status of the festival and presented problem definitions and solutions accordingly.

#  2. Description of the dataset <a name="section2"></a>
## 2.1 Initial steps <a name="sec2p1"></a>

This is "od_yyyymmdd_1.csv" data (hereinafter, od data), which is OD data between administrative periods from 2023.9.1 to 2023.10.15. 

@@@ 2. od_df 사진 

The other is "stay_yyyymmdd_1.csv" data (hereinafter, stay data), which is the national administrative unit residence population data from 2023.09.01 to 2023.10.15.

@@@ 3. stay_df 사진


## 2.2 Visitor analysis <a name="sec2p2"></a>
### This is the result of analyzing the number of people who visited Muju during the festival by age group.

@@@ 4. 연령별 방문인원 분포 사진

From this summary we can say that:
1. The percentage of visitors under 10s is the highest, followed by those in their 40s and 30s.
2. From this, it can be inferred that a large number of family visitors have visited, accounting for a total of 78%.
3. Among the remaining age groups, the proportion of people in their 20s is the highest, and the proportion of the remaining age groups (10s, 50s, 60s, 70s, and 80s) is less than 5%.

### This is the result of analyzing the number of people who stayed Muju during the festival by age group.

@@@ 5. 연령별 거주인원 분포사진

From this summary we can say that:
1. The percentage of staying people 40s is the highest, followed by those in their 30s, under 10s and 30s.
2. In the od data, few elderly people were observed, but the stay data clearly shows the ratio of those in their 50s to those in their 60s.

### This is the result of distribution of festival visitors' residence.

@@@ 6. 방문객 고향 사진

From this summary we can say that:
1. It can be seen that many visitors to the festival came from Jeonbuk and Chungnam/Daejeon.
2. The average proportion of outsiders in Korea's festivals is 50%. It can be seen that the proportion of outsiders in the Muju Firefly Festival is 88% very high.


## 2.3 Movement analysis <a name="sec2p3"></a>
### 2.3.1 Result of the distribution of travel distance to Muju by age group.

@@@ 7. 연령대별 이동거리 차이 사진

From this summary we can say that:
1. Those under 10s and 30s and 40s visit from various distances, ranging from close to far away.
2. 10s, 20s, 50s, and 60s usually visit at close range.

### 2.3.2 The distribution of transportation used by festival visitors.

@@@ 8. 방문객 이용 교통수단 사진

From this summary we can say that:
- With 39019 cases of car use, most visitors visited the festival by car.

#  3. Problem definitions and solutions <a name="section3"></a>
## 3.1 Hypothesis setting and cause analysis <a name="sec3p1"></a>
### 3.1.1 Hypothesis setting

1.  The means of off-vehicle transportation are poor.
2.  There are restrictions on participation according to accessibility by age group.

### 3.1.2 Cause analysis
#### 3.1.2.1 The results of transportation and time required to travel from major cities to Muju.

Departure City | Travel Route | Time |
------------|---------------|-------|
Seoul           | Seoul Station - KTX - Daejeon Station - City Bus - Daejeon Complex Terminal - Intercity Bus - Muju Public Bus Terminal | 2h 30m |
Jeonju     | Jeonju Express Bus Terminal - Express Bus - Daejeon Complex Terminal - Intercity Bus - Muju Public Bus Terminal | 2h 30m |
Daegu  | Daegu Station - Mugunghwa Train - Yeongdong Station - City Bus - Muju Public Bus Terminal | 2h 40m |
Busan     | Busan Station - SRT - Daejeon Station - City Bus - Daejeon Complex Terminal - Intercity Bus - Muju Public Bus Terminal | 3h |
Gwangju     | Gwangju Bus Terminal - Express Bus - Daejeon Complex Terminal - Intercity Bus - Muju Public Bus Terminal | 3h 20m | 

From this summary we can say that:
- From other cities to Muju festival sites, the travel route is complicated and the travel time is too long.

#### 3.1.2.2 This shows the contents of the festival by time and the last bus time from the festival site to each city

@@@@ 사진9

From this summary we can say that:
1. Bus services are limited to certain areas and time zones.
2. The bus schedule does not match the time of the festival program, so we cannot use it when we return home.

#### 3.1.2.3 There are restrictions on participation in festivals due to differences in accessibility by age groups.
1. In the case of 20s, the vehicle possession is low, so the dependence on public transportation is high, but the participation rate of the festival is low due to the weak public transportation situation to the festival venue.
2. In the case of people in their 50s, the degree of interest in the festival can be confirmed by looking at the distribution of the number of people staying, but participation restrictions are expected due to fatigue caused by long-distance travel.

#### 3.1.2.4 Improvements to the 27th Muju Firefly Festival (last year)
 Rank | Content |
------------|---------------|
1           | Transportation |
2     | The variety of festival food |
3  | Good things to buy / Local specialties |
4     | Event tour information |

From this survey we can say that:
- Many participants can see that they are uncomfortable with the transportation of the festival.


## 3.2 Proposition of shuttle bus <a name="sec3p2"></a>
### The need for a shuttle bus

@@@@ 사진10


## 3.3 Shuttle bus rimetable <a name="sec3p3"></a>
### 3.1.1 To Muju
@@@@ 사진11

Arrival | Sat | Sun | Mon | Tue | Wed | Thu | Fri |
------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|
10 o'clock   |ㅤㅤㅤㅤ|🚌ㅤㅤㅤ|ㅤㅤㅤㅤ|ㅤㅤㅤㅤ|ㅤㅤㅤㅤ|ㅤㅤㅤㅤ|ㅤㅤㅤㅤ|
12 o'clock   |🚌🚌|🚌🚌|🚌|||||
14 o'clock   |🚌🚌|🚌||||||
16 o'clock   |🚌🚌🚌|🚌|||||🚌|
18 o'clock   |🚌🚌🚌|🚌🚌|🚌|🚌|🚌|🚌|🚌🚌|
20 o'clock   |🚌🚌||||||🚌|


### 3.1.2 To Return
@@@@ 사진12

Departure | Sat | Sun | Mon | Tue | Wed | Thu | Fri |
------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|
12 o'clock   ||||||||
14 o'clock   ||🚌||||||
16 o'clock   |ㅤㅤㅤㅤ|ㅤㅤㅤㅤ|ㅤㅤㅤㅤ|ㅤㅤㅤㅤ|ㅤㅤㅤㅤ|ㅤㅤㅤㅤ|ㅤㅤㅤㅤ|   
18 o'clock   |🚌|🚌🚌||||||
20 o'clock   |🚌🚌🚌|🚌🚌🚌|🚌|🚌|🚌|🚌|🚌🚌🚌|
22 o'clock   |🚌🚌|🚌|||||🚌|


## 3.4 Shuttle bus route <a name="sec3p4"></a>
### 3.4.1 Selection of the station
1. Select the city that visits Muju the most during the festival.
```python
map_filtered = pd.DataFrame()
for region in festival_df_grouped_sido['시도명']:
    # Calculate the sum of 'od_cnts' by 'Region' and sort by 'od_cnts'
    region_filtered = festival_df_grouped_2[festival_df_grouped_2['시도명'] == region]
    # Sejong city doesn't have 'City' name
    if region == '세종특별자시치':
        region_grouped = region_filtered.groupby('시도명')['od_cnts'].sum().reset_index()
    else:
        region_grouped = region_filtered.groupby('시군구명')['od_cnts'].sum().reset_index()
    region_grouped['시도명'] = region
    # Sort in descending order based on 'od_cnts'
    region_grouped = region_grouped.sort_values(by='od_cnts', ascending=False)

    map_filtered = pd.concat([map_filtered, region_grouped[region_grouped['od_cnts'] >= 500]])

```
map_filtered:
City | # of Visitors
------------| ------------| 
Deokjin-gu, Jeonju-si, Jeonbuk | ㅤㅤ2834
Seo-gu, Daejeon | ㅤㅤ1813
Wansan-gu, Jeonju-si, Jeonbuk | ㅤㅤ1561
Yuseong-gu, Daejeon | ㅤㅤ1379
ㅤㅤㅤㅤㅤㅤ... | ㅤㅤ...
Iksan-si, Jeonbuk | ㅤㅤ772
Jinan-gun, Jeonbuk | ㅤㅤ704


   2. Give weight considering the number of visitors to the festival in the city.
```json
    "daejun": {
        "nodes": [
            "세종특별자치시",
            "대전광역시 유성구",
            "대전광역시 서구",
            "대전광역시 대덕구",
            "대전광역시 중구",
            "충청남도 금산군",
            "충청북도 영동군",
            "전라북도 무주군"
        ],
        "weights": [1, 2, 2, 1, 1, 1, 2, 0]
    },
    "jeonbuk": {
        "nodes": [
            "전라북도 군산시",
            "전라북도 익산시",
            "전라북도 전주시 완산구",
            "전라북도 전주시 덕진구",
            "전라북도 진안군",
            "전라북도 장수군",
            "전라북도 무주군"
        ],
        "weights": [1, 1, 2, 2, 1, 2, 0]
    }
```
ㅤ
   3. Give weight considering the "percentage of age groups (20, 50, 60s)" that are difficult to travel long distances.
```python
def get_visitors_num(lst):
    address = load_address()
    sum_od_cnts_all, sum_od_cnts_age = number_of_visitors_to_Muju_by_region()
    visitors_num = []
    visitors_num_256 = []

    for name in lst:
        # Get the list of administrative district codes for each specified region
        codes = address[address['시도 시군구'] == name]['행정동코드'].unique().tolist()
        
        # Initialize counters for total visitors and visitors in age groups 20s, 50s, and 60s
        cnt_all = 0
        cnt_256 = 0
        
        # Sum up visitors for each administrative district code in the region
        for code in codes:
            tmp_for_all = sum_od_cnts_all[sum_od_cnts_all['origin_hdong_cd'] == code]
            if not tmp_for_all.empty:
                cnt_all += tmp_for_all['od_cnts'].iloc[0]  # Total visitors from the administrative code
            tmp_for_256 = sum_od_cnts_age[sum_od_cnts_age['origin_hdong_cd'] == code]
            if not tmp_for_256.empty:
                cnt_256 += tmp_for_256['od_cnts'].iloc[0]  # Total visitors from the specific age groups

        visitors_num.append(int(cnt_all))
        visitors_num_256.append(int(cnt_256))
    
    return visitors_num, visitors_num_256
```

```python
def number_of_visitors_to_Muju_by_region():
    df_od = load_od()
    
    # Number of visitors to Muju Festival by region
    df_od_group = df_od.groupby(['origin_hdong_cd', 'date', 'age'])['od_cnts'].sum().reset_index()
    df_od_all = df_od_group.groupby(['origin_hdong_cd', 'date'])['od_cnts'].sum().reset_index()  # Total visitors per day
    sum_od_cnts_all = round(df_od_all.groupby(['origin_hdong_cd'])['od_cnts'].sum().reset_index(), 0)  # Total visitors from each region

    # Number of Muju Festival visitors by region for age groups 20s, 50s, and 60s
    df_od_age = df_od_group[df_od_group['age'].isin([2,5,6])]
    sum_od_cnts_age = round(df_od_age.groupby('origin_hdong_cd')['od_cnts'].sum().reset_index(), 0)

    return sum_od_cnts_all, sum_od_cnts_age
```
### 3.4.2 Linear Programing
@@@@@ 사진 13

### 3.4.3 Flow Chart
@@@@ 사진 14

### 3.4.4 Recommended Route
#### 3.4.4.1 Daejeon Line

@@@ 사진 15

Rank | Travel Route | Distance | Time |
------------|---------------|---------------|---------------|
ㅤ1 | Seo-gu, Daejeon → Daedeok-gu, Daejeon → Jung-gu, Daejeon → Muju-gun, Jeonbuk | 61.58km | 1h 37m |
ㅤ2 | Seo-gu, Daejeon → Yuseong-gu, Daejeon → Jung-gu, Daejeon → Muju-gun, Jeonbuk | 68.50km | 1h 45m |
ㅤ3 | Seo-gu, Daejeon → Yuseong-gun, Daejeon → Geumsan-gun, Chungnam → Muju-gun, Jeonbuk | 83.24km | 1h 39m |
ㅤ4 | Sejong City → Daedeok-gu, Daejeon → Jung-gu, Daejeon → Muju-gun, Jeonbuk | 83.64km | 2h 2m |

#### 3.4.4.2 Jeonbuk Line

@@@ 사진 16

Rank | Travel Route | Distance | Time |
------------|---------------|---------------|---------------|
ㅤ1 | Gunsan-si, Jeonbuk → Iksan-si, Jeonbuk → Jinan-gun, Jeonbuk → Muju-gun, Jeonbuk | 133.84km | 2h 21m |
ㅤ2 | Gunsan-si, Jeonbuk → Deokjin-gu, Jeonju-si, Jeonbuk → Jinan-gun, Jeonbuk → Muju-gun, Jeonbuk | 120.89km | 2h 34m |
ㅤ3 | Gunsan-si, Jeonbuk → Iksan-si, Jeonbuk → Wansan-gu, Jeonju-si, Jeonbuk → Muju-gun, Jeonbuk | 131.27km | 2h 50m |
ㅤ4 | Gunsan-si, Jeonbuk → Iksan-si, Jeonbuk → Jangsu-gun, Jeonbuk → Muju-gun, Jeonbuk | 165.31km | 2h 37m |


# 4. Conclusion <a name="section4"></a>
  

## 4.1 Summary <a name="sec4p1"></a>


### 4.2 Expectation Effectiveness <a name="sec4p2"></a>



## 5. References <a name="references"></a>

**General:**

- [1]  Anaconda Distribution
https://www.anaconda.com/

- [2] Python Software Foundation
https://www.python.org/

- [3] Project Jupyter
https://jupyter.org/

- [4] Sharing Jupyter notebooks
https://nbviewer.jupyter.org/

- [5] seaborn: statistical data visualization
https://seaborn.pydata.org/index.html#

- [6] matplotlib: Python plotting library
https://matplotlib.org/

- [7] The Tips data set from Michael Waskom
https://github.com/mwaskom/seaborn-data/blob/master/tips.csv

- [8] Description of what is contained in the tips set
https://www.kaggle.com/ranjeetjain3/seaborn-tips-data set

- [9] scikit-learn: Machine Learning in Python
https://scikit-learn.org/stable/index.html

- [10] statsmodels: Statistics in Python
https://www.statsmodels.org/stable/index.html

- [11] scipy.stats : Statistics with SciPy
https://docs.scipy.org/doc/scipy/reference/tutorial/stats.html

**Exploratory data analysis:**

- [12] Exploratory Statistical Data Analysis with a Real data set using Pandas
https://towardsdatascience.com/exploratory-statistical-data-analysis-with-a-real-data set-using-pandas-208007798b92

- [13] How to investigate a data set with Python
https://towardsdatascience.com/hitchhikers-guide-to-exploratory-data-analysis-6e8d896d3f7e

- [14] Data analysis with Python
https://medium.com/@onpillow/01-investigate-tmdb-movie-data set-python-data-analysis-project-part-1-data-wrangling-3d2b55ea7714

- [15] Python for Data Analysis: Data Wrangling with Pandas, NumPy, and IPython. 
Wes McKinney. ISBN-13: 978-1491957660 ISBN-10: 1491957662

- [16] Pandas In 10 Minutes || Wes McKinney
https://www.youtube.com/watch?v=1MGCD8SQp3k

- [17] Good description of quartiles on Seaborn plots
https://towardsdatascience.com/analyze-the-data-through-data-visualization-using-seaborn-255e1cd3948e

**Regression:**

- [18] Ordinary Least Squares in statsmodels
https://www.statsmodels.org/dev/examples/notebooks/generated/ols.html

- [19] Generalized Linear Models in scikit-learn
https://scikit-learn.org/stable/modules/linear_model.html#ordinary-least-squares

- [20] How to run Linear regression in Python scikit-Learn
https://bigdata-madesimple.com/how-to-run-linear-regression-in-python-scikit-learn/

- [21] A beginner’s guide to Linear Regression in Python with Scikit-Learn
https://towardsdatascience.com/a-beginners-guide-to-linear-regression-in-python-with-scikit-learn-83a8f7ae2b4f

- [22] Regression Analysis: How Do I Interpret R-squared and Assess the Goodness-of-Fit?
https://blog.minitab.com/blog/adventures-in-statistics-2/regression-analysis-how-do-i-interpret-r-squared-and-assess-the-goodness-of-fit

- [23] Python and R Tips To Learn Data Science: Pearson and Spearman Correlation in Python
https://cmdlinetips.com/2019/08/how-to-compute-pearson-and-spearman-correlation-in-python/

**Classification:**

- [24] K-nearest Neighbors (KNN) Classification Model
https://www.ritchieng.com/machine-learning-k-nearest-neighbors-knn/

- [25] Supervised and Unsupervised Machine Learning Algorithms
https://machinelearningmastery.com/supervised-and-unsupervised-machine-learning-algorithms/

- [26] Cross-Validation
https://www.ritchieng.com/machine-learning-cross-validation/

**References directly relating to Tips:**

- [27] Tips data set in PYTHON MACHINE LEARNING EXAMPLE – LINEAR REGRESSION
https://devarea.com/python-machine-learning-example-linear-regression/#.XbbfgOj7Q2w

- [28] Tips analysis using Seaborn: Visualizing statistical relationships
https://seaborn.pydata.org/tutorial/relational.html#relational-tutorial

- [29] Tips analysis using Seaborn: Plotting with categorical data
https://seaborn.pydata.org/tutorial/categorical.html#categorical-tutorial

- [30] Tips analysis using Seaborn: Visualizing linear relationships
https://seaborn.pydata.org/tutorial/regression.html#regression-tutorial

- [31] Tips analysis using Seaborn: Building structured multi-plot grids
https://seaborn.pydata.org/tutorial/axis_grids.html#grid-tutorial

- [32] STAT 503 Case Study 1: Restaurant Tipping (Author unknown)
https://dicook.public.iastate.edu/stat503/05/cs-tips2.pdf

- [33] Interactive analytics and predictions on Restaurant tips
https://medium.com/@valentinaalto/interactive-analytics-and-predictions-on-restaurant-tips-94f21f537de8

- [34] Seaborn again: Python Data Visualisation using Seaborn 
https://grindsquare.co.za/python-data-visualisation-using-seaborn/

- [35] Excerpt from the Python Data Science Handbook by Jake VanderPlas; Jupyter notebooks are available on GitHub.
https://jakevdp.github.io/PythonDataScienceHandbook/04.14-visualization-with-seaborn.html

- [36] Interactive analytics and predictions on Restaurant tips
https://datasciencechalktalk.com/2019/11/03/interactive-analytics-and-predictions-on-restaurant-tips/

- [37] atlassian.com: .gitignore
https://www.atlassian.com/git/tutorials/saving-changes/gitignore#personal-git-ignore-rules
