class Door:
    def __init__(self, is_opened=False):
        self.is_opened = is_opened

    def open(self):
        if self.is_opened:
            raise ValueError("Door is already opened.")
        self.is_opened = True

    def close(self):
        if not self.is_opened:
            raise ValueError("Door is already closed.")
        self.is_opened = False


class Lock:
    def __init__(self, is_locked=False):
        self.is_locked = is_locked

    def lock(self):
        if self.is_locked:
            raise ValueError("Door is already locked.")
        self.is_locked = True

    def unlock(self):
        if not self.is_locked:
            raise ValueError("Door is already unlocked.")
        self.is_locked = False


class BlockedDoor(Door):
    def open(self):
        raise TypeError("A blocked door cannot be opened.")

    def close(self):
        raise TypeError("A blocked door cannot be closed.")


d = BlockedDoor()

try:
    d.open()
except TypeError as e:
    print(f"ERROR: {e}")
except Exception as e:
    print(f"UNEXPECTED ERROR: {e}")


class DoorWithALock(Door):
    def __init__(self, is_opened=False):
        self._lock = Lock()
        super().__init__(is_opened=is_opened)

    def open(self):
        if self._lock.is_locked:
            raise ValueError("Door is locked.")
        super().open()

    def close(self):
        if self._lock.is_locked:
            raise ValueError("Door is locked.")
        super().close()
        self.close_times += 1

    def lock(self):
        self._lock.lock()

    def unlock(self):
        self._lock.unlock()


def open_door(d: Door):
    try:
        d.open()
    except TypeError as e:
        print(e)
    except ValueError as e:
        if str(e) == "Door is already opened.":
            pass
        elif str(e) == "Door is locked.":
            d.unlock()
            try:
                d.open()
            except Exception as e:
                print(f"Failed to open door: {e}")
        else:
            raise e from e
    except Exception as e:
        print(f"UNEXPECTED ERROR: {e}")
