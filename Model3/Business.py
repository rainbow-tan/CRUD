# coding=utf-8
from datetime import datetime
import os

import xlrd
from xlrd import xldate_as_tuple

from Model3 import DB


def sort_data(data):
    data.sort(key=lambda x: (x[1], x[2], x[3]))
    return data


def get_key_by_value(data, value):
    """
    根据value获取字典的key
    :param data: {'a': 'aa', 'b': 'bb', 'c': 'cc', 'd': 'aa'}
    :param value: cc
    :return: c
    """
    key = ''
    try:
        key = list(data.keys())[list(data.values()).index(value)]
    except Exception as e:
        msg = '根据value({})获取key失败,字典是({}),异常是({})'.format(value, data, e)
        print(msg)
    return key


gongchu_lilundengji_fengxian = {
    # 功出理论等级封线
    '1': '1-11,9-12',
    '2': '2-11,9-12',
    '3': '3-11,9-12',
    '4': '4-11,9-12',
    '5': '5-11,9-12',
    '6': '1-11,4-12',
    '7': '3-11,5-12',
    '8': '2-11,4-12',
    '9': '1-11,3-12',
    '10': '4-11,5-12',
    }
jieshou_lilundengji_fengxian = {
    # 接收理论等级封线
    '1': '6-16,7-17',
    '2': '8-16,9-17',
    '3': '8-16,7-17,6-9',
    '4': '9-16,10-17',
    '5': '7-16,9-17,6-10',
    '6': '8-16,10-17',
    '7': '7-16,8-17,6-10',
    '8': '8-16,11-17,10-12',
    '9': '9-16,11-17,7-12,6-10',
    '10': '9-16,11-17,10-12',
    '11': '8-16,11-17,6-9,7-12',
    '12': '8-16,11-17,9-12',
    '13': '6-16,11-17,7-12',
    '14': '11-16,12-17',
    '15': '7-16,11-17,6-12',
    '16': '9-16,11-17,8-12',
    '17': '7-16,11-17,6-9,8-12',
    '18': '10-16,11-17,9-12',
    '19': '7-16,11-17,6-10,9-12',
    '20': '10-16,11-17,8-12',
    '21': '7-16,11-17,6-10,8-12',
    '22': '11-16,13-17,10-14,8-12',
    '23': '11-16,13-17,6-10,9-12,7-14',
    '24': '11-16,13-17,9-12,10-14',
    '25': '11-16,13-17,6-9,8-12,7-14',
    '26': '11-16,13-17,8-12,9-14',
    '27': '11-16,13-17,6-12,7-14',
    '28': '11-16,13-17,12-14',
    '29': '7-16,13-17,6-11,12-14',
    '30': '9-16,13-17,8-11,12-14',
    '31': '7-16,13-17,6-9,8-11,12-14',
    '32': '10-16,13-17,9-11,12-14',
    '33': '7-16,13-17,6-10,9-11,12-14',
    '34': '10-16,13-17,8-11,12-14',
    '35': '8-16,13-17,6-10,7-14',
    '36': '8-16,13-17,10-14',
    '37': '9-16,13-17,6-10,7-14',
    '38': '9-16,13-17,10-14',
    '39': '8-16,13-17,6-9,7-14',
    '40': '8-16,13-17,9-14',
    '41': '6-16,13-17,7-14',
    '42': '13-16,14-17',
    '43': '7-16,13-17,6-14',
    '44': '9-16,13-17,8-14',
    '45': '7-16,13-17,8-14,6-9',
    '46': '10-16,13-17,9-14',
    '47': '7-16,13-17,9-14,6-10',
    '48': '10-16,13-17,8-14',
    '49': '7-16,13-17,6-10,8-14',
    '50': '8-16,13-17,10-12,11-14',
    '51': '9-16,13-17,6-10,7-12,11-14',
    '52': '9-16,13-17,10-12,11-14',
    '53': '8-16,13-17,6-9,7-12,11-14',
    '54': '8-16,13-17,9-12,11-14',
    '55': '6-16,13-17,7-12,11-14',
    '56': '12-16,13-17,11-14',
    '57': '7-16,13-17,6-12,11-14',
    '58': '9-16,13-17,8-12,11-14',
    '59': '7-16,13-17,6-9,8-12,11-14',
    '60': '10-16,13-17,9-12,11-14',
    '61': '7-16,13-17,6-10,9-12,11-14',
    '62': '10-16,13-17,8-12,11-14',
    '63': '7-16,13-17,6-10,8-12,11-14',
    '64': '11-16,14-17,10-15,8-12',
    '65': '11-16,14-17,6-10,9-12,7-15',
    '66': '11-16,14-17,9-12,10-15',
    '67': '11-16,14-17,6-9,8-12,7-15',
    '68': '11-16,14-17,8-12,9-15',
    '69': '11-16,14-17,6-12,7-15',
    '70': '11-16,14-17,12-15',
    }


