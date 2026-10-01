from models.book import Book
from dotenv import load_dotenv
from pathlib import Path
import os
import json

DATA_FOLDER= "data"
DATA_FILE = "books.json"
#Configuration for book data storage.

class Storage:
    def __init__(self , folder : str =DATA_FOLDER , file=DATA_FILE) :
        load_dotenv()
        self.folder=folder
        self.file=file
        self.path = Path(self.folder) / self.file

    def _ensure_folder(self):
        #Create the data folder if it does not exist.

        if not os.path.exists(self.folder):
            os.makedirs(self.folder)

    def load(self) -> list:
        #Load books from the JSON file and return them as a list.

        if not self.path.exists():
            return []
        # Return an empty list if the storage file does not exist.

        try:
            with open(self.path, "r" ,encoding="utf-8") as file:
                data=json.load(file)

        # Handle invalid or corrupted JSON data.
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON format in storage file: {self.path}")

          # Handle errors while reading the storage file.
        except OSError:
            raise ValueError("Error reading storage file")

        # Make sure the storage data is a list
        if not isinstance(data , list):
            raise ValueError("Storage data must be a list.")

        books=[]
        for item in data:
            books.append(Book.from_dict(item))
        return books
        # Return the list of Book objects Never data Dicts.


    def save(self, books: list) :
        # Make sure the data folder exists.

        self._ensure_folder()

        # Convert each Book object into a dictionary.
        data=[]
        for book in books:
            data.append(book.to_dict())

        try:
            with open(self.path , "w" , encoding="utf-8") as file:
                json.dump(data , file , indent=4 , ensure_ascii=False)

        # Handle errors while writing to the storage file
        except OSError:
            raise ValueError("Error writing to storage file")
        

            
        
    

        
