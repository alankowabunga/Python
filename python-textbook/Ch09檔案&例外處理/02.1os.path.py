'''
檔案和目錄管理: os.path module
可參考以下連結
https://blog.gtwang.org/programming/python-howto-check-whether-file-folder-exists/

檔案是否存在(回傳True or False)
檔案: isfile
資料夾: isdir
連結檔: islink
檔案/資料夾通用: isexit
eg.
import os
os.path.isfile(檔案路徑)
os.path.isdir(資料夾路徑)

!!!其實記這個就好!!!
檔案/資料夾通用: isexit
eg.
import os
os.path.isexit(檔案/資料夾路徑)
'''

import os
filepath = "/etc/motd" # 要檢查的檔案路徑

# 檢查檔案是否存在
if os.path.isfile(filepath):
  print("檔案存在。")
else:
  print("檔案不存在。")

# 檢查是否為連結檔
if os.path.islink(filepath):
  print("連結檔。")
else:
  print("非連結檔。")


folderpath = "/var/log"# 要檢查的目錄路徑
# 檢查目錄是否存在 
if os.path.isdir(folderpath):
  print("目錄存在。")
else:
  print("目錄不存在。")