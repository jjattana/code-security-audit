from typing import List
from .observer import Observer

class Subject:
    def __init__(self) -> None:
        """
        Initializes a Subject instance with an empty list of observers.
        """
        self._observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        """
        Adds an observer to the subject's list of observers.

        Args:
            observer (Observer): The observer to be added.
        """
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """
        Removes an observer from the subject's list of observers if it exists.

        Args:
            observer (Observer): The observer to be removed.
        """
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, message: str) -> None:
        """
        Notifies all registered observers with a given message.

        Args:
            message (str): The message to send to all observers.
        """
        for observer in self._observers:
            observer.update(message)
