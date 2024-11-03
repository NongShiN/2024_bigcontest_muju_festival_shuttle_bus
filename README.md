![1](https://github.com/user-attachments/assets/3f4fed98-7962-4996-93e7-d8b9eb0cc361)
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

- This is "od_yyyymmdd_1.csv" data (hereinafter, od data), which is OD data between administrative periods from 2023.9.1 to 2023.10.15. 

<img src="https://github.com/user-attachments/assets/e44e5ded-101d-41b3-854a-b168218f0764" alt="6" width="1000"/>


- The other is "stay_yyyymmdd_1.csv" data (hereinafter, stay data), which is the national administrative unit residence population data from 2023.09.01 to 2023.10.15.


<img src="https://github.com/user-attachments/assets/252f80c4-fe6f-4f4d-b855-fb3c05861e81" alt="6" width="400"/>


## 2.2 Visitor analysis <a name="sec2p2"></a>
### 2.2.1 Result of analyzing the number of people who visited Muju during the festival by age group.

<img src="https://github.com/user-attachments/assets/e52569e5-3986-4c8a-b5b4-4abb33bd4002" alt="6" width="500"/>


From this summary we can say that:
1. The percentage of visitors under 10s is the highest, followed by those in their 40s and 30s.
2. From this, it can be inferred that a large number of family visitors have visited, accounting for a total of 78%.
3. Among the remaining age groups, the proportion of people in their 20s is the highest, and the proportion of the remaining age groups (10s, 50s, 60s, 70s, and 80s) is less than 5%.

### 2.2.2 Result of analyzing the number of people who stayed Muju during the festival by age group.

<img src="https://github.com/user-attachments/assets/8db12ac8-a353-476e-bc65-42db7a8ffff6" alt="6" width="500"/>


From this summary we can say that:
1. The percentage of staying people 40s is the highest, followed by those in their 30s, under 10s and 30s.
2. In the od data, few elderly people were observed, but the stay data clearly shows the ratio of those in their 50s to those in their 60s.

### 2.2.3 Result of distribution of festival visitors' residence.

<img src="https://github.com/user-attachments/assets/90005650-4b72-47b4-8ba4-67fb707b6548" alt="6" width="600"/>

From this summary we can say that:
1. It can be seen that many visitors to the festival came from Jeonbuk and Chungnam/Daejeon.
2. The average proportion of outsiders in Korea's festivals is 50%. It can be seen that the proportion of outsiders in the Muju Firefly Festival is 88% very high.


## 2.3 Movement analysis <a name="sec2p3"></a>
### 2.3.1 Result of the distribution of travel distance to Muju by age group.

<img src="https://github.com/user-attachments/assets/2462d208-d46b-48e8-b3d2-49a5879d7f4a" alt="6" width="500"/>

From this summary we can say that:
1. Those under 10s and 30s and 40s visit from various distances, ranging from close to far away.
2. 10s, 20s, 50s, and 60s usually visit at close range.

### 2.3.2 The distribution of transportation used by festival visitors.

<img src="https://github.com/user-attachments/assets/95ff40ef-124d-4605-b6a5-0919d49191b5" alt="6" width="500"/>



From this summary we can say that:
- With 39019 cases of car use, most visitors visited the festival by car.

#  3. Problem definitions and solutions <a name="section3"></a>
## 3.1 Hypothesis setting and cause analysis <a name="sec3p1"></a>
### 3.1.1 Hypothesis setting

1.  The means of off-vehicle transportation are poor.
2.  There are restrictions on participation according to accessibility by age group.

### 3.1.2 Cause analysis
#### 3.1.2.1 The results of transportation and time required to travel from major cities to Muju.

Departure | Travel Route | Time |
------------|---------------|-------|
Seoul           | Seoul Station (KTX) → Daejeon Station (City Bus) → Daejeon Complex Terminal (Intercity Bus) → Muju Bus Terminal | 2h 30m |
Jeonju     | Jeonju Express Bus Terminal (Express Bus) → Daejeon Complex Terminal (Intercity Bus) → Muju Bus Terminal | 2h 30m |
Daegu  | Daegu Station (Mugunghwa Train) → Yeongdong Station (City Bus) → Muju Bus Terminal | 2h 40m |
Busan     | Busan Station (SRT) → Daejeon Station (City Bus) → Daejeon Complex Terminal (Intercity Bus) → Muju Bus Terminal | 3h |
Gwangju     | Gwangju Bus Terminal (Express Bus) → Daejeon Complex Terminal (Intercity Bus) → Muju Bus Terminal | 3h 20m | 

From this summary we can say that:
- From other cities to Muju festival sites, the travel route is complicated and the travel time is too long.

#### 3.1.2.2 This shows the contents of the festival by time and the last bus time from the festival site to each city

<img src="https://github.com/user-attachments/assets/0e0b0fe5-369e-47ed-a524-4ccb00366553" alt="6" width="800"/>

From this summary we can say that:
1. Bus services are limited to certain areas and time zones.
2. The bus schedule does not match the time of the festival program, so we cannot use it when we return home.

#### 3.1.2.3 There are restrictions on participation in festivals due to differences in accessibility by age groups.
1. In the case of 20s, the vehicle possession is low, so the dependence on public transportation is high, but the participation rate of the festival is low due to the weak public transportation situation to the festival venue.
2. In the case of people in their 50s, the degree of interest in the festival can be confirmed by looking at the distribution of the number of people staying, but participation restrictions are expected due to fatigue caused by long-distance travel.

#### 3.1.2.4 Improvements to the 27th Muju Firefly Festival (last year)
 Rank | Content |
------------|---------------|
ㅤ1           | Transportation |
ㅤ2     | The variety of festival food |
ㅤ3  | Good things to buy / Local specialties |
ㅤ4     | Event tour information |

From this survey we can say that:
- Many participants can see that they are uncomfortable with the transportation of the festival.


## 3.2 Proposition of shuttle bus <a name="sec3p2"></a>
### The need for a shuttle bus

<img src="https://github.com/user-attachments/assets/65fe38cf-c70a-4f3d-b382-0b4d94a7d783" alt="6" width="800"/>

## 3.3 Shuttle bus rimetable <a name="sec3p3"></a>
### 3.1.1 To Muju

<img src="https://github.com/user-attachments/assets/61cc4717-acba-4088-8a25-ed9ec87164d0" alt="6" width="1000"/>

Arrival | Sat | Sun | Mon | Tue | Wed | Thu | Fri |
------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|
10 o'clock   |ㅤㅤㅤㅤ|🚌ㅤㅤㅤ|ㅤㅤㅤㅤ|ㅤㅤㅤㅤ|ㅤㅤㅤㅤ|ㅤㅤㅤㅤ|ㅤㅤㅤㅤ|
12 o'clock   |🚌🚌|🚌🚌|🚌|||||
14 o'clock   |🚌🚌|🚌||||||
16 o'clock   |🚌🚌🚌|🚌|||||🚌|
18 o'clock   |🚌🚌🚌|🚌🚌|🚌|🚌|🚌|🚌|🚌🚌|
20 o'clock   |🚌🚌||||||🚌|


### 3.1.2 To Return

<img src="https://github.com/user-attachments/assets/2136989f-1ba8-4fb5-9e2d-aa73b94ad058" alt="6" width="1000"/>

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

<img src="https://github.com/user-attachments/assets/bc839c99-8357-4ad6-818d-61001801cd1e" alt="6" width="600"/>

### 3.4.3 Flow Chart

<img src="https://github.com/user-attachments/assets/bee931c6-d9a3-4301-88dd-f6c2de8b52f6" alt="14" width="600"/>

### 3.4.4 Recommended Route
#### 3.4.4.1 Daejeon Line

<img src="https://github.com/user-attachments/assets/b6939615-35cf-4055-8d98-018824cc31a2" alt="15" width="500"/>

Rank | Travel Route | Distance | Time |
------------|---------------|---------------|---------------|
ㅤ1 | Seo-gu, Daejeon → Daedeok-gu, Daejeon → Jung-gu, Daejeon → Muju-gun, Jeonbuk | 61.58km | 1h 37m |
ㅤ2 | Seo-gu, Daejeon → Yuseong-gu, Daejeon → Jung-gu, Daejeon → Muju-gun, Jeonbuk | 68.50km | 1h 45m |
ㅤ3 | Seo-gu, Daejeon → Yuseong-gun, Daejeon → Geumsan-gun, Chungnam → Muju-gun, Jeonbuk | 83.24km | 1h 39m |
ㅤ4 | Sejong City → Daedeok-gu, Daejeon → Jung-gu, Daejeon → Muju-gun, Jeonbuk | 83.64km | 2h 2m |

---------------------------------------------

#### 3.4.4.2 Jeonbuk Line

<img src="https://github.com/user-attachments/assets/9c351b94-87bd-4f06-89de-a621f191e217" alt="6" width="800"/>

Rank | Travel Route | Distance | Time |
------------|---------------|---------------|---------------|
ㅤ1 | Gunsan-si, Jeonbuk → Iksan-si, Jeonbuk → Jinan-gun, Jeonbuk → Muju-gun, Jeonbuk | 133.84km | 2h 21m |
ㅤ2 | Gunsan-si, Jeonbuk → Deokjin-gu, Jeonju-si, Jeonbuk → Jinan-gun, Jeonbuk → Muju-gun, Jeonbuk | 120.89km | 2h 34m |
ㅤ3 | Gunsan-si, Jeonbuk → Iksan-si, Jeonbuk → Wansan-gu, Jeonju-si, Jeonbuk → Muju-gun, Jeonbuk | 131.27km | 2h 50m |
ㅤ4 | Gunsan-si, Jeonbuk → Iksan-si, Jeonbuk → Jangsu-gun, Jeonbuk → Muju-gun, Jeonbuk | 165.31km | 2h 37m |


# 4. Conclusion <a name="section4"></a>
## 4.1 Summary <a name="sec4p1"></a>
#### 4.1.1 Analyze Muju festival and define problem: Lack of access to transportation to festival sites
- A high percentage of outsiders

- Lack of public transport infrastructure

- Targeting for various age groups

- Lack of access to certain age groups

#### 4.1.2 Solution: Propose introduction of shuttle buses connecting major cities during the festival
- Propose a timetable through analysis of visitor data by day and hour

- Propose a route through analysis of visitor data by region

## 4.2 Expectation Effectiveness <a name="sec4p2"></a>
#### 4.2.1 Improve transportation inconvenience
- Improve access to festival sites.
- Alleviate traffic congestion near the festival site.
  
#### 4.2.2 Increase participation rate
- Reduced transportation costs.
- Encourage the participation of various age groups by simplifying travel routes.

#### 4.2.3 Environmental benefits
- Reduce carbon emissions.
- Realize the value of **'green'**, the slogan of Muju Festival

# 5. References <a name="references"></a>

**Paper:**

- [1]  Changsoo Kim, Hyungbin Jang. (2014). A Study on the Relations between Vistor orientation and Consumer spending in the past 3 years Muju Firefly Festival, 18(1), 1-19.

    https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART001866295

- [2] Huiseok Seo, Junghyun Yoon. (2006). A Study on the Success Factors of Regional Festivals -focusing on the Andong maskdance festival, Hampyeong butterfly festival, and Iksan Seodong festival-, 20(4), 207-228.

    https://www.krila.re.kr/download/thesis/563

- [3] Changwoo Jeon, Gunhak Lee. (2017). Optimal Routing of Free Shuttle Bus to Enhance the Travel Convenience for the Elderly: A Case of Gwanak-gu, Seoul, 6(2), 291-304.

     https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002252629

- [4] Eunhak Lee, Seung-young Ko, Dongkyu Kim. (2021). Optimization of Direct Bus Route using Smart Card Data. 85th Conference of the Korea Transportation Association

    https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE10675729