def all_row(file_data):
    for one_data in file_data:
        one_row(one_data)
    return file_data


# 判断*标数据
def can_import(data):
    index = [1, 2, 3, 4, 5, 10]
    msg = ''
    for line, row_data in enumerate(data):
        for required in index:
            if row_data[required] == '':
                msg = '必填项为空,请检查!'
                msg += '\n行列数:从1开始数,第({})行,第({})列'.format(line + 6, required + 1)
                return False, msg

    for line2, row_data in enumerate(data):
        gongchu_keys = list(gongchu_lilundengji_fengxian.keys())
        gongchu_values = list(gongchu_lilundengji_fengxian.values())
        jieshou_keys = list(jieshou_lilundengji_fengxian.keys())
        jieshou_values = list(jieshou_lilundengji_fengxian.values())

        data_16 = str(row_data[16])
        if data_16 != '' and data_16 not in gongchu_keys:
            msg = '功出电平理论等级({})不在范围({})内,请检查!'.format(data_16, gongchu_keys)
            msg += '\n行列数:从1开始数,第({})行,第(Q)列'.format(line2 + 6)
            return False, msg

        data_17 = str(row_data[17])
        if data_17 != '' and data_17 not in gongchu_values:
            msg = '功出电平理论封线({})不在范围({})内,请检查!'.format(data_17, gongchu_values)
            msg += '\n行列数:从1开始数,第({})行,第(R)列'.format(line2 + 6)
            return False, msg

        data_18 = str(row_data[18])
        if data_18 != '' and data_18 not in gongchu_keys:
            msg = '功出电平变更等级({})不在范围({})内,请检查!'.format(data_18, gongchu_keys)
            msg += '\n行列数:从1开始数,第({})行,第(S)列'.format(line2 + 6)
            return False, msg

        data_19 = str(row_data[19])
        if data_19 != '' and data_19 not in gongchu_values:
            msg = '功出电平变更封线({})不在范围({})内,请检查!'.format(data_19, gongchu_values)
            msg += '\n行列数:从1开始数,第({})行,第(T)列'.format(line2 + 6)
            return False, msg

        data_20 = str(row_data[20])
        if data_20 != '' and data_20 not in jieshou_keys:
            msg = '接收电平理论等级({})不在范围({})内,请检查!'.format(data_20, jieshou_keys)
            msg += '\n行列数:从1开始数,第({})行,第(U)列'.format(line2 + 6)
            return False, msg

        data_21 = str(row_data[21])
        if data_21 != '' and data_21 not in jieshou_values:
            msg = '接收电平理论封线({})不在范围({})内,请检查!'.format(data_21, jieshou_values)
            msg += '\n行列数:从1开始数,第({})行,第(V)列'.format(line2 + 6)
            return False, msg

        data_22 = str(row_data[22])
        if data_22 != '' and data_22 not in jieshou_keys:
            msg = '接收电平变更等级({})不在范围({})内,请检查!'.format(data_22, jieshou_keys)
            msg += '\n行列数:从1开始数,第({})行,第(W)列'.format(line2 + 6)
            return False, msg

        data_23 = str(row_data[23])
        if data_23 != '' and data_23 not in jieshou_values:
            msg = '接收电平变更封线({})不在范围({})内,请检查!'.format(data_23, jieshou_values)
            msg += '\n行列数:从1开始数,第({})行,第(X)列'.format(line2 + 6)
            return False, msg
    return True, msg


def network_length_7(value):
    """
    发送模拟电缆电缆长度=>发送模拟电缆模拟固定长度
    接收模拟电缆电缆长度=>接收模拟电缆模拟固定长度
    :param value:
    :return:
    """
    if value == '':
        return ''
    try:
        value = int(value)
    except Exception as e:
        print('电缆长度转换数值失败:{}'.format(value))
        return ''
    if 7250 < value <= 7500:
        ret = '0'
    elif 7000 < value <= 7250:
        ret = '250'
    elif 6750 < value <= 7000:
        ret = '500'
    elif 6500 < value <= 6750:
        ret = '750'
    elif 6250 < value <= 6500:
        ret = '1000'
    elif 6000 < value <= 6250:
        ret = '1250'
    elif 5750 < value <= 6000:
        ret = '1500'
    elif 5500 < value <= 5750:
        ret = '1750'
    elif 5250 < value <= 5500:
        ret = '2000'
    elif 5000 < value <= 5250:
        ret = '2250'
    elif 4750 < value <= 5000:
        ret = '2500'
    elif 4500 < value <= 4750:
        ret = '2750'
    elif 4250 < value <= 4500:
        ret = '3000'
    elif 4000 < value <= 4250:
        ret = '3250'
    elif 3750 < value <= 4000:
        ret = '3500'
    elif 3500 < value <= 3750:
        ret = '3750'
    elif 3250 < value <= 3500:
        ret = '4000'
    elif 3000 < value <= 3250:
        ret = '4250'
    elif 2750 < value <= 3000:
        ret = '4500'
    elif 2500 < value <= 2750:
        ret = '4750'
    elif 2250 < value <= 2500:
        ret = '5000'
    elif 2000 < value <= 2250:
        ret = '5250'
    elif 1750 < value <= 2000:
        ret = '5500'
    elif 1500 < value <= 1750:
        ret = '5750'
    elif 1250 < value <= 1500:
        ret = '6000'
    elif 1000 < value <= 1250:
        ret = '6250'
    elif 750 < value <= 1000:
        ret = '6500'
    elif 500 < value <= 750:
        ret = '6750'
    elif 250 < value <= 500:
        ret = '7000'
    elif 0 < value <= 250:
        ret = '7250'
    elif value == 0:
        ret = '7500'
    else:
        ret = ''
    return ret


