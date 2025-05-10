# Дан взвешенный граф.
# Необходимо ответить на следующие вопросы:
# 
# 1. Найти длину всех наикротчайших маршрутов из 'Home' в любую точку на графе? (Просто применить алгоритм Дейкстры)
# 2. Найту как выглядит самый кротчайший маршрут из 'Home' в 'Theater' (вывести последовательность прохождения вершин)?
# Подсказка:
# Удобно хранить значения о пройденном маршруте в виде словаря, где ключ - это текущая вершина, а значение - вершина, из которой мы попали в текущую
# Потом в конце нужно будет просто пройтись по такому словарю от финиша к старту и развернуть его.
#
# Входные данные:
# city_map = {
#     'Home': {'Park': 2, 'School': 5, 'Mail': 10},
#     'Park': {'Home': 2, 'Museum': 4, 'Cafe': 3},
#     'School': {'Home': 5, 'Library': 6, 'Mail': 2},
#     'Mail': {'Home': 10, 'School': 2, 'Hospital': 3},
#     'Library': {'School': 6, 'Hospital': 1},
#     'Hospital': {'Library': 1, 'Mail': 3, 'Office': 4},
#     'Cafe': {'Park': 3, 'Theater': 8, 'Office': 7},
#     'Museum': {'Park': 4, 'Shop': 5},
#     'Shop': {'Museum': 5, 'Theater': 1},
#     'Theater': {'Shop': 1, 'Cafe': 8},
#     'Office': {'Cafe': 7, 'Hospital': 4}
# }
# 

city_map = {
    'Home': {'Park': 2, 'School': 5, 'Mail': 10},
    'Park': {'Home': 2, 'Museum': 4, 'Cafe': 3},
    'School': {'Home': 5, 'Library': 6, 'Mail': 2},
    'Mail': {'Home': 10, 'School': 2, 'Hospital': 3},
    'Library': {'School': 6, 'Hospital': 1},
    'Hospital': {'Library': 1, 'Mail': 3, 'Office': 4},
    'Cafe': {'Park': 3, 'Theater': 8, 'Office': 7},
    'Museum': {'Park': 4, 'Shop': 5},
    'Shop': {'Museum': 5, 'Theater': 1},
    'Theater': {'Shop': 1, 'Cafe': 8},
    'Office': {'Cafe': 7, 'Hospital': 4}
}
dist={i:float("inf") for i in city_map}
visited={i: False for i in city_map}
dist["Home"]=0
last={}
while True:
    city=-1
    min_dist=float("inf")
    for i in city_map:
        if not visited[i] and dist[i]<min_dist:
            city=i
            min_dist=dist[i]
    if city==-1:
        break
    visited[city]=True
    for i in city_map[city]:
        if not visited[i]:
            NewDist=dist[city]+city_map[city][i]
            if NewDist < dist[i]:
                dist[i]=NewDist
                last[i]=city
for i in dist:
    print(str(i)+': '+ str(dist[i]))
path=[]
now="Theater"
while now!="Home":
    path.append(now)
    now=last[now]
path.append("Home")
path.reverse()
