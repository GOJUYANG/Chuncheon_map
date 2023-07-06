import folium
from geopy.distance import geodesic

# 마커들의 위치 리스트
locations = [
    (37.5635, 126.9920),  # 마커 1
    (37.5710, 126.9919),  # 마커 2
    (37.5687, 126.9857),  # 마커 3
    (37.5672, 126.9776),  # 마커 4
    (37.5691, 126.9784)   # 마커 5
]

# 중앙 위도와 경도 계산
center_latitude = sum(coord[0] for coord in locations) / len(locations)
center_longitude = sum(coord[1] for coord in locations) / len(locations)

# 반경 설정 (단위: km)
radius = 5

# 중심 위치 설정
center_location = (center_latitude, center_longitude)

# Folium 지도 생성
m = folium.Map(location=center_location, zoom_start=13)

# 반경 내의 마커 표시를 위한 함수
def add_marker_within_radius(point, center, radius):
    print(point)
    distance = geodesic(center, point).km
    if distance <= radius:
        folium.Marker(location=point).add_to(m)

# 반경 내의 마커 표시
for location in locations:
    add_marker_within_radius(location, center_location, radius)

# 반경 표시를 위한 Circle 추가
folium.Circle(center_location, radius * 1000, color='blue', fill=False).add_to(m)

# Folium 지도 출력
m.show_in_browser()