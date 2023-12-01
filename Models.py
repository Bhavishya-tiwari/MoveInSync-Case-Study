class User:
    def __init__(self, username, email_id, name, department, designation):
        self.username = username
        self.email_id = email_id
        self.name = name
        self.department = department
        self.designation = designation

    def __str__(self):
        return f"Username: {self.username}, EmailID: {self.email_id}, 
        Name: {self.name}, Department: {self.department}, 
        Designation: {self.designation}"
    
class MeetingRoom:
    def __init__(self, room_id, address, capacity):
        # Parameters:
        # - room_id (int): Unique identifier for the meeting room.
        # - address (str): Address of the meeting room.
        # - capacity (int): Maximum capacity of the meeting room.
    
        self.RoomId = room_id
        self.Address = address
        self.Capacity = capacity

class Meeting:
    # Class variable to keep track of the last assigned meeting_id
    last_meeting_id = 0
    def __init__(self, scheduled_by, attenders, start_time_date, end_time_date, meeting_room_id, status="Not_started"):
        """
        Initialize a Meeting instance.

        Parameters:
        - meeting_id (int): Unique identifier for the meeting.
        - scheduled_by (str): Username of the user who scheduled the meeting.
        - attenders (list): List of usernames of attendees.
        - start_time_date (str): Start date and time of the meeting in the format "YYYY-MM-DD HH:MM".
        - end_time_date (str): End date and time of the meeting in the format "YYYY-MM-DD HH:MM".
        - meeting_room_id (int): Foreign key referencing the Meeting Room where the meeting takes place.
        - status (str): Not started yet, Ongoing, Finished and Pending
        """
        Meeting.last_meeting_id += 1

        self.meeting_id = Meeting.last_meeting_id # new meeting id = last meeting id + 1
        self.scheduled_by = scheduled_by
        self.attenders = attenders
        self.start_time_date = start_time_date
        self.end_time_date = end_time_date
        self.meeting_room_id = meeting_room_id
        self.status = status

def is_room_available(room_id, start_time, end_time):
    return True