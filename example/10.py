'''
10. 파일 인코딩 변경 프로그램
'''
import os
from chardet import detect
import argparse

def search_dir(dirname):
    result_list = []
    filenames = os.listdir(dirname)

    for filename in filenames:
        full_path = os.path.join(dirname, filename)
        print(full_path)
        if os.path.isdir(full_path): # case directory
            result_list.extend(search_dir(full_path))
        else: # file
            result_list.append(full_path)
    return result_list

def get_encoding_type(filepath):
    with open(filepath, "rb") as f:
        rawdata = f.read() # binary data

    codec = detect(rawdata)
    # print(codec)
    return codec["encoding"]

INCLUDE_EXT_LIST = [".txt", ".smi"]
# path = "c:\\test"
# filelists = search_dir(path)

# python .\example\10.py -f c:\\test -e .txt .smi
parse = argparse.ArgumentParser()
parse.add_argument("-f", type=str)
parse.add_argument("-e", nargs="+") # -e 뒤 열거 된 인자는 리스트로 넘어온다.
args = parse.parse_args()

if args.f is not None:
    path = args.f
    filelists = search_dir(path)

    if args.e is not None:
        if len(args.e) > 0:
            INCLUDE_EXT_LIST = []
            # for e in args.e:
            #     if e[0:1] == ".":
            #         INCLUDE_EXT_LIST.append(e)
            #     else:
            #         INCLUDE_EXT_LIST.append("." + e)
                
            # comprehension
            INCLUDE_EXT_LIST = [e.lower() if e[0:1] == "." else ".{}".format(e.lower()) for e in args.e]
    
    # c:\\test\\aaa.txt
    for file in filelists:
        # splittext
        filename, ext = os.path.splitext(file)
        
        tempfile = filename + "_tmp" + ext
        if ext.lower() in INCLUDE_EXT_LIST:
            encoding = get_encoding_type(file)
            if encoding.lower().find("utf") < 0:
                try:
                    with open(file, "r") as read, open(tempfile, "w", encoding="utf-8") as write:
                        write.write(read.read())

                    os.unlink(file)
                    os.rename(tempfile, file)
                    print("saved {}.".format(file))
                except:
                    pass
                finally:
                    if os.path.exists(tempfile):
                        os.unlink(tempfile)