def compensation_7(value):
    """
    当电缆规定总长度为7.5时
    发送模拟电缆电缆长度=>发送模拟电缆补偿连接线
    接收模拟电缆电缆长度=>接收模拟电缆补偿连接线
    :param value:
    :return:
    """
    if value == '':
        return ''
    try:
        value = int(value)
    except Exception as e:
        print('电缆长度转换数值失败:{}'.format(value))
        return ''
    if 7250 < value <= 7500:
        ret = '3-29,4-30'
    elif 7000 < value <= 7250:
        ret = '3-5,4-6,7-29,8-30'
    elif 6750 < value <= 7000:
        ret = '3-9,4-10,11-29,12-30'
    elif 6500 < value <= 6750:
        ret = '3-5,4-6,7-9,8-10,11-29,12-30'
    elif 6250 < value <= 6500:
        ret = '3-13,4-14,15-29,16-30'
    elif 6000 < value <= 6250:
        ret = '3-5,4-6,7-13,8-14,15-29,16-30'
    elif 5750 < value <= 6000:
        ret = '3-9,4-10,11-13,12-14,15-29,16-30'
    elif 5500 < value <= 5750:
        ret = '3-5,4-6,7-9,8-10,11-13,12-14,15-29,16-30'
    elif 5250 < value <= 5500:
        ret = '3-17,4-18,19-29,20-30'
    elif 5000 < value <= 5250:
        ret = '3-5,4-6,7-17,8-18,19-29,20-30'
    elif 4750 < value <= 5000:
        ret = '3-9,4-10,11-17,12-18,19-29,20-30'
    elif 4500 < value <= 4750:
        ret = '3-5,4-6,7-9,8-10,11-17,12-18,19-29,20-30'
    elif 4250 < value <= 4500:
        ret = '3-13,4-14,15-17,16-18,19-29,20-30'
    elif 4000 < value <= 4250:
        ret = '3-5,4-6,7-13,8-14,15-17,16-18,19-29,20-30'
    elif 3750 < value <= 4000:
        ret = '3-9,4-10,11-13,12-14,15-17,16-18,19-29,20-30'
    elif 3500 < value <= 3750:
        ret = '3-5,4-6,7-9,8-10,11-13,12-14,15-17,16-18,19-29,20-30'
    elif 3250 < value <= 3500:
        ret = '3-25,4-26,27-29,28-30'
    elif 3000 < value <= 3250:
        ret = '3-5,4-6,7-25,8-26,27-29,28-30'
    elif 2750 < value <= 3000:
        ret = '3-9,4-10,11-25,12-26,27-29,28-30'
    elif 2500 < value <= 2750:
        ret = '3-5,4-6,7-9,8-10,11-25,12-26,27-29,28-30'
    elif 2250 < value <= 2500:
        ret = '3-13,4-14,15-25,16-26,27-29,28-30'
    elif 2000 < value <= 2250:
        ret = '3-5,4-6,7-13,8-14,15-25,16-26,27-29,28-30'
    elif 1750 < value <= 2000:
        ret = '3-9,4-10,11-13,12-14,15-25,16-26,27-29,28-30'
    elif 1500 < value <= 1750:
        ret = '3-5,4-6,7-9,8-10,11-13,12-14,15-25,16-26,27-29,28-30'
    elif 1250 < value <= 1500:
        ret = '3-17,4-18,19-25,20-26,27-29,28-30'
    elif 1000 < value <= 1250:
        ret = '3-5,4-6,7-17,8-18,19-25,20-26,27-29,28-30'
    elif 750 < value <= 1000:
        ret = '3-9,4-10,11-17,12-18,19-25,20-26,27-29,28-30'
    elif 500 < value <= 750:
        ret = '3-5,4-6,7-9,8-10,11-17,12-18,19-25,20-26,27-29,28-30'
    elif 250 < value <= 500:
        ret = '3-13,4-14,15-17,16-18,19-25,20-26,27-29,28-30'
    elif 0 < value <= 250:
        ret = '3-5,4-6,7-13,8-14,15-17,16-18,19-25,20-26,27-29,28-30'
    elif value == 0:
        ret = '3-9,4-10,11-13,12-14,15-17,16-18,19-25,20-26,27-29,28-30'
    else:
        ret = ''
    return ret


