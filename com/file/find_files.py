import os


def find_files_by_type(test_dir, test_type):
    for test_file in os.listdir(test_dir):
        tmp_dir = test_dir + '/' + test_file
        if os.path.isdir(tmp_dir):
            find_files_by_type(tmp_dir, test_type)
        else:
            if os.path.splitext(tmp_dir)[1] == '.' + test_type:
                print(tmp_dir[len('/WorkSpace/Eclipse/PythonPractice/com'):])
    

if __name__ == '__main__':
    find_files_by_type('/WorkSpace/Eclipse/PythonPractice/com', 'py')
