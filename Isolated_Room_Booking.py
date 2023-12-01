from threading import Lock
from datetime import datetime
from Models import User, MeetingRoom, Meeting, is_room_available

room_booking_lock = Lock()
def book_room(room_id, start_time, end_time, employee_id, attenders_list):
    with room_booking_lock:
        # Check if the room is available for the specified time
        if is_room_available(room_id, start_time, end_time): 
            # Create a new Meeting instance
            new_meeting = Meeting(
                scheduled_by=employee_id,
                attenders=attenders_list,  # Assuming the scheduler is also an attender
                start_time_date=start_time,
                end_time_date=end_time,
                meeting_room_id=room_id
            )

            # Save the new meeting to the database
            new_meeting.save()

            print(f"Room {room_id} booked for meeting {new_meeting.meeting_id} by {employee_id}")

            return True  # Room booked successfully
        else:
            # Room is not available for the specified time
            print(f"Room {room_id} is not available for the specified time.")
            return False

# Example Usage
room_id_to_book = 1
start_time_to_book = "2023-12-01 14:00"
end_time_to_book = "2023-12-01 15:00"
employee_booking = "Employee123"

# Call the book_room function
success = book_room(room_id_to_book, start_time_to_book, end_time_to_book, employee_booking)
