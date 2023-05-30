What's required from the project?

    Imagine you are making a chat app. 
    You have been given the task to handle the list of users you are connected to in the app. 
    The list maintains the users in the list in a certain order.
    As a user’s status updates, the list should update to reflect that.

    Points to keep in mind:

    You do not need to make the view for this problem, just the data structure for the list of users.
    This list periodically receives update events with new status of a user in the list which contains user’s: id, current online status, timestamp of update
    The ordering in the list is online first then offline, all online users are sorted according to time with the latest update first, same for all offline users.
