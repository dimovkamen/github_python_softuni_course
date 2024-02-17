
def chairs_extracted(chairs_in_room_str):
    chairs_count = len(chairs_in_room_str.split(" ")[0])
    visitors_count = int(chairs_in_room_str.split(" ")[1])
    return chairs_count, visitors_count


number_of_rooms = int(input())
total_free_chairs = 0

for room_number in range(1, number_of_rooms + 1):
    room_info = input()
    chairs_count, visitors_count = chairs_extracted(room_info)
    difference = chairs_count - visitors_count
    if difference < 0:
        print(f"{abs(difference)} more chairs needed in room {room_number}")
    total_free_chairs += difference

if total_free_chairs >= 0:
    print(f"Game On, {total_free_chairs} free chairs left")