def reality_length_7(value):
    if value == '':
        return ''
    try:
        value = int(value)
    except Exception as e:
        print('电缆长度转换数值失败:{}'.format(value))
        return ''
    if 7250 < value <= 7500:
        ret = '7250<S<=7500'
    elif 7000 < value <= 7250:
        ret = '7000<S<=7250'
    elif 6750 < value <= 7000:
        ret = '6750<S<=7000'
    elif 6500 < value <= 6750:
        ret = '6500<S<=6750'
    elif 6250 < value <= 6500:
        ret = '6250<S<=6500'
    elif 6000 < value <= 6250:
        ret = '6000<S<=6250'
    elif 5750 < value <= 6000:
        ret = '5750<S<=6000'
    elif 5500 < value <= 5750:
        ret = '5500<S<=5750'
    elif 5250 < value <= 5500:
        ret = '5250<S<=5500'
    elif 5000 < value <= 5250:
        ret = '5000<S<=5250'
    elif 4750 < value <= 5000:
        ret = '4750<S<=5000'
    elif 4500 < value <= 4750:
        ret = '4500<S<=4750'
    elif 4250 < value <= 4500:
        ret = '4250<S<=4500'
    elif 4000 < value <= 4250:
        ret = '4000<S<=4250'
    elif 3750 < value <= 4000:
        ret = '3750<S<=4000'
    elif 3500 < value <= 3750:
        ret = '3500<S<=3750'
    elif 3250 < value <= 3500:
        ret = '3250<S<=3500'
    elif 3000 < value <= 3250:
        ret = '3000<S<=3250'
    elif 2750 < value <= 3000:
        ret = '2750<S<=3000'
    elif 2500 < value <= 2750:
        ret = '2500<S<=2750'
    elif 2250 < value <= 2500:
        ret = '2250<S<=2500'
    elif 2000 < value <= 2250:
        ret = '2000<S<=2250'
    elif 1750 < value <= 2000:
        ret = '1750<S<=2000'
    elif 1500 < value <= 1750:
        ret = '1500<S<=1750'
    elif 1250 < value <= 1500:
        ret = '1250<S<=1500'
    elif 1000 < value <= 1250:
        ret = '1000<S<=1250'
    elif 750 < value <= 1000:
        ret = '750<S<=1000'
    elif 500 < value <= 750:
        ret = '500<S<=750'
    elif 250 < value <= 500:
        ret = '250<S<=500'
    elif 0 < value <= 250:
        ret = '0<S<=250'
    elif value == 0:
        ret = 'S=0'
    else:
        ret = ''
    return ret


def network_length_10(value):
    if value == '':
        return ''
    try:
        value = int(value)
    except Exception as e:
        print('电缆长度转换数值失败:{}'.format(value))
        return ''
    if 9750 < value <= 10000:
        ret = '0'
    elif 9500 < value <= 9750:
        ret = '250'
    elif 9250 < value <= 9500:
        ret = '500'
    elif 9000 < value <= 9250:
        ret = '750'
    elif 8750 < value <= 9000:
        ret = '1000'
    elif 8500 < value <= 8750:
        ret = '1250'
    elif 8250 < value <= 8500:
        ret = '1500'
    elif 8000 < value <= 8250:
        ret = '1750'
    elif 7750 < value <= 8000:
        ret = '2000'
    elif 7500 < value <= 7750:
        ret = '2250'
    elif 7250 < value <= 7500:
        ret = '2500'
    elif 7000 < value <= 7250:
        ret = '2750'
    elif 6750 < value <= 7000:
        ret = '3000'
    elif 6500 < value <= 6750:
        ret = '3250'
    elif 6250 < value <= 6500:
        ret = '3500'
    elif 6000 < value <= 6250:
        ret = '3750'
    elif 5750 < value <= 6000:
        ret = '4000'
    elif 5500 < value <= 5750:
        ret = '4250'
    elif 5250 < value <= 5500:
        ret = '4500'
    elif 5000 < value <= 5250:
        ret = '4750'
    elif 4750 < value <= 5000:
        ret = '5000'
    elif 4500 < value <= 4750:
        ret = '5250'
    elif 4250 < value <= 4500:
        ret = '5500'
    elif 4000 < value <= 4250:
        ret = '5750'
    elif 3750 < value <= 4000:
        ret = '6000'
    elif 3500 < value <= 3750:
        ret = '6250'
    elif 3250 < value <= 3500:
        ret = '6500'
    elif 3000 < value <= 3250:
        ret = '6750'
    elif 2750 < value <= 3000:
        ret = '7000'
    elif 2500 < value <= 2750:
        ret = '7250'
    elif 2250 < value <= 2500:
        ret = '7500'
    elif 2000 < value <= 2250:
        ret = '7750'
    elif 1750 < value <= 2000:
        ret = '8000'
    elif 1500 < value <= 1750:
        ret = '8250'
    elif 1250 < value <= 1500:
        ret = '8500'
    elif 1000 < value <= 1250:
        ret = '8750'
    elif 750 < value <= 1000:
        ret = '9000'
    elif 500 < value <= 750:
        ret = '9250'
    elif 250 < value <= 500:
        ret = '9500'
    elif 0 < value <= 250:
        ret = '9750'
    else:
        ret = ''
    return ret


