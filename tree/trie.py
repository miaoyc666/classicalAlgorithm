#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : trie.py
Author       : miaoyc
Create time  : 2021/12/27 12:41 
Update time  : 2022/7/11 18:28
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
        self.is_world = None

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        新增节点
        :param word:
        :return:
        """
        cur = self.root
        for char in word:
            if char not in cur.nodes:
                cur.nodes[char].count += 1
            cur = cur.nodes[char]
        cur.is_world = True

    def search_prefix(self, word: str) -> TrieNode:
        """
        查找前缀
        :param word:
        :return:
        """
        cur = self.root
        for char in word:
            if char not in cur.nodes:
                return None
            cur = cur.nodes[char]
        return cur

    def search(self, word: str) -> bool:
        """
        查找节点
        :param word:
        :return:
        """
        cur = self.search_prefix(word) 
        return True if cur and cur.is_world else False

    def startsWith(self, prefix: str) -> bool:
        """
        前缀
        :param word:
        :return:
        """
        cur = self.search_prefix(prefix)
        
        return True if cur else False


obj = Trie()
obj.insert("apple")
param_2 = obj.search("apple")
param_3 = obj.search("app")
param_3 = obj.startsWith(prefix)



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# class TrieNode(object):
#     """
#     前缀树节点
#     """
#     def __init__(self):
#         self.nodes = defaultdict(TrieNode)
#         self.count = 1


# class Trie(object):
#     """
#     前缀树
#     """

#     def __init__(self):
#         self.root = TrieNode()

#     def add(self, word):
#         """
#         新增节点
#         :param word:
#         :return:
#         """
#         cur = self.root
#         for char in word:
#             if char in cur.nodes:
#                 cur.nodes[char].count += 1
#             cur = cur.nodes[char]

#     def find(self, prefix):
#         """
#         查找节点
#         :param prefix:
#         :return:
#         """
#         cur = self.root
#         for char in prefix:
#             if char not in cur.nodes:
#                 return 0
#             cur = cur.nodes[char]
#         return cur.count


# if __name__ == "__main__":
#     trie_tree = Trie()
#     trie_tree.add("test")
#     trie_tree.add("alpha")
#     trie_tree.add("allow")
#     print(trie_tree.find("al"))
#     print(trie_tree.find("alp"))
#     print(trie_tree.find("tes"))
#     print(trie_tree.find("table"))

