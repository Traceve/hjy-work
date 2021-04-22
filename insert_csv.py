"""
json 插入表格

date: 2021-4-22
Author: Traceve

"""
import csv,json
name_list = ["201906","201907","201908","201909","201910","201911",
             "202001","202002","202003","202004","202005","202006","202007","202008","202009","202010","202011","202012","202013",
             "202101","202102",]
data = []
for name in name_list:
    csv_path = "csv/"+name+".csv"
    json_path = "json/"+name+".json"
    with open(csv_path,'w',encoding="utf-8-sig",newline="") as f1:
        a = ["车型","外廓尺寸长（mm）","外廓尺寸宽（mm）","外廓尺寸高（mm）","总质量（kg）",
             "整备质量（kg）","电池系统能量密度（Wh/kg）","储能装置种类","驱动电机类型",
             "驱动电机峰值功率/转速/转矩（kW /r/min/N.m）","配置ID","续驶里程（km，工况法）",
             "储能装置总储电量（kWh）","Ekg单位载质量能量消耗量（Wh/km·kg）","30分钟最高车速（km/h）",
             "工况条件下百公里耗电量（Y）（kWh/100km）","续驶里程（km，等速法）","最高车速","电池系统总质量占整车整备质量比例（% ）"]
        writer = csv.DictWriter(f1, fieldnames=a)
        writer.writeheader()
        write = csv.writer(f1)
        for item in open(json_path, "r", encoding="utf8"):
            item = json.loads(item)
            data = []
            for i in item.keys():
                data.append(item[i])
            write.writerow(data)