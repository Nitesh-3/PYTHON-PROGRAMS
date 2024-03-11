populatiom=80000

t_m=52/100*80000
t_w=48/100*80000

t_l=48/100*80000
t_l_m=35/100*80000
t_l_w = t_l - t_l_m

t_i_m = t_m - t_l_m
t_i_w = t_w - t_l_w

print("The total number of illiterate men = ",t_i_m)
print("The total number of illiterate women = ",t_i_w)
