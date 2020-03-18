from dataclasses import dataclass, field
from typing import List

from dataclasses_json import DataClassJsonMixin

from frater.data.category import Category


@dataclass
class Dataset(DataClassJsonMixin):
    name: str = ''
    labels: List[str] = field(default_factory=list)

    def __getitem__(self, item: int):
        return self.get_category(item)

    def __len__(self):
        return len(self.labels)

    def get_category(self, index):
        return Category(index, self.labels[index], self.name)

    def get_category_by_label(self, label):
        index = self.labels.index(label)
        return self.get_category(index)