def compensation_10(value):
    """
    当电缆规定总长度为10时
    发送模拟电缆电缆长度=>发送模拟电缆补偿连接线
    接收模拟电缆电缆长度=>接收模拟电缆补偿连接线
    :param value:
    :return:
    """
    if value == '':
        return ''
    try:
        value = int(value)
    except Exception as e:
        print('电缆长度转换数值失败:{}'.format(value))
        return ''
    if 9750 < value <= 10000:
        ret = '3-29,4-30'
    elif 9500 < value <= 9750:
        ret = '3-5,4-6,7-29,8-30'
    elif 9250 < value <= 9500:
        ret = '3-9,4-10,11-29,12-30'
    elif 9000 < value <= 9250:
        ret = '3-5,4-6,7-9,8-10,11-29,12-30'
    elif 8750 < value <= 9000:
        ret = '3-13,4-14,15-29,16-30'
    elif 8500 < value <= 8750:
        ret = '3-5,4-6,7-13,8-14,15-29,16-30'
    elif 8250 < value <= 8500:
        ret = '3-9,4-10,11-13,12-14,15-29,16-30'
    elif 8000 < value <= 8250:
        ret = '3-5,4-6,7-9,8-10,11-13,12-14,15-29,16-30'
    elif 7750 < value <= 8000:
        ret = '3-17,4-18,19-29,20-30'
    elif 7500 < value <= 7750:
        ret = '3-5,4-6,7-17,8-18,19-29,20-30'
    elif 7250 < value <= 7500:
        ret = '3-9,4-10,11-17,12-18,19-29,20-30'
    elif 7000 < value <= 7250:
        ret = '3-5,4-6,7-9,8-10,11-17,12-18,19-29,20-30'
    elif 6750 < value <= 7000:
        ret = '3-13,4-14,15-17,16-18,19-29,20-30'
    elif 6500 < value <= 6750:
        ret = '3-5,4-6,7-13,8-14,15-17,16-18,19-29,20-30'
    elif 6250 < value <= 6500:
        ret = '3-9,4-10,11-13,12-14,15-17,16-18,19-29,20-30'
    elif 6000 < value <= 6250:
        ret = '3-5,4-6,7-9,8-10,11-13,12-14,15-17,16-18,19-29,20-30'
    elif 5750 < value <= 6000:
        ret = '3-25,4-26,27-29,28-30'
    elif 5500 < value <= 5750:
        ret = '3-5,4-6,7-25,8-26,27-29,28-30'
    elif 5250 < value <= 5500:
        ret = '3-9,4-10,11-25,12-26,27-29,28-30'
    elif 5000 < value <= 5250:
        ret = '3-5,4-6,7-9,8-10,11-25,12-26,27-29,28-30'
    elif 4750 < value <= 5000:
        ret = '3-13,4-14,15-25,16-26,27-29,28-30'
    elif 4500 < value <= 4750:
        ret = '3-5,4-6,7-13,8-14,15-25,16-26,27-29,28-30'
    elif 4250 < value <= 4500:
        ret = '3-9,4-10,11-13,12-14,15-25,16-26,27-29,28-30'
    elif 4000 < value <= 4250:
        ret = '3-5,4-6,7-9,8-10,11-13,12-14,15-25,16-26,27-29,28-30'
    elif 3750 < value <= 4000:
        ret = '3-17,4-18,19-25,20-26,27-29,28-30'
    elif 3500 < value <= 3750:
        ret = '3-5,4-6,7-17,8-18,19-25,20-26,27-29,28-30'
    elif 3250 < value <= 3500:
        ret = '3-9,4-10,11-17,12-18,19-25,20-26,27-29,28-30'
    elif 3000 < value <= 3250:
        ret = '3-5,4-6,7-9,8-10,11-17,12-18,19-25,20-26,27-29,28-30'
    elif 2750 < value <= 3000:
        ret = '3-13,4-14,15-17,16-18,19-25,20-26,27-29, 28-30'
    elif 2500 < value <= 2750:
        ret = '3-5,4-6,7-13,8-14,15-17,16-18,19-25,20-26,27-29, 28-30'
    elif 2250 < value <= 2500:
        ret = '3-9,4-10,11-13,12-14,15-17,16-18,19-25,20-26,27-29,28-30'
    elif 2000 < value <= 2250:
        ret = '3-5,4-6,7-9,8-10,11-13,12-14,15-17,16-18,19-25,20-26,27-29,28-30'
    elif 1750 < value <= 2000:
        ret = '3-17,4-18,19-21,20-22,23-25,24-26,27-29,28-30'
    elif 1500 < value <= 1750:
        ret = '3-5,4-6,7-17,8-18,19-21,20-22,23-25,24-26,27-29,28-30'
    elif 1250 < value <= 1500:
        ret = '3-9,4-10,11-17,12-18,19-21,20-22,23-25,24-26,27-29,28-30'
    elif 1000 < value <= 1250:
        ret = '3-5,4-6,7-9,8-10,11-17,12-18,19-21,20-22,23-25,24-26,27-29,28-30'
    elif 750 < value <= 1000:
        ret = '3-13,4-14,15-17,16-18,19-21,20-22,23-25,24-26,27-29,28-30'
    elif 500 < value <= 750:
        ret = '3-5,4-6,7-13,8-14,15-17,16-18,19-21,20-22,23-25,24-26,27-29,28-30'
    elif 250 < value <= 500:
        ret = '3-9,4-10,11-13,12-14,15-17,16-18,19-21,20-22,23-25,24-26,27-29,28-30'
    elif 0 < value <= 250:
        ret = '3-5,4-6,7-9,8-10,11-13,12-14,15-17,16-18,19-21,20-22,23-25,24-26,27-29,28-30'
    else:
        ret = ''
    return ret


