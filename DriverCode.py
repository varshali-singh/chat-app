from ChatApp import ChatApp


if __name__ == "__main__":
    ca = ChatApp()
    ca.addNewUser("1")
    ca.addNewUser("2")
    ca.addNewUser("3")
    ca.addNewUser("4")
    ca.addNewUser("5")
    ca.addNewUser("6")
    ca.addNewUser("7")
    ca.addNewUser("8", "online")
    ca.addNewUser("9", "online")
    ca.addNewUser("10", "online")
    ca.updateStatus("3", "online")
    ca.updateStatus("8", "online")
    ca.updateStatus("3", "offline")
    ca.updateStatus("2", "online")
    ca.updateStatus("9", "offline")
    ca.updateStatus("3", "online")
    ca.updateStatus("6", "offline")
    ca.displayList()
