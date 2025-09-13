from pydantic import BaseModel
from typing import List, Optional


class ImageQuery(BaseModel):
    image_query: str