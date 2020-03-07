#*_coding:utf-8_*_
import xml.etree.ElementTree as ET

root = ET.parse('GHO.xml')#------------------分析指定xml文件
tree = root.getroot()#-----------------------获取第一标签
data = tree.find('Data')#--------------------查找第一标签中'Data'标签
for obs in data:#----------------------------历遍'Data'中的所有标签
    print obs,type(obs)
    if len(obs) >= 1:
        t = obs[0].attrib.keys()
        print t
    # for items in obs:#------------------------历遍'Data'中的'obs'标签下的所有标签
    #     print items
    #     key = items.attrib()#-----------------提取key值参数
    #     print key
        #print(list(key))#--------------------输出key值