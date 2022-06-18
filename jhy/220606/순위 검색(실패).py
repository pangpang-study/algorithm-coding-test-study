def solution(info, query):
    answer = []
    
    for order in query:
        lang, group, period, food = order.split(" and ")
        food, point = food.split()
        count = 0
        for person in info:
            p_lang, p_group, p_period, p_food, p_point = person.split()
            if lang != '-':
                if lang != p_lang:
                    continue
            if group != '-':
                if group != p_group:
                    continue
            if period != '-':
                if period != p_period:
                    continue
            if food != '-':    
                if food != p_food:
                    continue
            if int(point) <= int(p_point):
                count += 1
        answer.append(count)
    
    return answer