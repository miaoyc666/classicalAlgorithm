#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : trie.py
Author       : miaoyc
Create date  : 2021/12/27 12:41 上午
Description  : 前缀树
"""

from collections import defaultdict


class TrieNode(object):
    """
    前缀树节点
    """
    def __init__(self):
        self.nodes = defaultdict(TrieNode)
        self.count = 1


class Trie(object):
    """
    前缀树
    """

    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        """
        新增节点
        :param word:
        :return:
        """
        cur = self.root
        for char in word:
            if char in cur.nodes:
                cur.nodes[char].count += 1
            cur = cur.nodes[char]

    def find(self, prefix):
        """
        查找节点
        :param prefix:
        :return:
        """
        cur = self.root
        for char in prefix:
            if char not in cur.nodes:
                return 0
            cur = cur.nodes[char]
        return cur.count


if __name__ == "__main__":
    trie_tree = Trie()
    trie_tree.add("test")
    trie_tree.add("alpha")
    trie_tree.add("allow")
    print(trie_tree.find("al"))
    print(trie_tree.find("alp"))
    print(trie_tree.find("tes"))
    print(trie_tree.find("table"))

