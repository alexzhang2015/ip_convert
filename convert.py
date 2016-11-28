#!/usr/bin/env python
# coding: utf-8

__author__ = 'alexzhang2014@live.com'


def ipv4_convert(ipv4_addr):
    """
    172.168.5.1 => 2896692481
    :param ipv4_addr:
    :return:
    """

    # null terminated string
    if ipv4_addr[-1] != '\0' :
        raise Exception('This is not valid null terminated string')

    # validate and strip ipv4 string
    # ipv4_list = [x.strip() for x in ipv4_addr.split(".")]
    ipv4_a = []
    ipv4_b = []
    ipv4_c = []
    ipv4_d = []

    dot_count = 0
    for i in xrange(len(ipv4_addr)-1):
        if ipv4_addr[i+1] == '\0':
            ipv4_d.append(ipv4_addr[i])
            break

        if not (ipv4_addr[i].isdigit() or ipv4_addr[i] is '.' or ipv4_addr[i].isspace()):
            raise Exception('This is not valid ipv4 string')

        if i == 0 :
            ipv4_a.append(ipv4_addr[i])
            continue

        befoe_ = ipv4_addr[i-1]
        after_ = ipv4_addr[i+1]
        if ipv4_addr[i].isspace() :
            if befoe_.isdigit() and after_.isdigit():
                raise Exception('This is not valid input')

        if ipv4_addr[i] is '.' :
            dot_count += 1

        if ipv4_addr[i].isdigit():
            if dot_count == 0:
                ipv4_a.append(ipv4_addr[i])
            elif dot_count == 1:
                ipv4_b.append(ipv4_addr[i])
            elif dot_count == 2:
                ipv4_c.append(ipv4_addr[i])
            else:
                ipv4_d.append(ipv4_addr[i])

    print ''.join(ipv4_a)
    print ''.join(ipv4_b)
    print ''.join(ipv4_c)
    print ''.join(ipv4_d)

    # calc
    result = int(''.join(ipv4_a)) << 24 | int(''.join(ipv4_b)) << 16 | int(''.join(ipv4_c)) << 8 | int(''.join(ipv4_d))

    return result