def reality_length_10(value):
    if value == '':
        return ''
    try:
        value = int(value)
    except Exception as e:
        print('电缆长度转换数值失败:{}'.format(value))
        return ''
    if 9750 < value <= 10000:
        ret = '9750<S<=10000'
    elif 9500 < value <= 9750:
        ret = '9500<S<=9750'
    elif 9250 < value <= 9500:
        ret = '9250<S<=9500'
    elif 9000 < value <= 9250:
        ret = '9000<S<=9250'
    elif 8750 < value <= 9000:
        ret = '8750<S<=9000'
    elif 8500 < value <= 8750:
        ret = '8500<S<=8750'
    elif 8250 < value <= 8500:
        ret = '8250<S<=8500'
    elif 8000 < value <= 8250:
        ret = '8000<S<=8250'
    elif 7750 < value <= 8000:
        ret = '7750<S<=8000'
    elif 7500 < value <= 7750:
        ret = '7500<S<=7750'
    elif 7250 < value <= 7500:
        ret = '7250<S<=7500'
    elif 7000 < value <= 7250:
        ret = '7000<S<=7250'
    elif 6750 < value <= 7000:
        ret = '6750<S<=7000'
    elif 6500 < value <= 6750:
        ret = '6500<S<=6750'
    elif 6250 < value <= 6500:
        ret = '6250<S<=6500'
    elif 6000 < value <= 6250:
        ret = '6000<S<=6250'
    elif 5750 < value <= 6000:
        ret = '5750<S<=6000'
    elif 5500 < value <= 5750:
        ret = '5500<S<=5750'
    elif 5250 < value <= 5500:
        ret = '5250<S<=5500'
    elif 5000 < value <= 5250:
        ret = '5000<S<=5250'
    elif 4750 < value <= 5000:
        ret = '4750<S<=5000'
    elif 4500 < value <= 4750:
        ret = '4500<S<=4750'
    elif 4250 < value <= 4500:
        ret = '4250<S<=4500'
    elif 4000 < value <= 4250:
        ret = '4000<S<=4250'
    elif 3750 < value <= 4000:
        ret = '3750<S<=4000'
    elif 3500 < value <= 3750:
        ret = '3500<S<=3750'
    elif 3250 < value <= 3500:
        ret = '3250<S<=3500'
    elif 3000 < value <= 3250:
        ret = '3000<S<=3250'
    elif 2750 < value <= 3000:
        ret = '2750<S<=3000'
    elif 2500 < value <= 2750:
        ret = '2500<S<=2750'
    elif 2250 < value <= 2500:
        ret = '2250<S<=2500'
    elif 2000 < value <= 2250:
        ret = '2000<S<=2250'
    elif 1750 < value <= 2000:
        ret = '1750<S<=2000'
    elif 1500 < value <= 1750:
        ret = '1500<S<=1750'
    elif 1250 < value <= 1500:
        ret = '1250<S<=1500'
    elif 1000 < value <= 1250:
        ret = '1000<S<=1250'
    elif 750 < value <= 1000:
        ret = '750<S<=1000'
    elif 500 < value <= 750:
        ret = '500<S<=750'
    elif 250 < value <= 500:
        ret = '250<S<=500'
    elif 0 < value <= 250:
        ret = '0<S<=250'
    else:
        ret = ''
    return ret


def change_guidaoleixing(guidaoleixing):
    str1 = guidaoleixing.replace('k', 'K')
    str2 = str1.replace('m', 'M')
    str3 = str2.replace('（', '(')
    str4 = str3.replace('）', ')')
    str5 = str4.replace('t', 'T')
    return str5


