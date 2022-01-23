#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : heap_sort.py
Author       : miaoyc
Create date  : 2022/1/22 12:44 上午
Description  : 堆排序
"""

"""
堆构建的思路：
1.把无序数组构建成二叉堆，需要从小到大（或从大到小）排序，则构建成最大堆（或最小堆）；
2.循环删除堆顶元素，替换到二叉堆的末尾，调整堆产生新的堆顶。
"""