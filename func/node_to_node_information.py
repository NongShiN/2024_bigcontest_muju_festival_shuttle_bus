import pandas as pd
import yaml
import requests
import json

import sys, os
 
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

# 'data/raw_data' 경로 설정
with open('config.json', 'r', encoding='utf-8') as f:
    paths = json.load(f)

root_dir = paths['root_dir']
address = pd.read_csv(os.path.join(root_dir, "address_with_lon_lat_final.csv"))  # 행정동코드 + 위도경도 (행정동코드,시도명,시군구명,읍면동명,동리명,위도,경도)
address['시도 시군구'] = address['시도명'].fillna('') + ' ' + address['시군구명'].fillna('')
address['시도 시군구'] = address['시도 시군구'].str.strip() # 양쪽 값이 모두 null인 경우 빈 문자열 처리

# 시도시군구명으로 위경도 좌표를 반환하는 함수
def get_coordinates(lst):
    coordinates = []
    for name in lst:
        try:
            # '시도 시군구'로 '위도', '경도' 가져옴
            target = address[address['시도 시군구'] == name][['위도','경도']].iloc[0]
            x, y = target.iloc[0], target.iloc[1]
            coordinates.append((x,y))
        except IndexError:
            # 해당 '시도 시군구'에 대한 데이터가 없는 경우
            print(f"{name} 지역의 위도, 경도 정보가 없습니다.")
    return coordinates



# config.yaml 파일에서 키값 가져오기
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

# naver_api_id와 naver_api_key, kakao_api_key가 각각 존재하는 경우에만 할당
naver_api_id = config.get('naver api', {}).get('id') if 'naver api' in config and 'id' in config['naver api'] else None
naver_api_key = config.get('naver api', {}).get('key') if 'naver api' in config and 'key' in config['naver api'] else None
kakao_api_key = config.get('kakao api', {}).get('key') if 'kakao api' in config and 'key' in config['kakao api'] else None


# 네이버 api 요청 함수
def naver_request(start, goal):
    # 요청
    url = 'https://naveropenapi.apigw.ntruss.com/map-direction/v1/driving'
    params = {
        'goal': f'{goal[1]},{goal[0]}',
        'start': f'{start[1]},{start[0]}',
    }
    headers = {
        'x-ncp-apigw-api-key-id': naver_api_id,
        'x-ncp-apigw-api-key': naver_api_key
    }
    response = requests.get(url, headers=headers, params=params)

    # 응답
    data = response.json()
    if data['code'] == 0:
        if data['route']['traoptimal']:
            summary = data['route']['traoptimal'][0]['summary']
            distance = summary['distance']
            duration = summary['duration']
            return distance, duration
        else:
            print("응답 에러: 'traoptimal' 데이터가 없습니다.")
            return -1, -1
    else:
        print("요청 실패: ", data['message'])
        return -1, -1

# 카카오 api 요청 함수
def kakao_request(start, goal):
    # 요청
    url = 'https://apis-navi.kakaomobility.com/v1/directions'
    params = {
        'origin': f'{start[1]},{start[0]}',
        'destination': f'{goal[1]},{goal[0]}',
        'alternatives': True,
    }
    headers = {
        'Authorization': f'KakaoAK {kakao_api_key}'
    }
    response = requests.get(url, headers=headers, params=params)

    # 응답
    if response.status_code == 200:
        data = response.json()
        if data['routes']:
            summary = data['routes'][0]['summary']
            distance = summary.get('distance')
            duration = summary.get('duration')
            return distance, duration
        else:
            print("응답 에러: 'routes' 데이터가 없습니다.")
            return -1, -1
    else:
        print("요청 실패")
        return -1, -1
    
# 노드 간 이동시간, 이동거리 테이블 반환하는 함수
def get_path_info(coordinates, request_func):
    n = len(coordinates)
    distance_table = [[0] * n for _ in range(n)]
    duration_table = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if j > i:
                start = coordinates[i]
                goal = coordinates[j]
                distance, duration = request_func(start, goal)
                distance_table[i][j], distance_table[j][i] = distance, distance
                duration_table[i][j], duration_table[j][i] = duration, duration

    return distance_table, duration_table