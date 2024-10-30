import pandas as pd
from tqdm import tqdm
import sys, os
import json
 
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from preprocess.dataload_preprocess import preprocess_od, preprocess_stay

# paths 파일 불러오기
with open('config.json', 'r', encoding='utf-8') as f:
    paths = json.load(f)


# 'data/raw_data' 경로 설정
root_dir = paths['root_dir']
visitor_city = pd.read_csv(os.path.join(root_dir, "city_of_festival_visitors.csv"))  # 무주축제 방문객 top 18 지역들 (시군구명,od_cnts,시도명,행정동코드,위도,경도)
address = pd.read_csv(os.path.join(root_dir, "address_with_lon_lat_final.csv"))  # 행정동코드 + 위도경도 (행정동코드,시도명,시군구명,읍면동명,동리명,위도,경도)
mooju = set(list(address[address['시군구명'] == '무주군']['행정동코드']))  # 무주군 행정동코드
other_city = list(address.merge(visitor_city, on=['시도명', '시군구명'])['행정동코드_x'])  # 다른 지역들 행정동코드 모음

visitor_city['시도 시군구'] = visitor_city['시도명'].fillna('') + ' ' + visitor_city['시군구명'].fillna('')
visitor_city['시도 시군구'] = visitor_city['시도 시군구'].str.strip() # 양쪽 값이 모두 null인 경우 빈 문자열 처리

address['시도 시군구'] = address['시도명'].fillna('') + ' ' + address['시군구명'].fillna('')
address['시도 시군구'] = address['시도 시군구'].str.strip() # 양쪽 값이 모두 null인 경우 빈 문자열 처리

# raw_data 경로 설정
od_dir = paths['od_dir']
stay_dir = paths['stay_dir']


# festival od data load
def load_od():
    df_od = pd.DataFrame()
    for dirpath, dirnames, filenames in os.walk(od_dir):
        for filename in tqdm(filenames, desc="load od data", unit="file"):
            if filename.endswith('.csv'):
                # 파일 이름에서 날짜 추출
                date_str = filename.split('_')[1]
                
                # 날짜가 20230902에서 20230910 사이인 파일만 처리
                if '20230902' <= date_str <= '20230910':
                    # 파일 경로 설정 및 CSV 읽기
                    file_path = os.path.join(dirpath, filename)
                    csv_data = pd.read_csv(file_path)
                    
                    # 전처리
                    filtered_data = preprocess_od(csv_data, mooju)

                    # 날짜에서 월일(MMDD) 부분 추출
                    mmdd_str = date_str[4:]  # 'YYYYMMDD'에서 마지막 네 자리 'MMDD' 추출
                    
                    # 동적으로 변수 생성 (예: df_0902)
                    globals()[f'df_{mmdd_str}'] = filtered_data
                    df_od = pd.concat([df_od, globals()[f'df_{mmdd_str}']])
    return df_od

# festival stay data load
def load_stay():
    df_stay = pd.DataFrame()
    for dirpath, dirnames, filenames in os.walk(stay_dir):
        for filename in tqdm(filenames, desc="load stay data", unit="file"):
            if filename.endswith('.csv'):
                # 파일 이름에서 날짜 추출
                date_str = filename.split('_')[1]
                
                # 날짜가 20230902에서 20230910 사이인 파일만 처리
                if '20230902' <= date_str <= '20230910':
                    # 파일 경로 설정 및 CSV 읽기
                    file_path = os.path.join(dirpath, filename)
                    csv_data = pd.read_csv(file_path)
                    
                    # 전처리
                    filtered_data = preprocess_stay(csv_data)

                    # 날짜에서 월일(MMDD) 부분 추출
                    mmdd_str = date_str[4:]  # 'YYYYMMDD'에서 마지막 네 자리 'MMDD' 추출
                    
                    # 동적으로 변수 생성 (예: df_0902)
                    globals()[f'df_{mmdd_str}'] = filtered_data
                    df_stay = pd.concat([df_stay, globals()[f'df_{mmdd_str}']])
        return df_stay