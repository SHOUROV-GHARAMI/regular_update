# a  = [1,2,3,"Number","odd",15,100,201]
# # print(a)
# # a[2] = 540
# # print(a)
# # print(a[-2])
# # print(len(a))
# a.append([1,2,3])
# a.reverse()
# print(a)

t = (513,56,6,79,330,543,543)
# t[0] = 654
print(t)

t_r = tuple(reversed(t))
print(t_r)
t_s = tuple(sorted(t_r)) # tuple print hobe
print(t_s)
t_a = sorted(t_s) # arry print hobe
print(t_a)
t_r_s = tuple(reversed(t_a))
print(t_r_s)