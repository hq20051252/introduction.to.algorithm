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
        兄弟节点标记Pu, 插入点的父节点标记Pp.
        (1). C是红色, 如果P是黑色, 就没有违反红黑树性质. 不用处理.
        (2). C是红色, 如果P是红色, Pp是黑色(这是显然的), P与C同为红色, 违
        反性质4.
            (I).如果Pu是红色，就将P, Pu置为黑色， Pp置为红色，这样P,C就不
            冲突。只有Pp与Ppp冲突的可能，但我们将发生冲突的节点向上移了一层。`
            冲突只会发生在一层，不断递归，我们可以将冲突的节点移到根节点，即
            根节点是是红色，到这一步，就只需将根节点置黑色就结束了。
            (II). 如果Pu是黑色，C是P的左孩子节点(若是右孩子节点，就作下左旋
            ，将其变为左孩子节点)，就将P,与Pp的颜色对换，P置为黑色，Pp置为红
            色，再从Pp处作右旋，就可以保证不冲突。


**删除**



"""

__author__ = '何琪'

from graphviz import Digraph


class Node:
    """
    红黑树的节点类型．
    有属性：颜色(红/黑), 值, 父节点指针, 子节点指针, 比较算法.
    """
    def __init__(self, value, comp=cmp, color='red', parent=None, left=None, right=None):
        self.color = color
        self.value = value
        self.comp = comp
        self.parent = parent
        self.left = left
        self.right = right

    def __cmp__(self, other):
        """
        用于比较两个节点内的值的大小.
        """
        return self.comp(self.value, other.value)


class Nil(Node):
    def __init__(self):
        super(Nil, self).__init__(self, None, comp=None, color='black')


class RBTree:
    """
    """
    nil = Nil()

    def __init__(self, comp=cmp):
        self.root = None
        self.comp = comp

    def _findinsertposition(self, insert):
        """
        查找插入节点.
        :param insert:
        :return: 如果树是空的，返回self.nil.
        """
        cur = self.root

        node = self.nil
        while cur is not self.nil:
            node = cur
            if insert >= cur:
                cur = cur.right
            else:
                cur = cur.left

        return node

    def rbinsertfixup(self, node):
        """
        注: 为方便讨论, 给节点编号, 插入的节点标记C, 插入点标记P, 插入点的
        兄弟节点标记Pu, 插入点的父节点标记Pp.
        (1). C是红色, 如果P是黑色, 就没有违反红黑树性质. 不用处理.
        (2). C是红色, 如果P是红色, Pp是黑色(这是显然的), P与C同为红色, 违
        反性质4.
            (I).如果Pu是红色，就将P, Pu置为黑色， Pp置为红色，这样P,C就不
            冲突。只有Pp与Ppp冲突的可能，但我们将发生冲突的节点向上移了一层。`
            冲突只会发生在一层，不断递归，我们可以将冲突的节点移到根节点，即
            根节点是是红色，到这一步，就只需将根节点置黑色就结束了。
            (II). 如果Pu是黑色，C是P的左孩子节点(若是右孩子节点，就作下左旋
            ，将其变为左孩子节点)，就将P,与Pp的颜色对换，P置为黑色，Pp置为红
            色，再从Pp处作右旋，就可以保证不冲突。
        修正树, 使符合红黑树的性质.
        :param node: 插入的节点.
        :return:
        """
        isleft = lambda x: x == x.parent.left
        isroot = lambda x: x == self.root

        c = node
        p = c.parent

        while p != self.root and p.color == 'r':
            if isleft(p):
                pp = p.parent
                pu = p.parent.right

                if pu.color == 'r':
                    p.color = 'b'
                    pu.color = 'b'
                    pp.color = 'r'

                    # 调整当前窗口.
                    c = pp
                    p = c.parent
                else:
                    if not isleft(c):
                        self._leftrotate(p)

                        # 调整窗口
                        p = c
                    p.color = 'b'
                    pp.color = 'r'
                    self._rightrotate(pp)
                    break
            else:
                pp = p.parent
                pu = p.parent.left
                if pu.color == 'r':
                    p.color = 'b'
                    pu.color = 'b'
                    pp.color = 'r'

                    # 调整当前窗口.
                    c = pp
                    p = c.parent
                else:
                    if not isleft(c):
                        self._leftrotate(p)

                        # 调整窗口
                        p = c
                    p.color = 'b'
                    pp.color = 'r'
                    self._leftrotate(pp)
                    break

        if isroot(p):
            p.color = 'b'

        return self.root

    def insert(self, value, comp=cmp):
        """向红黑树中插入一个值.
        :param value: 待插入的值.
        """
        insert = Node(value, color='red', comp=comp)
        node = self._findinsertposition(insert)

        # 空树
        if node == self.nil:
            self.root = insert
        else:
            insert.parent = node
            if node < insert:
                node.right = insert
            else:
                node.left = insert

            self.rbinsertfixup(insert)

    def create(self, vl, comp=cmp):
        """从一列节点构造出红黑树, 不断调用insert方法插入节点.
        :param vl: 红黑树的点的列表.
        :param comp: 节点比较大小的函数."""
        for v in vl:
            self.insert(v, comp)

    def delete(self, node, comp):
        """从红黑树中删除节点node.
        :param node: 要删除的节点.
        :param comp: 节点比较大小的函数."""
        pass

    def find(self, value, comp):
        """查找给定节点.
        :param value: 要查找的节点.
        :param comp: 节点比较大小的函数."""
        pass

    def traversal(self, node, style='preorder'):
        """
        遍历红黑树, 这个方法返回一个生成器. 利用返回的生成器的next()方法
        遍历树.
        :param node: 起始顶点。
        :param style: 遍历方式，默认是先序遍历。还可以指定中序遍历，后序遍历。
        :return:
        """
        pass

    @staticmethod
    def _leftrotate(node):
        """
        以node为顶点的子树进行左旋操作．
        :param node:　以node节点旋转．
        :return:　没有返回值
        """
        isleft = lambda x: x.parent.left == x

        parent = node.parent
        right = node.right
        gson = node.right.left

        gson.parent = node
        node.right = gson

        node.parent = right
        right.left = node

        if isleft(node):
            parent.left = right
        else:
            parent.right = right

        right.parent = parent

    @staticmethod
    def _rightrotate(node):
        """
        以node为顶点的子树进行右旋操作．
        :param node:　以node节点旋转．
        :return:　没有返回值
        """
        isleft = lambda x: x.parent.left == x

        parent = node.parent
        left = node.left
        gson = node.left.right

        gson.parent = node
        node.left = gson

        node.parent = left
        left.right = node

        if isleft(node):
            parent.left = left
        else:
            parent.right = left

        left.parent = parent

    def visualization(self, node):
        """
        以node为顶点节点，画出这个子树。输出为pdf文件。树的可视化输出。
        :param node: 子树的顶点。
        :return:
        """

        dot = Digraph(comment="")

        for i, path in self.traversal(node):
            if i.color == 'red':
                dot.node(path.name, label=i.data, fillcolor='red', fontcolor='black')
            else:
                dot.node(path.name, label=i.data, fillcolor='black', fontcolor='white')

            if i.left is not None:
                dot.edge(path.name, path.name + "0")
            if i.right is not None:
                dot.edge(path.name, path.name + "1")

        return dot.render()

