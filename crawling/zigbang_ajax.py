import requests
import json
import pprint
import geohash2

q = "충정로"
serviceType = "아파트"
url = "https://apis.zigbang.com/v2/search?q={}&serviceType={}".format(q, serviceType)
r = requests.get(url) # json 형태를 반환
result = json.loads(r.text) # dict
# pprint.pprint(result)  # 정렬
if result["success"]:
    lat = result["items"][0]["lat"]
    lng = result["items"][0]["lng"]

# geohash # https://en.wikipedia.org/wiki/Geohash 
geohash = geohash2.encode(lat, lng, precision=5)
# 위에서 구한 geohash 값을 아래의 api 로 호출하고 쿼리(전세 월세 등)를 넘겨주는 주소 입니다.
url = "https://apis.zigbang.com/v2/items?deposit_gteq=0&domain=zigbang&geohash={}&rent_gteq=0&sales_type_in=전세%7C월세&service_type_eq=원룸".format(geohash)
r_items = requests.get(url).json() # json 형태 처리

# items 값은 실제 매물 데이터의 인덱스 값입니다.
items = r_items.get("items")
# pprint.pprint(items)

# 위에서 취한 json 형태의 items 목록을 파이썬 리스트 형태로 저장합니다.
item_ids = []
for item in items:
    item_ids.append(item.get("item_id"))

items = {"item_ids": item_ids[:10]} # 10개만 items_ids 라는 키의 값으로 설정
# post - data = items
results = requests.post('https://apis.zigbang.com/v2/items/list', data=items).json() # json 형태 처리
# pprint.pprint(results)

datas = results.get("items") # 최종 결과 items
for d in datas:
    address = "{}".format(d.get("address1"))
    if d.get("address2") is not None:
        address += " {}".format(d.get("address2"))
    if d.get("address3") is not None:
        address += " {}".format(d.get("address3"))
   
    building_floor = d.get("building_floor")
    floor = d.get("floor")
    thumbnail = d.get("images_thumbnail")
    item_id = d.get("item_id")
    reg_date = d.get("reg_date")
    sales_type = d.get("sales_type")
    service_type = d.get("service_type")
    size_m2 = d.get("size_m2")
    title = d.get("title")
    deposit = d.get("deposit")
    rent = d.get("rent")

    print("*" * 100)
    print("{} [{}]".format(title, item_id))
    print("보증금/월세: {}/{}".format(deposit, rent))
    print("건물층/매물층: {}/{}".format(building_floor, floor))
    print("등록일자: {}".format(reg_date))
    print("서비스형태/매물형태: {}/{}".format(service_type, sales_type))
    print("사이즈: {}".format(size_m2))
