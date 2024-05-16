#change_pptx_speed用の自作関数集

import os
import shutil
import subprocess


#拡張子を変更する関数
def change_entension(original_file, to_entension):
    #変更するファイルのパスと拡張子を取得
    path_name, original_entension = os.path.splitext(original_file)
    #名前を変更
    print(original_entension + "  →→→  " + to_entension)
    os.rename(original_file, path_name + to_entension)
    return path_name + to_entension


#解凍先のフォルダを作る関数
def make_folder_unzip(original_file):
    #フォルダ名を取得（受け取ったファイル名）
    folder_name = os.path.splitext(os.path.basename(original_file))[0]
    #フォルダのパスを作成
    folder_path = os.path.dirname(original_file) + "\\" + folder_name
    #フォルダを作成
    os.mkdir(folder_path)
    return folder_path


#zipファイルを解凍する関数
def unzip(zip_file, zip_folder):
    try:
         shutil.unpack_archive(zip_file,zip_folder)
    except Exception as e:
        print(e)
    else:
        print("解凍が正常に終了しました")


#倍速編集する関数
def chage_speed(original_file, chaged_file, speed):
    #subprocess.run('ffmpeg -i ' + original_file + ' -af atempo=' + speed + ' ' + chaged_file, shell=True)
    subprocess.run('ffmpeg -i ' + original_file + ' -af atempo=' + speed + ' ' + chaged_file, shell=True, stdout=subprocess.DEVNULL)
    #subprocess.run('ffmpeg -i ' + original_file + ' -af atempo=' + speed + ' ' + chaged_file, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


#すべての音声ファイルを倍速にする関数
def chage_for(folder,speed):
    to_folder = os.path.dirname(folder) + '\\temporary\\'
    j = 0
    i = 0
    for file in os.listdir(folder):
        extension = os.path.splitext(file)[1]
        if (extension == ".mp3") or (extension == ".m4a") :
            j = j + 1

    if j == 0:
        print("音声ファイルが存在しません")
    else:
        for file in os.listdir(folder):
            extension = os.path.splitext(file)[1]
            if (extension == ".mp3") or (extension == ".m4a") :
                i = i + 1
                print(i , '/', j, '個目のファイルを編集中です・・・')
                original_file = folder + '\\' + file
                chaged_file = to_folder + os.path.basename(file)
                chage_speed(original_file, chaged_file, speed)
    
            
    
#音声ファイルを移動させる関数
def move_file(folder,to_folder):
    for file in os.listdir(folder):
        original_file = folder + '\\' + file
        moved_file = to_folder + '\\' + file
        shutil.move(original_file, moved_file)
