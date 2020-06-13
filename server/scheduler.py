import functools
import itertools
from typing import Any, Callable


class TaskNotRetrieved(Exception):
    pass


class Task:

    def __init__(self, callable: Callable, interval: float, repeat: bool = False) -> None:
        self.callable = callable
        self.interval = interval
        self.repeat = repeat

        self._delta_time = 0

    def __call__(self, delta_time: float) -> bool:
        self._delta_time += delta_time

        if self._delta_time >= self.interval:
            self.callable()
            self._delta_time = 0

            if not self.repeat:
                return True

        return False


class Scheduler:
    _tasks = dict()
    _ids = itertools.count()

    @classmethod
    def schedule(cls, callable: Callable, interval: float, repeat: bool = False, *args: Any, **kwargs: Any) -> int:
        task_id = next(cls._ids)
        cls._tasks[task_id] = Task(functools.partial(callable, *args, **kwargs), interval, repeat)
        return task_id

    @classmethod
    def unschedule(cls, task_id: int) -> None:
        try:
            cls._tasks.pop(task_id)

        except KeyError:
            raise TaskNotRetrieved(f'Task {task_id} is not found') from None

    @classmethod
    def collect(cls, delta_time: float) -> None:
        for task_id, task in cls._tasks.items():
            should_remove = task(delta_time)

            if should_remove:
                cls._tasks.pop(task_id)
