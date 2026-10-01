from dataclasses import dataclass

MAX_TITLE_LENGTH = 100
MAX_AUTHOR_NAME = 100


@dataclass
# dataclass generates __init__, __repr__, __eq__, etc.


class Book:
    title: str
    author: str
    read: bool = False
    id: int = 0
    # fileds with def must comes last --> Python requires it

    def __post_init__(self):
        # Validate and normalize book data after initialization.

        if not isinstance(self.title, str):
            raise ValueError("Title must be string")
        if not isinstance(self.author, str):
            raise ValueError("Author must be string")

        self.title = self.title.strip()
        self.author = self.author.strip()

        if self.title == "":
            raise ValueError("Title cannot be empty")

        if self.author == "":
            raise ValueError("Author cannot be empty")

        if len(self.title) > MAX_TITLE_LENGTH:
            raise ValueError(f"Title cannot exceed {MAX_TITLE_LENGTH} characters")

        if len(self.author) > MAX_AUTHOR_NAME:
            raise ValueError(f"Author cannot exceed {MAX_AUTHOR_NAME} characters")

    def mark_read(self):
        # A metod instead of setiing book.read = True frome outside
        self.read = True

    def mark_unread(self):
        # A metod instead of setiing book.read = False frome outside
        self.read = False

    def to_dict(self) -> "dict":
        # Convert the Book object to a dictionary.
        return {
            "title": self.title,
            "author": self.author,
            "read": self.read,
            "id": self.id,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Book":
        # Create a Book object from a dictionary.

        if not isinstance(data, dict):
            raise ValueError("Data must be a Dictionary")

        for key in ["id", "title", "author", "read"]:
            if key not in data:
                raise ValueError(f"missing key {key}")

        return cls(
            id=data["id"], 
            title=data["title"], 
            author=data["author"], 
            read=data["read"]
        )
