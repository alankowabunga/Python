import pandas as pd

#資料索引:pd.DataFrame(字典{}, index=索引列表)
data=pd.DataFrame({
    "name":["amy","bob","charles"],
    "salary":[30000,50000,40000]
},index=["a","b","c"])
print(data)
print("================")

#觀察資料
print("資料數量 data.size:", data.size)
print("資資料形狀(列,狀) data.shape:",data.shape)
print("資料索引 data.index:", data.index)

#取得列(row/橫向)的 Series 資料: 根據順序,根據索引
print("取得第二列: data.iloc['1']", data.iloc[1], sep="\n")
print("============")
print("取得第c列: data.loc['c']", data.loc["c"], sep="\n")

# 取得欄 (column/直向) 的 Series 資料:根據欄位的名稱
# print("取得 name 欄位", data["name",sep="\n"])
names = data["name"] # 取得單維度的 Series 資料
print("把 name 轉成大寫 : name.str.uper()", names.str.upper(),sep="\n")

#計算薪水平均值
salaries=data["salary"]
print("薪水的平均值: salaries.mean", salaries.mean())

#建立新的欄位
data["revenue"]=[50000,40000,30000] # data[新欄位名稱]=列表
#更謹慎地建立方法: data[新欄位名稱]=Series 的資料
data["rank"]=pd.Series([3,6,1],index=["a","b","c"])
print(data)
print("================")

#利用已有欄位複製建立新欄位, 或是操作
data["cp"]=data["revenue"]/data["salary"] #利用已有的revenue, salary欄位操作後建立新欄位"cp"
print("新增欄位cp \n", data)