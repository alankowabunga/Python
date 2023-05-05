'''
多維度資料 DataFrame

# 建立 Dataframe 資料
import pandas as pd
data=pd.DataFrame(字典)

# 建立篩選條件(與資料列數量對應的布林值)
condition=[True,False,True]
condition=data[欄位名稱]>5

# 根據條件完成篩選
filteredData=data[condition]
'''
import pandas as pd

data=pd.DataFrame({
    "name":["amy","bob","charles"],
    "salary":[30000,50000,40000]
})

print("原資料為 \n", data)
print("==============")
print("條件為布林值, 為是否要取值")
condition=[False,True,True]
filteredData=data[condition]
print(filteredData)

print("============")
print("condition=data['salary']>=40000 , salary欄位中資料是是否大於40000 結果為布林值")
print("再用得到的布林值去做真正的篩選")
condition=data["salary"]>=40000 
print(condition)
print("===============")
print("dilteredData=data[condition] 用布林值結果當條件去做篩選")
filteredData=data[condition]
print(filteredData)


print("=============")
#若用 name 欄位中資料amy 當作條件~~結果為布林值
condition=data["name"]=="amy"
print("用amy得出布林值結果當條件做篩選")
print(condition)

print("篩選取值")
filteredData=data[condition]
print(filteredData)
