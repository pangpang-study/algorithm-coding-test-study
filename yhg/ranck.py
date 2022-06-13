from bisect import bisect_left
def solution(info, query):
    answer = []
    info_dic = {"java" : {"backend"  : {"junior" : {"chicken" : [],
                                                    "pizza" : []},
                                        "senior" : {"chicken" : [],
                                                    "pizza" : []
                                                    }
                                        },
                          "frontend"  : {"junior" : {"chicken" : [],
                                                    "pizza" : []},
                                        "senior" : {"chicken" : [],
                                                    "pizza" : []}
                                                    }
                                        
                        },
                "cpp" : {"backend"  : {"junior" : {"chicken" : [],
                                                    "pizza" : []},
                                        "senior" : {"chicken" : [],
                                                    "pizza" : []
                                                    }
                                        },
                          "frontend"  : {"junior" : {"chicken" : [],
                                                    "pizza" : []},
                                        "senior" : {"chicken" : [],
                                                    "pizza" : []}
                                                    }
                                        
                        },
                "python" :{"backend"  : {"junior" : {"chicken" : [],
                                                    "pizza" : []},
                                        "senior" : {"chicken" : [],
                                                    "pizza" : []
                                                    }
                                        },
                          "frontend"  : {"junior" : {"chicken" : [],
                                                    "pizza" : []},
                                        "senior" : {"chicken" : [],
                                                    "pizza" : []}
                                                    }
                                        
                        },
               }
    
    for inf in info:
        info_list = list(inf.split())
        
        info_dic[info_list[0]][info_list[1]][info_list[2]][info_list[3]].append(int(info_list[4]))
        
    for que in query:
        q = que.split(" and ")
        now_list = [[],[],[],[]]
        
        now = q[0] 
        if now == "-":
            now_list[0] = ["java" , "cpp" , "python"]
        else:
            now_list[0] = [now]
            
        now = q[1]
        if now  == "-":
            now_list[1]  = ["backend", "frontend"]
        else:
            now_list[1] = [now]
            
        now = q[2]
        if now == "-":
            now_list[2] = ["senior" , "junior"]
        else:
            now_list[2] = [now]
        now = list(q[3].split())
        if now[0] == "-":
            now_list[3] = ["chicken" ,"pizza"]
        else:
            now_list[3] = [now[0]]
        
        count = 0 
        check_list = []
        for lang in now_list[0]:
            for job in now_list[1]:
                for car in now_list[2]:
                    for food in now_list[3]:
                        check_list+=info_dic[lang][job][car][food]
        check_list = sorted(check_list)
        count += len(check_list) - bisect_left(check_list, int(now[1]))
                        
                                
                            
        
        answer.append(count)
                        
        
    return answer



info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]	
qurey = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]	
print(solution(info, qurey))