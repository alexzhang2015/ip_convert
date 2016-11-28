#!/usr/bin/env python
# coding: utf-8

import convert

def main():
    print convert.ipv4_convert('172.168.5.1'+'\0')

if __name__ == "__main__":
    main()