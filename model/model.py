import networkx as nx
import sys, os
 
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from func.node_to_node_information import get_coordinates, get_path_info, naver_request, kakao_request
from func.weight_by_region import get_weights
from model.explore_the_best_path import find_optimal_routes
from func.print_path import print_optimal_routes

import json

with open('config.json', 'r', encoding='utf-8') as f:
    locations = json.load(f)

# 경유지와 가중치 사용하기
daejun = locations['daejun']['nodes']
daejun_weights = locations['daejun']['weights']
jeonbuk = locations['jeonbuk']['nodes']
jeonbuk_weights = locations['jeonbuk']['weights']



def explore_the_best_shuttle_bus_path(name):
    if name == "대전":
        nodes = daejun
        weights = daejun_weights
    elif name == "전북":
        nodes = jeonbuk
        weights = jeonbuk_weights
    else:
        raise ValueError("지원하지 않는 지역입니다.")
    
    # 1. 위경도 좌표 기반으로 경유지 간 이동거리, 이동시간 테이블 만듦

    # 경유지 위경도 좌표 
    coordinates = get_coordinates(nodes) 

    # 네이버 api
    # n_distance_table, n_duration_table = get_path_info(coordinates, naver_request)
    # n_duration_min_table = [[round(value / 3600, 2) for value in row] for row in n_duration_table]

    # 카카오 api
    k_distance_table, k_duration_table = get_path_info(coordinates, kakao_request)
    k_duration_min_table = [[round(value / 60, 2) for value in row] for row in k_duration_table]


    distance_table = k_distance_table
    duration_table = k_duration_min_table

    # 2. 정거장 후보지와 가중치
    stations = get_weights(nodes, weights)

    # 3. 탐색
    # 그래프 생성
    G = nx.DiGraph()

    # 그래프에 엣지 추가
    for i, from_station in enumerate(stations.keys()):
        for j, to_station in enumerate(stations.keys()):
            if i != j:
                G.add_edge(from_station, to_station, 
                        distance=distance_table[i][j], 
                        time=duration_table[i][j])
                
    # 탐색 범위 설정 (예: 1.1부터 1.5까지 0.1 간격으로 탐색)
    min_factor = 1.1
    max_factor = 1.5
    step = 0.01

    # 최적 경로 탐색 실행
    optimal_routes = find_optimal_routes(G, stations, min_factor, max_factor, step)

    # 결과 출력
    print_optimal_routes(optimal_routes, name)