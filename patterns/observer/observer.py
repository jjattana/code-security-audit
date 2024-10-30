from abc import ABC, abstractmethod

class Observer(ABC):
    """
    Abstract base class for observers in the Observer design pattern.

    Observers implement this interface to receive updates from a subject when the subject's state changes.
    Concrete observer classes must implement the `update` method to handle the incoming messages.
    """
    @abstractmethod
    def update(self, message: str) -> None:
        """
        Receives updates from the subject. This method should be implemented in concrete observer classes.
        
        Args:
            message (str): The message containing update information from the subject.
        """
        pass
