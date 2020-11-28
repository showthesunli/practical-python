def solution(data, n): 
    # Your code here
    meta_dic = count_key_num(data)
    indexs = index_to_del(meta_dic,n)
    new_data = []
    for i in data: 
        if i not in indexs:
            new_data.append(i)
    return new_data

def index_to_del(meta_dic,n):
    indexs= []
    for k,v in meta_dic.items():
        if v > n:
            indexs.append(k)
    return indexs

def count_key_num(data):
    meta_dic = {}
    for key in data:
        if key in meta_dic:
            meta_dic[key] = meta_dic[key]+1
        elif key not in meta_dic:
            meta_dic[key] = 1
    return meta_dic

print(solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 1))
print(solution({1, 2, 3}, 0))

        