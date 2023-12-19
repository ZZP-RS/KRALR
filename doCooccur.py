import collections

cf_file = 'datasets/last-fm/train.txt'
kg_file = 'datasets/last-fm/kg_final.txt'
save_file = 'datasets/last-fm/kg_final3.txt'

nodes = collections.defaultdict(list)
items = set()
# load cf_data
lines = open(cf_file, 'r').readlines()
for line in lines:
    temp = [int(x) for x in line.split()]
    items.add(temp[1])
lines = open(cf_file, 'r').readlines()
for line in lines:
    temp = [int(x) for x in line.split()]
    if temp[1] not in nodes.keys():
        nodes[temp[1]] = [temp[0]]
    else:
        nodes[temp[1]].append(temp[0])
# load kg_data
h = []
r = []
t = []
lines = open(kg_file, 'r').readlines()
for line in lines:
    temp = [int(x) for x in line.split()]
    assert len(temp) == 3
    h.append(temp[0])
    r.append(temp[1])
    t.append(temp[2])
    if temp[0] in nodes.keys():
        nodes[temp[0]].append(temp[2])
    if temp[2] in nodes.keys():
        nodes[temp[2]].append(temp[0])

assert len(h) == len(r)
assert len(h) == len(t)
n_relations = len(set(r))
n_h_origin = len(h)
print(n_h_origin)
print(n_relations)
item_list = list(nodes.keys())
intersection_num = 0
intersection_num_4 = 0
intersection_num_5 = 0
intersection_num_6 = 0
intersection_num_7 = 0
intersection_num_8 = 0
intersection_num_9 = 0
intersection_num_10 = 0
for i in range(len(item_list)):
    target_set = set(nodes[item_list[i]])
    for j in range(i + 1, len(item_list)):
        object_set = set(nodes[item_list[j]])
        # if len(target_set.intersection(object_set)) > 3:
        #     h.append(item_list[i])
        #     r.append(n_relations)
        #     t.append(item_list[j])
        #     intersection_num += 1
        if len(target_set.intersection(object_set))>4 :
            intersection_num_4 +=1
        if len(target_set.intersection(object_set))>5 :
            intersection_num_5 +=1
        if len(target_set.intersection(object_set)) > 6:
            intersection_num_6 += 1
        if len(target_set.intersection(object_set))>7 :
            intersection_num_7 +=1
        if len(target_set.intersection(object_set))>8:
            intersection_num_8 +=1
        if len(target_set.intersection(object_set))>9 :
            intersection_num_9 +=1
        if len(target_set.intersection(object_set))>10 :
            intersection_num_10 +=1

print(intersection_num_4)
print(intersection_num_5)
print(intersection_num_6)
print(intersection_num_7)
print(intersection_num_8)
print(intersection_num_9)
print(intersection_num_10)

# 2299 15,518
# writer = open(save_file, 'w')
# assert len(h) == len(r)
# assert len(h) == len(t)
# assert len(h) == intersection_num + n_h_origin
# for i in range(len(h)):
#     writer.write('%d %d %d\n' % (h[i], r[i], t[i]))
# writer.close()
