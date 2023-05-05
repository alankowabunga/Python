'''

封包 package: 用來整理&分類模組的資料夾
*專案檔案配置

專案資料夾
    -主程式.py
    封包資料夾
        - __init__.py  #加入此特殊的py程式, 會能被視為封包package
        - 模組一.py
        - 模組二.py
'''

#for example

# 專案資料夾
#     - main.py
#     - geometry #封包資料夾
#         - __init__.py
#         - point.py
#         _ line.py

'''
基本語法:
import 封包名稱.模組名稱 (as 模組別名)
'''

#開一個檔案main.py , 實作練習