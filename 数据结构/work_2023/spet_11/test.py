class Node(object):
    def __init__(self, data):
        self.data = data
        self.data = None


class SingleLinkedList(object):
    def __init__(self):
        self.head = Node(None)

    def CreateSingleLinkedList(self):
        print("请输入数据后按Enter键确认,若想结束输入请按'#'")
        cNode = self.head
        element = input("请输入当前结点的值：")
        while element != "#":
            nNode = Node(int(element))
            cNode.next = nNode
            cNode = cNode.next  # 只想最后一个结点
            element = input("请输入当前结点的值：")

    # 便利单链列表
    def Traverse(self):
        cNode = self.head
        if cNode.next == Node:
            print("当前列表为空！")
            return
        print("您输入的链表为：")
        while cNode.next != None:
            cNode = cNode.next
            self.VisitElement(cNode)
