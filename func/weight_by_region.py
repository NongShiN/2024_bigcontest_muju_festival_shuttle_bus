import pandas as pd
import numpy as np
import sys, os
import json
 
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from dataloader.dataloader import load_od, load_stay

# 'data/raw_data' 경로 설정
with open('config.json', 'r', encoding='utf-8') as f:
    paths = json.load(f)

root_dir = paths['root_dir']
address = pd.read_csv(os.path.join(root_dir, "address_with_lon_lat_final.csv"))  # 행정동코드 + 위도경도 (행정동코드,시도명,시군구명,읍면동명,동리명,위도,경도)
address['시도 시군구'] = address['시도명'].fillna('') + ' ' + address['시군구명'].fillna('')
address['시도 시군구'] = address['시도 시군구'].str.strip() # 양쪽 값이 모두 null인 경우 빈 문자열 처리


####
df_od = load_od()
df_stay = load_stay()

# 지역별 전체 거주민 수
df_stay_all = df_stay.groupby(['hdong_cd', 'date'])['stay_cnts'].sum().reset_index()  # 날짜별 거주인구 합산
avg_stay_cnts_all = round(df_stay_all.groupby('hdong_cd')['stay_cnts'].mean().reset_index(), 0)  # 하루 평균 거주인구

# 지역별 20대,50대,60대 거주민 수
df_stay_age = df_stay[df_stay['age'].isin([2,5,6])]  # 날짜별 20대 거주인구
avg_stay_cnts_age = round(df_stay_age.groupby(['hdong_cd'])['stay_cnts'].mean().reset_index(), 0)  # 하루 평균 20대 거주인구

# 지역별 무주축제 방문객 인원수
df_od_group = df_od.groupby(['origin_hdong_cd', 'date', 'age'])['od_cnts'].sum().reset_index()
df_od_all = df_od_group.groupby(['origin_hdong_cd', 'date'])['od_cnts'].sum().reset_index()  # 날짜별 방문객수 합산
sum_od_cnts_all = round(df_od_all.groupby(['origin_hdong_cd'])['od_cnts'].sum().reset_index(), 0)  # 해당 지역에서 온 전체 방문객수

# 지역별 20대,50대,60대 무주축제방문객 수
df_od_age = df_od_group[df_od_group['age'].isin([2,5,6])]
sum_od_cnts_age = round(df_od_age.groupby('origin_hdong_cd')['od_cnts'].sum().reset_index(), 0)


# 각 지역 거주인원
def get_residents_num(lst):
    residents_num = []
    residents_num_256 = []
    for name in lst:
        #print("지역명:", name)
        codes = address[address['시도 시군구'] == name]['행정동코드'].unique().tolist()
        #print("관련 행정동코드: ", codes)
        # 지역 내 행정동코드들의 거주인원 합산
        cnt_all = 0
        cnt_256 = 0
        for code in codes:
            tmp_for_all = avg_stay_cnts_all[avg_stay_cnts_all['hdong_cd']==code]
            if not tmp_for_all.empty:
                cnt_all += tmp_for_all['stay_cnts'].iloc[0]
            tmp_for_256 = avg_stay_cnts_age[avg_stay_cnts_age['hdong_cd']==code]
            if not tmp_for_256.empty:
                cnt_256 += tmp_for_256['stay_cnts'].iloc[0]
        residents_num.append(int(cnt_all))
        residents_num_256.append(int(cnt_256))
        #print("총 거주인원:", cnt_all, ",  20/50/60대 거주인원:", cnt_256, "\n")
    return residents_num, residents_num_256

# 각 지역 방문객
def get_visitors_num(lst):
    visitors_num = []
    visitors_num_256 = []
    for name in lst:
        #print("지역명:", name)
        codes = address[address['시도 시군구'] == name]['행정동코드'].unique().tolist()
        #print("관련 행정동코드: ", codes)
        # 지역 내 행정동코드들의 방문객 합산
        cnt_all = 0
        cnt_256 = 0
        for code in codes:
            tmp_for_all = sum_od_cnts_all[sum_od_cnts_all['origin_hdong_cd']==code]
            if not tmp_for_all.empty:
                cnt_all += tmp_for_all['od_cnts'].iloc[0]
            tmp_for_256 = sum_od_cnts_age[sum_od_cnts_age['origin_hdong_cd']==code]
            if not tmp_for_256.empty:
                cnt_256 += tmp_for_256['od_cnts'].iloc[0]
        visitors_num.append(int(cnt_all))
        visitors_num_256.append(int(cnt_256))
        #print("총 방문객 수:", cnt_all, ",  20/50/60대 방문객 수:", cnt_256, "\n")
    return visitors_num, visitors_num_256

# 지역별 20/50/60대 방문율
def get_proportion(a, b, n):
    lst = []
    for i in range(n):
        lst.append(a[i] / b[i])
    return lst


def softmax(weights):
    e = np.exp(weights - np.max(weights))  # 오버플로 방지를 위해 최대값을 빼줌
    return e / e.sum()

def get_weights(nodes, weights):    
    #residents_num, residents_num_256 = get_residents_num(nodes)
    visitors_num, visitors_num_256 = get_visitors_num(nodes)
    # 방식1: 해당 지역의 2/5/60대 거주민 중 축제방문객 비율. (2/5/60대 축제 관심도가 높은 곳을 우선)
    # weight_age = get_proportion(visitors_num_256, residents_num_256, len(nodes))
    # 방식2: 해당 지역의 전체 축제방문객 중 2/5/60대 비율. ()
    weight_age = get_proportion(visitors_num_256, visitors_num, len(nodes))
    # 방식3: 해당 지역의 거주민 중 2/5/60대 거주민 비율. (단순히 2/5/60대가 많은 곳을 우선)
    # weight_age = get_proportion(residents_num_256, residents_num, len(nodes))

    for i, w in enumerate(weight_age):
        weights[i] += w

    softmax_weights = softmax(weights)
    
    stations = {nodes: weight for nodes, weight in zip(nodes, softmax_weights)}
    stations['전라북도 무주군'] = 0 # 무주군은 목적지이므로 가중치 0 으로 설정  
    
    #print("정류장 가중치")
    #print(stations)

    return stations