#!/usr/bin/env python
# coding: utf-8

__author__ = 'alexzhang2014@live.com'

import convert
import pytest


def test_passes():
    with pytest.raises(Exception) as e_info:
        x = 1 / 0


def test_normal_ipv4():
    assert convert.ipv4_convert('172.168.5.1'+'\0') == 2896692481


def test_valid_ipv4_with_whitespace():
    convert.ipv4_convert('172. 168.5.1'+'\0') == 2896692481


def test_invalid_ipv4():
    try:
        convert.ipv4_convert('172.16 8.5.1'+'\0')
        assert False
    except Exception:
        assert True