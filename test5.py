import xlrd


def open_excel(file):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print(str(e))


#根据索引获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_index：表的索引
def excel_table_byindex(file= 'rew_data.xlsx', colnameindex=0, by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows #行数
    ncols = table.ncols #列数
    print(nrows, ncols)
    province_index = divide_by_province(table, nrows, ncols)
    print(province_index)


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
    bound_distance = 100
    excel_table_byindex('rew_data.xlsx', 0, 1)