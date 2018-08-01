import pymysql, json

connection = pymysql.connect(host='47.104.14.235', user='am', password='1234', db='sql_learn', charset='utf8mb4', port=3306, cursorclass=pymysql.cursors.DictCursor)

try:
  sql = "insert into sys_region (region_id, region_name, region_parent_id, region_level) values (%s, %s, %s, %s)"
  with open('./area.json', 'rb') as f :
    arealist = json.load(f)
    for key, value in arealist.items() :
      '''
      with connection.cursor() as cursor:
        cursor.execute(sql, (key, value['name'], '-1', 1))
      '''
      if 'child' in value and  type(value['child']) != list:
        for city_id, city_value in value['child'].items() :
          '''
          with connection.cursor() as cursor_city:
            cursor_city.execute(sql, (city_id, city_value['name'], key, 2))
          '''
          if 'child' in city_value and type(city_value['child']) != list :
            for area_id, area_value in city_value['child'].items() :
              with connection.cursor() as cursor_area:
                cursor_area.execute(sql, (area_id, area_value, city_id, 3))
  connection.commit()
finally:
  connection.close()