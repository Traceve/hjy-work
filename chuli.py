# -*- coding: UTF-8 -*-
"""
将txt文本转换为json的形式，去取出对应字段，方便插入表格。

date: 2021-4-22
Author: Traceve
"""

import json,re

name_list = ["201906","201907","201908","201909","201910","201911",
             "202001","202002","202003","202004","202005","202006","202007","202008","202009","202010","202011","202012","202013",
             "202101","202102",]

# 删除标点符号(此函数删除冒号)
def removebdfh(text):
    text = re.sub(r'[{}]+'.format(':：'),'',text)
    return text

def deal_rule(s):
    data = []
    s = str(s).replace("  ", ",").replace(" ", "").replace("\n",'')
    s = str(s).replace(",,,,", ',')
    s = s.split(',')
    for j in s:
        if j != '':
            data.append(j)
    result = "， ".join(data)
    return result


for t_name in name_list:
    path1 = "json/"+t_name+".json"
    path2 = "txt/" + t_name + ".txt"
    f2 = open(path1, "w", encoding="utf-8")
    with open(path2, "r", encoding='utf-8') as f:
        count = 1
        count2 = 0
        data = []
        data1 = []
        data2 = []

        # 删除多余行
        for i in f:
            count += 1
            if len(i) != 1 and i.find('Page') == -1 and i.find('《') == -1:
                data.append(i)
            else:
                continue

        # 将两行分开的内容合并到一行
        for num, j in enumerate(data):
            if j.find('、') != -1 and j.find("二、") == -1:
                data1 = []
                if data[num+1].find("外廓") == -1 and len(data[num+1]) > 1:
                    name = j+data[num+1]
                else:
                    name = j
                data1.append(name)
                data2.append(data1)
            else:
                data1.append(j)

        # 抽取对应字段过程
        for w in data2:
            count2 += 1
            for n, m in enumerate(w):
                if w[1].find("车辆基本信息") != -1:
                    w[0] = w[0].split("车辆基本信息")[0]
            cx = ''
            id = ''
            ccc = ''
            cck = ''
            ccg = ''
            zzl = ''
            zbzl = ''
            nlmd = ''
            zzlx = ''
            djlx = ''
            fzgl = ''
            xhlcds = ''
            xhlcgk = ''
            zcdl = ''
            ekgxhl = ''
            zgcs = ''
            gkhdl = ''
            zgcs1 = ''
            zlbl = ''
            for y, x in enumerate(w):
                cx = w[0].strip().replace("\n", '').replace(" ", '')
                s1 = re.split("、", str(cx))
                print(cx)
                cx = str(count2) + "、" + s1[1]
                if x.find("配置ID") != -1:
                    id = x.replace("车辆基本信息                      配置ID ：", "").replace("车辆基本信息", "").replace("配置ID ：", "")
                    id = deal_rule(id)
                    id = id.replace("*", '')
                elif x.find("外廓尺寸长") != -1 and x.find("：") != -1:
                    print(x)
                    ccc = re.split(":|：", x)[1]
                    ccc = deal_rule(ccc)
                    ccc = re.sub('[a-zA-Z|\u4e00-\u9fa5|:|：|（）]', "", ccc)
                elif x.find("外廓尺寸宽") != -1 and x.find("：") != -1:
                    cck = re.split(":|：", x)[1]
                    cck = deal_rule(cck)
                    cck = re.sub('[a-zA-Z|\u4e00-\u9fa5|:|：|（）]', "", cck)
                elif x.find("外廓尺寸高") != -1 and x.find("：") != -1:
                    ccg = re.split(":|：", x)[1]
                    ccg = deal_rule(ccg)
                    ccg = re.sub('[a-zA-Z|\u4e00-\u9fa5|:|：|（）]', "", ccg)
                elif x.find("总质量") != -1 and x.find("kg") != -1:
                    zzl = re.split(":|：", x)[1]
                    zzl = deal_rule(zzl)
                    zzl = re.sub('[a-zA-Z|\u4e00-\u9fa5|:|：|（）]', "", zzl)
                elif x.find("整备质量") != -1 and x.find("：") != -1 and x.find("kg") != -1:
                    print(x)
                    zbzl = re.split(":|：", x)[1]
                    zbzl = deal_rule(zbzl)
                    zbzl = re.sub('[a-zA-Z|\u4e00-\u9fa5|:|：|（）]', "", zbzl)
                elif x.find("电池系统能量密度") != -1 and x.find("：") != -1:
                    nlmd = re.split(":|：", x)[1]
                    nlmd = deal_rule(nlmd)
                    nlmd = re.sub('[a-zA-Z|\u4e00-\u9fa5:]', "", nlmd)
                elif x.find("储能装置种类") != -1:
                    zzlx = re.split(":|：", x)[1]
                    zzlx = deal_rule(zzlx)
                elif x.find("驱动电机类型：") != -1:
                    djlx = re.split(":|：", x)[1]
                    djlx = deal_rule(djlx)
                elif x.find("驱动电机峰值功率/转速/转矩") != -1 :
                    print(w[y])
                    fzgl = w[y+1]
                    fzgl = deal_rule(fzgl)
                elif x.find("续驶里程") != -1 and x.find("等速法") != -1:
                    xhlcds = re.split(":|：", x)[1]
                    xhlcds = deal_rule(xhlcds)
                elif x.find("续驶里程") != -1 and x.find("工况法") != -1:
                    xhlcgk = re.split(":|：", x)[1]
                    xhlcgk = deal_rule(xhlcgk)
                elif x.find("储能装置总储电量") != -1 and x.find("：") != -1:
                    zcdl = re.split(":|：", x)[1]
                    zcdl = re.sub('[a-zA-Z|\u4e00-\u9fa5|:|：|（）]', "", zcdl)
                    zcdl = deal_rule(zcdl)
                elif x.find("Ekg单位载质") != -1 and x.find("：") != -1:
                    x = re.split(":|：", x)[1]
                    ekgxhl = deal_rule(x)
                    ekgxhl = re.sub('[a-zA-Z|\u4e00-\u9fa5|:|：|（）|/|·]', "", ekgxhl)
                elif x.find("30分钟最高车速") != -1 and x.find("：") != -1:
                    zgcs = re.split(":|：", x)[1]
                    zgcs = deal_rule(zgcs)
                elif x.find("最高车速") != -1 and x.find("：") != -1:
                    zgcs_1 = re.split(":|：", x)[1]
                    zgcs_1 = deal_rule(zgcs_1)
                elif x.find("工况条件下百公里耗电量") != -1:
                    gkhdl = w[y+1]
                    gkhdl = deal_rule(gkhdl)
                elif x.find("电池系统总质量占整车整备质量比例") != -1:
                    zlbl = re.split(":|：", x)[1]
                    zlbl = deal_rule(zlbl)
                else:
                    continue
            ele = {"cx": cx, "ccc": ccc, "cck": cck, "ccg": ccg, "zzl": zzl, "zbzl": zbzl,
                   "nlmd": nlmd, "zzlx": zzlx,"djlx": djlx, "fzgl": fzgl,"id": id, "xhlcgk": xhlcgk,
                   "zcdl": zcdl, "ekgxhl": ekgxhl, "30_zgcs": zgcs, "gkhdl": gkhdl, "xhlcds": xhlcds, "zgcs": zgcs_1, "zlbl": zlbl}
            t = json.dumps(ele, ensure_ascii=False).encode("utf-8").decode()
            f2.write(t + "\n")
            print(y,ele)
            print("***"*8)
            print(count2,"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

