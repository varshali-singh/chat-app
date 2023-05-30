import time
from User import User
from Node import Node
from Status import Status


class ChatApp:
    def __init__(self):
        self.__onlineHead = None
        self.__onlineTail = None
        self.__offlineHead = None
        self.__offlineTail = None
        self.__userIdNodeMap = {}

    #method for adding new user to list
    def addNewUser(self, id, status=Status.Offline.value):
        if id in self.__userIdNodeMap.keys():
            print("<<ERROR in addNewUser>> : user id:",
                  id, "- User already present in list")
            return
        if status == Status.Online.value:
            self.__addNewUserToOnline(id)
        elif status == Status.Offline.value:
            self.__addNewUserToOffline(id)
        else:
            print("<<ERROR in addNewUser>> : user id:", id,
                  "-status can either be online or offline\n")

    def __addNewUserToOffline(self, id):
        u = User(id, Status.Offline.value)
        temp = Node(u)
        if self.__offlineHead is None:
            self.__offlineHead = temp
            self.__offlineTail = temp
        else:
            temp.next = self.__offlineHead
            self.__offlineHead.prev = temp
            self.__offlineHead = temp
        self.__userIdNodeMap[id] = temp

    def __addNewUserToOnline(self, id):
        u = User(id, Status.Online.value)
        temp = Node(u)
        if self.__onlineHead is None:
            self.__onlineHead = temp
            self.__onlineTail = temp
        else:
            temp.next = self.__onlineHead
            self.__onlineHead.prev = temp
            self.__onlineHead = temp
        self.__userIdNodeMap[id] = temp

    def updateStatus(self, userId, userStatus):
        if userId not in self.__userIdNodeMap.keys():
            print("<<ERROR in updateStatus>> : user with user id:",
                  userId, "is not present in the list\n")
            return
        if (userStatus != Status.Online.value and
                userStatus != Status.Offline.value):
            print("<<ERROR in updateStatus>> : user id:", userId,
                  "-status can either be online or offline\n")
            return
        self.__deleteUser(self.__userIdNodeMap[userId])
        self.__userIdNodeMap[userId].data.status = userStatus
        self.__userIdNodeMap[userId].data.statusChangeTime = time.time()
        self.__addUser(self.__userIdNodeMap[userId])

    def __deleteUser(self, nodeRef):
        #case for head node
        if nodeRef.prev == None:
            nodeRef.next.prev = None
            if (nodeRef.data.status == Status.Offline.value):
                self.__offlineHead = nodeRef.next
            if (nodeRef.data.status == Status.Online.value):
                self.__onlineHead = nodeRef.next  # 3->node
        #case for tail node
        elif nodeRef.next == None:
            nodeRef.prev.next = None
            if (nodeRef.data.status == Status.Offline.value):
                self.__offlineTail = nodeRef.prev
            if (nodeRef.data.status == Status.Online.value):
                self.__onlineTail = nodeRef.prev
        #case for in-between node
        else:
            nodeRef.prev.next = nodeRef.next
            nodeRef.next.prev = nodeRef.prev

    #method for adding existing user
    def __addUser(self, nodeRef):
        userId = nodeRef.data.id
        if nodeRef.data.status == Status.Offline.value:
            self.__addNewUserToOffline(userId)
        else:
            self.__addNewUserToOnline(userId)

    #method for printing list
    def displayList(self):
        onlineHead = self.__onlineHead
        offlineHead = self.__offlineHead
        print("Sorted list in the required order is given below:")
        while onlineHead is not None:
            print(onlineHead.data.id, "-online")
            onlineHead = onlineHead.next
        while offlineHead is not None:
            print(offlineHead.data.id, "-offline")
            offlineHead = offlineHead.next
