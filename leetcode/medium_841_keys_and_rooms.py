class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # Escapology :-)
        n = len(rooms)
        all_rooms = {r for r in range(n)}  # WE CAN ALSO JUST CHECK THE LEN AT THE END!!!! SAVE MEMORY!!!!
        visited_rooms = set()
        def dfs(room):
            if room not in visited_rooms:
                visited_rooms.add(room)
                keys = rooms[room]  # someone calls this "next_rooms" which is prorbably better
                for key in keys:
                    if key not in visited_rooms:
                        dfs(key)
        dfs(0)
        return all_rooms == visited_rooms

