class Solution:
    @staticmethod
    def can_visit_all_rooms(rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        can_visited = [False] * len(rooms)

        seen = set()
        q = [0]
        while q:
            n = q.pop(0)
            can_visited[n] = True
            for key in rooms[n]:
                if (n, key) not in seen:
                    seen.add((n, key))
                    q.append(key)

        for can in can_visited:
            if not can:
                return False
        return True
