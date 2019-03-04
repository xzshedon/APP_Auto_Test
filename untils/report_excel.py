# encoding: utf-8

''' 制作xlsx的测试报告 '''


import xlwt
from xlwt import *
from datetime import datetime
from config.config import *
from untils.result import parse_result
from untils.log_action import LOG,logger
from untils.get_phone_info import get_phone_info


def first_level():
    fir_style = XFStyle()
    fnt = Font()
    fnt.name = u'微软雅黑'
    fnt.bold = True
    fir_style.font = fnt
    alignment = xlwt.Alignment()
    alignment.horz = xlwt.Alignment.HORZ_CENTER
    alignment.vert = xlwt.Alignment.VERT_CENTER
    fir_style.alignment = alignment
    fir_style.font.height = 430
    return fir_style


def second_level():
    sec_style = XFStyle()
    alignment = xlwt.Alignment()
    alignment.horz = xlwt.Alignment.HORZ_CENTER
    alignment.vert = xlwt.Alignment.VERT_CENTER
    sec_style.alignment = alignment
    sec_style.font.height = 330
    return sec_style


def third_level():
    thi_style = XFStyle()
    thi_style.font.height = 330
    return thi_style


def diff_css(res):
    if res == 'pass':
        style = first_level()
        Pattern = xlwt.Pattern
        Pattern.pattern = xlwt.Pattern.SOLID_PATTERN
        Pattern.pattern_fore_colour = xlwt.Style.colour_map['green']
        style.pattern = Pattern
    else:
        style = second_level()
        Pattern = xlwt.Pattern()
        Pattern.pattern = xlwt.Pattern.SOLID_PATTERN
        Pattern.pattern_fore_colour = xlwt.Style.colour_map['red']
        style.pattern = Pattern
    return style


@logger('生成测试报告')
def create(file_name, test_time, test_version, devices_list):
    try:
        file = Workbook(file_name)
        style1 = first_level()
        style2 = second_level()
        style3 = third_level()

        table = file.add_sheet('测试结果', cell_overwrite_ok=True)
        for i in range(0, 7):
            table.col(i).width = 380*20
        table.write_merge(0,0,0,6,'测试报告',style1)
        table.write_merge(2,3,0,6,'测试详情',style2)
        table.write(4,0,'测试项目',style=style2)
        table.write(5,0,'测试版本',style=style2)
        table.write(6,0,'提测时间',style=style2)
        table.write(7,0,'提测人',style=style2)
        table.write(4,2,'测试人',style=style2)
        table.write(5,2,'测试时间',style=style2)
        table.write(6,2,'审核人',style=style2)
        table.write(8,0,'链接',style=style2)
        table.write(8,1,'品牌',style=style2)
        table.write(8,2,'设备名',style=style2)
        table.write(8,3,'型号',style=style2)
        table.write(8,4,'版本',style=style2)
        table.write(8,5,'通过',style=style2)
        table.write(8,6,'失败',style=style2)
        table.write(4,1,Test_Project_name,style=style2)
        table.write(5,1,test_version,style=style2)
        table.write(6,1,test_time,style=style2)
        table.write(7,1,TiTestuser,style=style2)
        table.write(4,3,Test_user,style=style2)
        table.write(5,3,datetime.now().strftime("%Y-%m-%d %H:%M:%S"),style=style2)
        table.write(6,3,"admin", style=style2)
        all_result = []
        for device in devices_list:
            pass_num, fail_num, result_list = parse_result(device=str(device))
            all_result.append(result_list)
            device_result = get_phone_info(device=str(device))
            table.write(9, 0, device, style=style2)
            table.write(9, 1, device_result['brand'], style=style2)
            table.write(9, 2, device_result['device'], style=style2)
            table.write(9, 3, device_result['model'], style=style2)
            table.write(9, 4, device_result['release'], style=style2)
            table.write(9, 5, pass_num, style=style2)
            table.write(9, 6, fail_num, style=style2)

        table1 = file.add_sheet('测试详情',cell_overwrite_ok=True)
        table1.write_merge(0,0,0,8,'测试详情',style=style1)
        for i in range(0,6):
            table1.col(i).width = 400*20
        table1.write(1, 0, '测试用例编号', style=style3)
        table1.write(1, 1, '测试模块', style=style3)
        table1.write(1, 2, '所需要参数', style=style3)
        table1.write(1, 3, '预期', style=style3)
        table1.write(1, 4, '结果', style=style3)
        table1.write(1, 5, '测试设备', style=style3)
        table1.write(1, 6, '原因', style=style3)
        j = 0
        for i in range(len(all_result)):
            for item in all_result[i]:
                table1.write(j+2, 0, str(eval(item['parameter'])['id']), style=style3)
                table1.write(j+2, 1, str(eval(item['parameter'])['model']), style=style3)
                table1.write(j+2, 2, str(eval(item['parameter'])['case']), style=style3)
                table1.write(j+2, 3, str(eval(item['parameter'])['assert']), style=style3)
                table1.write(j+2, 4, str(item['result']), style=style3)
                table1.write(j+2, 5, str(item['device']), style=style3)
                table1.write(j+2, 6, str(item['reason']), style=style3)
                j += 1
        file.save(file_name)
        LOG.info("测试报告保存成功")
    except Exception as e:
        LOG.error("测试报告生成失败,原因：%s" % e)




