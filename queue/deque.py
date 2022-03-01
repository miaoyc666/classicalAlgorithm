#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : deque.py
Author       : miaoyc
Create date  : 2022/3/1 4:49 PM 
Description  : 双端队列
"""


class Deque(object):
    """
    双端队列
    """

    def __init__(self):
        self._items = []

    @property
    def is_empty(self):
        """
        判断队列是否为空
        :return:
        """
        return len(self._items) == 0

    @property
    def size(self):
        """
        返回队列大小
        :return:
        """
        return len(self._items)

    def add_head(self, item):
        """
        在队头添加元素
        :param item:
        :return:
        """
        self._items.insert(0, item)

    def add_tail(self, item):
        """
        在队尾添加元素
        :param item:
        :return:
        """
        self._items.append(item)

    def remove_head(self):
        """
        从队头删除元素
        :return:
        """
        return self._items.pop(0)

    def remove_tail(self):
        """
        从队尾删除元素
        :return:
        """
        return self._items.pop()
