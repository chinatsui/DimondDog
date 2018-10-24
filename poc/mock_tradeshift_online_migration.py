class OnlineMigration:

    def __init__(self, name: str):
        self.name = name
        self.dependencies = None

    def execute(self):
        pass


class OnlineMigrationService:
    def __init__(self, migrations: set):
        for m in migrations:
            self._dfs_verification(m, set(m))
        self.migrations = self._flatten(migrations)
        self.completed = self._strip_completed(self.migrations)
        self.pending = migrations - self.completed

    def run(self):
        pending_list = list(self.pending)
        while pending_list:
            cur = pending_list.pop(0)
            if not cur.dependencies:
                cur.execute()
            else:
                pending_list.append(cur)

    def _verify_no_recycle(self, m, seen):
        if not m.dependencies:
            return

        for d in m.dependencies:
            if d in seen:
                raise Exception("Dependency cycle found.")
            else:
                new_seen = set(seen)
                new_seen.add(d)
                self._verify_no_recycle(d, new_seen)

    @staticmethod
    def _flatten(migrations: set):
        res = set()
        for m in migrations:
            q = [m]
            while q:
                cur = q.pop(0)
                res.add(cur)
                for d in cur.dependencies:
                    q.append(d)
        return res

    @staticmethod
    def _strip_completed(migrations: set):
        return [m for m in migrations if m.name in ['B', 'C', 'E']]
