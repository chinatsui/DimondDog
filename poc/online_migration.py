class OnlineMigration:

    def __init__(self, name: str):
        self.name = name
        self.dependencies = set()

    def execute(self):
        print(self.name)


class OnlineMigrationService:
    def __init__(self, migrations: set):
        for m in migrations:
            self._verify_no_recycle(m, set([m]))
        self.migrations = self._flatten(migrations)
        self.completed = self._strip_completed(self.migrations)
        self.pending = self.migrations - self.completed

    def run(self):
        pending_list = list(self.pending)
        while pending_list:
            cur = pending_list.pop(0)
            if not cur.dependencies - self.completed:
                cur.execute()
                self.completed.add(cur)
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
        return set([m for m in migrations if m.name in ['B', 'C', 'E']])


t_m1 = OnlineMigration("1")
t_m2 = OnlineMigration("2")
t_m3 = OnlineMigration("3")
t_m4 = OnlineMigration("4")
t_m5 = OnlineMigration("5")
t_m6 = OnlineMigration("6")
t_m7 = OnlineMigration("7")

t_m1.dependencies.add(t_m2)
t_m2.dependencies.add(t_m3)
t_m2.dependencies.add(t_m6)

t_m4.dependencies.add(t_m5)

t_migrations = {t_m1, t_m4, t_m7}
OnlineMigrationService(t_migrations).run()
