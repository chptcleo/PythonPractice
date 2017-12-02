import os

def get_files(path, file_list1):
    files = os.listdir(path)
    for file in files:
        full_path =  os.path.join(path, file)
        if os.path.isdir(full_path):
            get_files(full_path, file_list1)
        if not os.path.isdir(full_path):
            file_list1.append(file)

def remove(path, file_list1):
    files = os.listdir(path)
    count =0
    for file in files:
        if file_list1.count(file) !=0:
            count = count+1
            print file
            full_path = os.path.join(path, file)
            os.remove(full_path)
        
    print count
    

if __name__ == '__main__':
    path1 = 'E:\Music\car'
    file_list1 = []
    get_files(path1,file_list1)
    print file_list1
    print len(file_list1)
    path2 = 'E://Music/M'
    remove(path2, file_list1)
    
    