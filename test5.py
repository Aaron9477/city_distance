import xlrd
import  xdrlib ,sys


def open_excel(file):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print(str(e))


#根据省份不同，划分成数组，提取出不同省份数据起始点
def divide_by_province(table, nrows, ncols):
    province_col = ncols - 1    #province的列数索引
    province_current = table.cell(1, province_col).value
    province_index = [1, ]
    for i in range(2, nrows-1):
        if province_current != table.cell(i, province_col).value:
            province_current = table.cell(i, province_col).value
            province_index.append(i)
    return province_index




if __name__=="__main__":
    file = 'rew_data.xlsx'  #文件路径
    bound_distance = 100    #设定在多少公里内，认为是邻近城市
    by_index = 1    #使用第二个表，如果使用第一个表，by_index=0


    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows #行数
    ncols = table.ncols #列数
    province_index = divide_by_province(table, nrows, ncols)
    print(province_index)

