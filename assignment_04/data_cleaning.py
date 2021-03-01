with open('census_cost.txt') as census_data_file:
    # 1
    line_list = census_data_file.readlines()
    print('line list:\n',line_list)
    
    # 2
    top2_list = list()
    top2_list.insert(0,line_list.pop(0))
    top2_list.insert(1,line_list.pop(0))
    print('top2_list:\n',top2_list)
       
    # 3
    data_list = line_list
    print('data_list:\n',data_list)
    
    # 4
    year_list = list()
    for i in data_list:
        x=i.split('\t')
        year= x[0].strip('*') #for cleaning the last element '2010*'  
        year_list.append(year) 
    print('year_list:\n',year_list)
    
    # 5
    pop_list = list()
    for i in data_list:
        x = i.split('\t')
        population = x[1].replace(',','')
        pop_list.append(population)
    print('pop_list:\n',pop_list)
    
    # 6
    cost_list = list()
    for i in data_list:
        x = i.split('\t')
        cost = x[2].replace(',','')
        cost = cost.replace('$','')
        if 'Billion' in cost:
            cost = cost.replace(' Billion','')
            cost = str(int((float(cost)*1000000000)))
        cost_list.append(cost)
    print('cost_list:\n',cost_list)
    
    # 7
    avg_list = list()
    for i in data_list:
        x = i.split('\t')
        avg = x[3]
        if '$' in avg:
            avg = avg.replace('$','')
            avg = avg.replace('\n','')
        if 'cents' in avg:
            avg = avg.replace(' cents','')
            avg = str(round(float(avg)*0.01,2)) #1 cents is equal to 0.01 dollar.
        avg_list.append(avg)
    print('avg_list:\n',avg_list)
    
# 8
with open('census_cost.csv','w') as newfile:
    # first 2 lines:
    newfile.writelines(top2_list)
    
    # writing the data
    for i in range(len(data_list)):
        line = f'{year_list[i]}\t{pop_list[i]}\t{cost_list[i]}\t{avg_list[i]}\n'
        newfile.write(line)

# 9
with open('census_cost.csv') as census_file:
    x=census_file.readlines()
    for line in x:
        print(line,end='')