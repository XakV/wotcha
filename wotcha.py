import pathlib
import subprocess

def build_dir_tree(var_dir):
    dir_tree = []
    vdir_file_obj = var_dir.glob('*')
    for f_obj in vdir_file_obj:
        if f_obj.is_dir():
            file_list = build_dir_tree(f_obj)
            dir_tree.append(file_list)
        else:
            dir_tree.append(f_obj)
    return dir_tree


def show_dir_tree(dir_tree):
    for d_obj in dir_tree:
        try:
            if pathlib.Path(d_obj).is_file():
                obj_mb, obj_gb = bit_converter(d_obj.stat()[6])
                if obj_mb > 1:
                    print(d_obj.name, obj_mb, obj_gb)
        except:
            show_dir_tree(d_obj)
    return


def bit_converter(byte_num):
    mb_num = round(byte_num / 1048576)
    gb_num = round(byte_num / 1073741824)
    return [mb_num, gb_num]


var_dir = pathlib.Path('/home/zach')
dir_tree = build_dir_tree(var_dir)
show_dir_tree(dir_tree)



