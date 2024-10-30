from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, message: str) -> None:
        """
        Receives updates from the subject. This method should be implemented in concrete observer classes.
        
        Args:
            message (str): The message containing update information from the subject.
        """
        pass