def change_db_data(data):
    """数据库轨道类型km变KM,（）变(),t变T"""
    new = []
    for value in data:
        new_value = change_guidaoleixing(value)
        new.append(new_value)
    return new


def cheli_huanzu(data):
    """
    处理环阻
    是整数就保存整数 e.g 14.0=>14 14=>14
    否则保存小数 e.g 14.1=>14.1
    """
    try:
        if is_zhengshu(data[26]):
            data[26] = int(float(data[26]))
    except Exception as e:
        print('发送环阻保存整数失败:{}'.format(data[26]))
    try:
        if is_zhengshu(data[32]):
            data[32] = int(float(data[32]))
    except Exception as e:
        print('接收环阻保存整数失败:{}'.format(data[32]))


def is_zhengshu(number):
    """判断是不是整数"""
    flag = False
    try:
        if float(number) % 1 == 0:
            flag = True
    except Exception as e:
        flag = False
    return flag


def one_row(data_list):
    # print('一行数据')
    # print(data_list)
    # print('======================')
    dianrong(data_list)  # 电容取整
    cheli_huanzu(data_list)  # 处理环阻
    """
    data_list[16]功出电平理论等级
    data_list[17]功出电平理论封线
    data_list[18]功出电平变更等级
    data_list[19]功出电平变更封线
    """

    # 功出电平理论等级与封线互换
    if data_list[16] != '' and str(int(data_list[16])) in gongchu_lilundengji_fengxian:
        data_list[17] = gongchu_lilundengji_fengxian[str(int(data_list[16]))]
    if str(data_list[17]).replace('，', ',') in list(gongchu_lilundengji_fengxian.values()):
        data_list[16] = get_key_by_value(gongchu_lilundengji_fengxian, data_list[17])

    # 功出电平变更等级与封线互换
    if data_list[18] != '' and str(int(data_list[18])) in gongchu_lilundengji_fengxian:
        data_list[19] = gongchu_lilundengji_fengxian[str(int(data_list[18]))]
    if str(data_list[19]).replace('，', ',') in list(gongchu_lilundengji_fengxian.values()):
        data_list[18] = get_key_by_value(gongchu_lilundengji_fengxian, data_list[19])

    # 接收电平理论等级与封线互换
    fengxians = list(jieshou_lilundengji_fengxian.values())
    if data_list[20] != '' and str(int(data_list[20])) in jieshou_lilundengji_fengxian:
        data_list[21] = jieshou_lilundengji_fengxian[str(int(data_list[20]))]
    if str(data_list[21]).replace('，', ',') in fengxians:
        data_list[20] = get_key_by_value(jieshou_lilundengji_fengxian, data_list[21])

    # 接收电平变更等级与封线互换
    if data_list[22] != '' and str(int(data_list[22])) in jieshou_lilundengji_fengxian:
        data_list[23] = jieshou_lilundengji_fengxian[str(int(data_list[22]))]
    if str(data_list[23]).replace('，', ',') in fengxians:
        data_list[22] = get_key_by_value(jieshou_lilundengji_fengxian, data_list[23])

    """
    data_list[24]轨道类型
    data_list[25]电缆规定总长度km
    """

    # 根据轨道类型求电缆规定总长度
    data_list[24] = change_guidaoleixing(data_list[24])
    for_7_5_km = change_db_data(DB.select_duidao_changdu('7.5'))
    for_10_km = change_db_data(DB.select_duidao_changdu('10'))
    if data_list[24] in for_7_5_km:
        data_list[25] = '7.5'
    elif data_list[24] in for_10_km:
        data_list[25] = '10'
    else:
        data_list[25] = ''

    """
    data_list[26]发送模拟电缆环阻
    data_list[27]发送模拟电缆电缆长度
    data_list[28]发送模拟电缆实际电缆长度档位
    data_list[29]发送模拟电缆模拟长度
    data_list[30]发送模拟电缆模拟固定长度
    """

    # 发送
    # 根据环租求电缆长度
    try:
        if data_list[26] != '':
            data_list[27] = round(float(data_list[26]) / 45 * 1000)
    except Exception as e:
        raise RuntimeError('发送环阻转换数值失败:{}'.format(data_list[26]))

    # 根据电缆规定总长度和电缆长度求实际电缆长度档位
    if data_list[25] == '7.5' and data_list[27] != '':
        data_list[28] = reality_length_7(data_list[27])
    elif data_list[25] == '10' and data_list[27] != '':
        data_list[28] = reality_length_10(data_list[27], )
    else:
        data_list[28] = ''

    # 根据电缆规定总长度和电缆长度求模拟长度
    if data_list[25] == '7.5' and data_list[27] != '':
        data_list[29] = int(7500 - data_list[27])
    elif data_list[25] == '10' and data_list[27] != '':
        data_list[29] = int(10000 - data_list[27])
    else:
        data_list[29] = ''

    # 根据电缆规定总长度和电缆长度求模拟固定长度
    if data_list[25] == '7.5' and data_list[27] != '':
        data_list[30] = network_length_7(data_list[27])
    elif data_list[25] == '10' and data_list[27] != '':
        data_list[30] = network_length_10(data_list[27])
    else:
        data_list[30] = ''

    # 根据电缆规定总长度和电缆长度求补偿连接线
    if data_list[25] == '7.5' and data_list[27] != '':
        data_list[31] = compensation_7(data_list[27])
    elif data_list[25] == '10' and data_list[27] != '':
        data_list[31] = compensation_10(data_list[27])
    else:
        data_list[31] = ''

    # 接收
    # 根据环租求电缆长度
    try:
        if data_list[32] != '':
            data_list[33] = round(float(data_list[32]) / 45 * 1000)
    except Exception as e:
        raise RuntimeError('发送环阻转换数值失败:{}'.format(data_list[26]))

    # 根据电缆规定总长度和电缆长度求实际电缆长度档位
    if data_list[25] == '7.5' and data_list[33] != '':
        data_list[34] = reality_length_7(data_list[33])
    elif data_list[25] == '10' and data_list[33] != '':
        data_list[34] = reality_length_10(data_list[33], )
    else:
        data_list[34] = ''

    # 根据电缆规定总长度和电缆长度求模拟长度
    if data_list[25] == '7.5' and data_list[33] != '':
        data_list[35] = int(7500 - data_list[33])
    elif data_list[25] == '10' and data_list[33] != '':
        data_list[35] = int(10000 - data_list[33])
    else:
        data_list[35] = ''

    # 根据电缆规定总长度和电缆长度求模拟固定长度
    if data_list[25] == '7.5' and data_list[33] != '':
        data_list[36] = network_length_7(data_list[33])
    elif data_list[25] == '10' and data_list[33] != '':
        data_list[36] = network_length_10(data_list[33])
    else:
        data_list[36] = ''

    # 根据电缆规定总长度和电缆长度求补偿连接线
    if data_list[25] == '7.5' and data_list[33] != '':
        data_list[37] = compensation_7(data_list[33])
    elif data_list[25] == '10' and data_list[33] != '':
        data_list[37] = compensation_10(data_list[33])
    else:
        data_list[37] = ''

    baocun_zhengshu(data_list)
    return data_list


