import sys
import os
import time

headline = ['#','##','###','####','#####','######']
lines_in_file = []

"""����Ŀ¼�б��е�ĳһ��"""
def creat_directory_line(line,headline_mark,i):
    if headline_mark == '#':
        return '<a href="#' + str(i) + '">' + line[2:-1] + "</a>  \n"
    elif headline_mark == '##':
        #&emsp;ΪMarkdown�е�һ�����������ﲻֱ���ÿո���Ϊ��������Ϊ����ո�һ����ֿ��ܻ����ɴ���飬��������
        return '&emsp;<a href="#' + str(i) + '">' + line[3:-1] + "</a>  \n"
    elif headline_mark == '###':
        return '&emsp;&emsp;<a href="#' + str(i) + '">' + line[4:-1] + "</a>  \n"
    elif headline_mark == '####':
        return '&emsp;&emsp;&emsp;<a href="#' + str(i) + '">' + line[5:-1] + "</a>  \n"
    elif headline_mark == '#####':
        return '&emsp;&emsp;&emsp;&emsp;<a href="#' + str(i) + '">' + line[6:-1] + "</a>  \n"
    elif headline_mark == '######':
        return '&emsp;&emsp;&emsp;&emsp;&emsp;<a href="#' + str(i) + '">' + line[7:-1] + "</a>  \n"

"""����Ŀ¼�б�"""
def creat_directory(f):
    i = 0
    directory = []
    directory.append('<a name="index">**Index**</a>\n')
    for line in f:
        lines_in_file.append(line)
    f.close()
    length = len(lines_in_file)
    for j in range(length):
        splitedline = lines_in_file[j].lstrip().split(' ')
        if splitedline[0] in headline:
            #���Ϊ���һ����ĩβ�޻��У������һ���ֱ�ȥ����
            if j == length - 1 and lines_in_file[j][-1] != '\n':
                directory.append(creat_directory_line(lines_in_file[j] + '\n',splitedline[0],i) + '\n')
                lines_in_file[j] = lines_in_file[j].replace(splitedline[0] + ' ',splitedline[0] + ' ' + '<a name="' + str(i) + '">')[:] + '</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>' + "\n"
                i = i + 1
            else:
                directory.append(creat_directory_line(lines_in_file[j],splitedline[0],i))
                lines_in_file[j] = lines_in_file[j].replace(splitedline[0] + ' ',splitedline[0] + ' ' + '<a name="' + str(i) + '">')[:-1] + '</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>' + "\n"
                i = i + 1
    return directory

"""��Ŀ¼�б�Ϊ�����������Ŀ¼���ļ�"""
def creat_file_with_toc(f):
    directory = creat_directory(f)
    file_with_toc = os.getcwd() + '\\file_with_toc.md'
    if not os.path.exists(file_with_toc):
        with open(file_with_toc, 'w+',encoding='utf-8') as f:
            for directory_line in directory:
                f.write(directory_line)
            for line in lines_in_file:
                f.write(line)
            print('�ļ�������')
    else:
        print('�ļ����ظ������޸��ļ�'+'file_with_toc.md'+'���ļ���������')

if __name__=='__main__':
    file_name = ''
    #���δ�����ļ���
    if len(sys.argv) < 2:
        path = os.getcwd()
        file_and_dir = os.listdir(path)
        md_file = []
        for item in file_and_dir:
            if item.split('.')[-1].lower() in ['md','mdown','markdown'] and os.path.isfile(item):
                md_file.append(item)
        if len(md_file) != 0:
            print('��ǰĿ¼�µ�Markdown�ļ���')
            for file in md_file:
                print(file)
            file_name = input('�������ļ���(����׺)\n')
        else:
            print('��Ŀ¼����Markdown�ļ��������˳�...')
            time.sleep(2)
            os._exit(0)
    else:
        file_name = sys.argv[1]
    if os.path.exists(file_name) and os.path.isfile(file_name):
        with open(file_name,'r',encoding='utf-8') as f:
            creat_file_with_toc(f)
    else:
        msg = "δ�ҵ��ļ�"
        print(msg)