#!/usr/bin/python
# -*-coding:utf-8-*-
# email: hq20051252@163.com

"""
红黑树是平衡二叉树, 要满足如下5条性质:

1. 节点的颜色只能是红色或黑色.
2. 根节点是黑色.
3. 所有叶子节点是黑色, 叶子节点是哨兵节点.(叶节点不存数据)
4. 红节点的两个子节点是黑色.
5. 从根节点到叶节点的所有路径中, 黑节点的个数相同.

**插入**

    1. 红黑树为空, 直接插入为根节点, 并将根节点置为黑色.
    2. 红黑树不为空, 找到插入点, 插入, 并将插入节点置为红色. 对树进行调整,
    满足红黑树性质. 分为以下几种情况讨论:
        注: 为方便讨论, 给节点编号, 插入的节点标记C, 插入点标记P, 插入点的
        兄弟节点标记Pb, 插入点的父节点标记Pp.
        (1). C是红色, 如果P是黑色, 就没有违反红黑树性质. 不用处理.
        (2). C是红色, 如果P是红色, Pp是黑色(这是显然的), P与C同为红色, 违
        反性质4.
            (I).如果Pu是红色，就将P, Pu置为黑色， Pp置为红色，这样P,N就不
            冲突。只有Pp与Ppp冲突的可能，但我们将发生冲突的节点向上移了一层。
            冲突只会发生在一层，不断递归，我们可以将冲突的节点移到根节点，即
            根节点是是红色，到这一步，就只需将根节点置黑色就结束了。
            (II). 如果Pu是黑色，N是P的左孩子节点(若是右孩子节点，就作下左旋
            ，将其变为左孩子节点)，就将P,与Pp的颜色对换，P置为黑色，Pp置为红
            色，再从Pp处作右旋，就可以保证不冲突。


**删除**



"""

__author__ = '何琪'


class RBTree:
    """
    """
    def __init__(self):
        self.root = None

        pass

    def insert(self, node, comp):
        """向红黑树中插入一个节点.
        :param node: 待插入的节点.
        :param comp: 节点比较大小的函数."""

        pass

    def create(self, nodes, comp):
        """从一列节点构造出红黑树, 不断调用insert方法插入节点.
        :param nodes 红黑树的点的列表.
        :param comp 节点比较大小的函数."""
        pass

    def delete(self, node, comp):
        """从红黑树中删除节点node.
        :param node 要删除的节点.
        :param comp 节点比较大小的函数."""
        pass

    def find(self, node, comp):
        """查找给定节点.
        :param node 要查找的节点.
        :param comp 节点比较大小的函数."""
        pass

    def traversal(self):
        """遍历红黑树, 这个方法返回一个生成器. 利用返回的生成器的next()方法
        遍历树."""
        pass

    def _leftrotate(self, node):
        """
        以node为顶点的子树进行左旋操作．
        :param node:　以node节点旋转．
        :return:　没有返回值
        """

    def _rightrotate(self, node):
        """
        以node为顶点的子树进行右旋操作．
        :param node:　以node节点旋转．
        :return:　没有返回值
        """