def dianrong(data):
    """
    处理电容
    14->电容规格
    15->电容数量
    取整 e.g 14.4=>14 14.5=>14 14.9=>14
    """
    try:
        if data[14] != '':
            data[14] = int(float(data[14]))
    except Exception as e:
        print('电容规格取整失败:{}'.format(data[14]))
    try:
        if data[15] != '':
            data[15] = int(float(data[15]))
    except Exception as e:
        print('电容数量取整失败:{}'.format(data[15]))


def baocun_zhengshu(row_data):
    """保存整数"""
    try:
        pass

        row_data[6] = int(row_data[6])

        row_data[7] = int(row_data[7])

        row_data[11] = int(row_data[11])

        row_data[14] = int(row_data[14])

        row_data[15] = int(row_data[15])

        row_data[16] = int(row_data[16])

        row_data[18] = int(row_data[18])

        row_data[20] = int(row_data[20])

        row_data[22] = int(row_data[22])
    except Exception as e:
        pass


def remove_index_for_data(data_list, remove_index=[38, 39, 40, 41, 42, 43, 44]):
    """
    移除不显示字段
    :param data_list:
    :param remove_index:
    :return:
    """
    new_data = []
    for one_data in data_list:
        new_one_data = []
        for index, data in enumerate(one_data):
            if index not in remove_index:
                new_one_data.append(data)
        new_data.append(new_one_data)
    return new_data


def read_xls(filename, read_begin_row=1):
    all_data = []
    if os.path.isfile(filename):
        f = xlrd.open_workbook(filename)  # 打开Excel
        all_sheets = f.sheets()  # 找到所有的表
        if len(all_sheets) >= 1:
            sheet1 = all_sheets[0]
            rows = sheet1.nrows  # 行
            lines = sheet1.ncols  # 列
            for row in range(read_begin_row, rows):
                row_data = []
                for line in range(lines):
                    data_type = sheet1.cell(row, line).ctype
                    if data_type == 2:  # number
                        data = float(sheet1.cell(row, line).value)
                    elif data_type == 3:  # 日期
                        val = sheet1.cell(row, line).value
                        data = datetime(*xldate_as_tuple(val, 0)).strftime('%Y-%m-%d')
                    else:
                        data = sheet1.cell(row, line).value
                    row_data.append(data)
                all_data.append(row_data)
    else:
        print('未找到文件:{}'.format(filename))
    return all_data


if __name__ == '__main__':
    a = dict(a=1, b=2, c=3)
    print(a)
