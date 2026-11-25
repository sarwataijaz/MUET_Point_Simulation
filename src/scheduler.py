
"""Scheduling policies for the MUET Point fleet."""


class Scheduler:

    def __init__(self, strategy, queue_threshold=8):

        self.strategy = strategy
        self.queue_threshold = queue_threshold

    def get_dispatch_candidates(self, current_time, terminals):

        interval = None

        if self.strategy == "baseline":
            interval = 15

        elif self.strategy == "improved":
            interval = 10

        if interval is not None:

            if int(current_time) % interval == 0:
                return [
                    terminal
                    for terminal in terminals.values()
                    if terminal.queue
                ]

            return []

        if self.strategy == "optimized":

            candidates = [
                terminal
                for terminal in terminals.values()
                if len(terminal.queue) >= self.queue_threshold
            ]

            if candidates:
                return [
                    max(candidates, key=lambda t: len(t.queue))
                ]

        return []
