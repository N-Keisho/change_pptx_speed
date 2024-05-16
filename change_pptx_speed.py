import sys
import os
import shutil
import my_function


try:
    #ファイルパスの読み込み
    originnal_file = sys.argv[1]
    print(originnal_file)

    #ファイルの存在確認
    if(os.path.exists(originnal_file)):

        #拡張子の取得
        path_name, extension = os.path.splitext(originnal_file)

        #パワーポイントか確認
        if(extension == ".pptx"):
            print("これはパワーポイントです")
        
        #倍率を決定
            while(1):
                speed = input("編集スピードを入力してください：")
                if 0.5 <= float(speed) <= 2:
                    break
                else:
                    print("speedは0.5以上2以下の数値にしてください")
            print("複製します")

        #複製
            copy_file_p = path_name + "_x" + speed + extension
            shutil.copy(originnal_file, copy_file_p)
            print("ファイルの複製が完了しました")
            print("zipファイルに変更します")

        #拡張子の変更
            copy_file_z = my_function.change_entension(copy_file_p,".zip")
            print("拡張子を変更しました")
            print("zipファイルの解凍先ファイルを作成します")

        #zipファイルの解凍先ファイルを作成
            zip_folder = my_function.make_folder_unzip(copy_file_z)
            print("zipファイルの解凍先ファイルを作成しました")
            print("zipファイルを解凍します")

        #zipファイルを解凍
            my_function.unzip(copy_file_z,zip_folder)
            print("解凍が終了しました")
            print("音声ファイルの一時保管場所を作成します")

        #音声ファイルの一時保管場所を作成
            temporary_folder = zip_folder + r'\ppt\temporary'
            os.mkdir(temporary_folder)
            print("一時保管用のフォルダを作成しました")
            print("音声ファイルを編集します")

        #音声ファイルの編集
            media_folder = zip_folder + r'\ppt\media'
            my_function.chage_for(media_folder, speed)
            print("音声ファイルの編集が終了しました")
            print("音声ファイルを移動させます")

        #音声ファイルの移動
            my_function.move_file(temporary_folder, media_folder)
            print("音声ファイルの移動が完了しました")
            print("一時保管場所を削除します")

        #一時保管場所を削除
            os.rmdir(temporary_folder)
            print("一時保管場所を削除しました")
            print("フォルダを圧縮します")

        #フォルダをzipに
            zip_name = os.path.splitext(copy_file_p)[0]
            shutil.make_archive(zip_name, format='zip', root_dir=zip_folder)
            print("フォルダの圧縮が終了しました")
            print("拡張子を変更します")

        #zipからpptxへ
            final_file = my_function.change_entension(copy_file_z,".pptx")
            print("拡張子を変更しました")
            print("不要なファイルを削除します")
            
        #不要なファイルを削除する
            shutil.rmtree(zip_folder)
            #print(zip_folder)
            print("不要なファイルを削除しました")

            print("処理が終了しました")


        else:
            print("これはパワーポイントではありません")

    else:
        print("ファイルが存在しません")
except Exception as e:
        print(e)

input("press any key to end")