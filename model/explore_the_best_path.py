import numpy as np

# 모든 경로 찾기
def find_all_routes(G, start, target, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path.append(start)

    if start == target:
        yield path.copy()
    else:
        for neighbor in G.neighbors(start):
            if neighbor not in visited:
                yield from find_all_routes(G, neighbor, target, visited, path)

    path.pop()
    visited.remove(start)

# 최적 경로 탐색 함수
def find_optimal_routes(G, stations, min_threshold, max_threshold, step):
    optimal_routes = []
    max_stops = 0
    explored_routes = set()  # 탐색된 경로를 저장할 집합

    # 여러 배수 값을 탐색
    for threshold in np.arange(min_threshold, max_threshold + step, step):
        for station in stations.keys():
            if station != "전라북도 무주군":  # 목적지가 아니면
                routes = list(find_all_routes(G, station, "전라북도 무주군"))

                for route in routes:
                    valid_route = True
                    total_distance = 0
                    total_time = 0
                    total_weight = 0  # 가중치 누적

                    # 각 경로의 모든 구간에 대해 개별적으로 검증
                    for i in range(len(route) - 1):
                        current_station = route[i]

                        # 현재 노드에서 무주군으로 바로 이동할 때의 거리와 시간
                        if "전라북도 무주군" in G[current_station]:  # 직접 경로가 있는 경우에만
                            direct_distance = G[current_station]["전라북도 무주군"]['distance']
                            direct_time = G[current_station]["전라북도 무주군"]['time']

                            # 경로의 나머지 정류장을 포함하여 검증
                            cumulative_distance = 0
                            cumulative_time = 0

                            for j in range(i, len(route) - 1):
                                cumulative_distance += G[route[j]][route[j + 1]]['distance']
                                cumulative_time += G[route[j]][route[j + 1]]['time']

                                # 각 정류장에서 무주군으로의 직행 거리/시간과 누적 거리/시간을 threshold 기준으로 검증
                                if cumulative_distance > direct_distance * threshold or cumulative_time > direct_time * threshold:
                                    valid_route = False
                                    break
                                
                            if not valid_route:
                                break  # 이 경로는 유효하지 않으므로 종료
                            
                        # 현재 구간의 거리와 시간을 누적
                        total_distance += G[route[i]][route[i + 1]]['distance']
                        total_time += G[route[i]][route[i + 1]]['time']

                        # 가중치 누적 (출발지 제외)
                        if i > 0:
                            total_weight += stations[current_station]

                    # 모든 구간을 통과한 유효 경로만 선택
                    if valid_route:
                        # 경로를 집합에 저장할 수 있는 형태로 변환 (정렬하여 순서 상관없이 비교하기 위함)
                        route_tuple = tuple(route)

                        # 만약 해당 경로가 이전 배수에서 이미 탐색되었다면 제외
                        if route_tuple not in explored_routes:
                            explored_routes.add(route_tuple)  # 새로운 경로로 저장

                            # 최대 정거장 수 확인
                            if len(route) > max_stops:
                                max_stops = len(route)
                                optimal_routes = [(route, total_distance, total_time, total_weight, threshold)]
                            elif len(route) == max_stops:
                                optimal_routes.append((route, total_distance, total_time, total_weight, threshold))

    return optimal_routes
