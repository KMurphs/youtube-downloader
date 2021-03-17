import json
import logging

class DownloadIterator:

  def __init__(self, file_path: str = None, prompt_message = "Enter Youtube Video Link (Leave Empty To Stop): "):

    self.usesIteratorFromPrompts = file_path is None
    self.concreteIterator = IteratorFromPrompts(prompt_message) if file_path is None else IteratorFromFile(file_path)


  def __iter__(self):
    return self.concreteIterator.__iter__()


  def __next__(self):
    self.concreteIterator.__next__()


  def usesPrompts(self): return self.usesIteratorFromPrompts





class IteratorFromFile:
  def __init__(self, file_path: str = None):

    self.values = None
    

    try: 
      with open(file_path, "r") as f:
        self.values = f.readlines()
    except Exception as e:
      logging.debug(f"The content of '{file_path}' could not be interpreted as json array")
      pass


    try: 
      with open(file_path, "r") as f:
        tmp = json.load(f)
        if not isinstance(tmp, list): raise Exception("json object is not an array")
        self.values = tmp
    except Exception as e:
      logging.debug(f"The content of '{file_path}' could not be interpreted as json array")
      pass


    if self.values == None:
      raise Exception(f"File '{file_path}' could not be read")


  def __iter__(self):
    """This creates the iterator. It is called when the iterator is first initialized 
    (aka the first time a value is required from the iterator)

    Returns:
        [str]: A string that indicates a video link
    """
    self.current = 0

    return self



  def __next__(self):
    
    if self.current == len(self.values):
      raise StopIteration

    current_value = self.values[self.current]
    self.current = self.current + 1

    return current_value






class IteratorFromPrompts:

  def __init__(self, file_path: str = None, prompt_message = "Enter Youtube Video Link (Leave Empty To Stop): "):
    self.prompt_message = prompt_message



  def __iter__(self):
    """This creates the iterator. It is called when the iterator is first initialized 
    (aka the first time a value is required from the iterator)

    Returns:
        [str]: A string that indicates a video link
    """
    return self


  def __next__(self):
    
    current_value = input(f"\n{self.prompt_message}")
    if current_value == "" or current_value == None:
      raise StopIteration

    return current_value







if __name__ == "__main__":
  for i in DownloadIterator(file_path="./app/downloads/downloads.json"): print(i)
