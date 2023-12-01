from datetime import datetime
from django.db.models import Q
from Models import User, MeetingRoom, Meeting 

def find_available_rooms(capacity_needed, start_time, end_time):
    start_datetime = datetime.strptime(start_time, "%Y-%m-%d %H:%M")
    end_datetime = datetime.strptime(end_time, "%Y-%m-%d %H:%M")

    # Query to find available rooms using Django models
    available_rooms = MeetingRoom.objects.filter(
        Capacity__gte=capacity_needed,
        id__in=Meeting.objects.exclude(
            (Q(start_time_date__gte=start_datetime) & Q(start_time_date__lt=end_datetime)) |
            (Q(end_time_date__gt=start_datetime) & Q(end_time_date__lte=end_datetime))
        ).values_list('meeting_room_id', flat=True)
    ).values_list('id', flat=True)

    return available_rooms

# Example usage
capacity_needed = 15
start_time = "2023-01-01 12:00"
end_time = "2023-01-01 14:00"

available_rooms = find_available_rooms(capacity_needed, start_time, end_time)

print("Available Rooms:", available_rooms)
