import pickle
def save_pickle_file(boy,girl,count):
    file_name_boy = 'boy_' + str(count) + '.txt'
    file_name_girl = 'girl_' + str(count) + '.txt'
 
    boy_pickle_file = open(file_name_boy,'wb')
    girl_pickle_file = open(file_name_girl,'wb')
 
    pickle.dump(boy,boy_pickle_file)
    pickle.dump(girl,girl_pickle_file)
 
    boy_pickle_file.close()
    girl_pickle_file.close()
 
def split_file(file_name):
    f = open(file_name)
    boy = []
    girl = []
    count = 1
 
    for each_line in f:
        if each_line[:6] != '======':
            (role,line_spoken) = each_line.split(':',1)
            if role == '小甲鱼':
                boy.append(line_spoken)
            elif role == '小客服':
                girl.append(line_spoken)
        else:
            save_pickle_file(boy,girl,count)
            count += 1
            boy = []
            girl = []
 
    save_pickle_file(boy,girl,count)
 
    f.close()
 
split_file('33.txt')