from abc import ABC, abstractmethod


class Manipulator:
  
  def __init__(self):
    self.state = UnlockedState()
  
  def transition_to(self, state):
    print(f"Manipulator: Transition to {type(state).__name__}")
    self.state = state
    self.state.context = self

  def lock(self):
    self.locked = True

  def unlock(self):
    self.locked = False


class State(ABC):

  @property
  def context(self):
    return self._context

  @context.setter
  def context(self, context) -> None:
      self._context = context
      
  @abstractmethod
  def lock():
    pass

  @abstractmethod
  def unlock():
    pass


class LockedFullState(State):

  def lock(self):
    print("The manipulator is already locked")
    print("So the object in it got broken")
    self.context.transition_to(LockedEmptyState())

  def unlock(self):
    print("The object held was released")
    self.context.transition_to(UnlockedState())


class LockedEmptyState(State):
  
  def lock(self):
    print("The manipulator is locked")
    self.context.transition_to(LockedFullState())

  def unlock(self):
    print("The manipulator is unlocked")
    self.context.transition_to(LockedEmptyState())


class UnlockedState(State):

  def lock(self):
    print("The manipulator is locked")
    self.context.transition_to(LockedFullState())
  
  def unlock(self):
    print("The manipulator remains unlocked")
    self.context.transition_to(UnlockedState())
