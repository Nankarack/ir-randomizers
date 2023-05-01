import ir_datasets
from ir_datasets.formats import JsonlDocs, TrecXmlQueries
from typing import NamedTuple
from ir_datasets.datasets.base import Dataset

class IrAnthologyDocument(NamedTuple):
    doc_id: str
    text: str
    
    def default_text(self):
        return self.text

ir_datasets.registry.register('iranthology-randomizers', Dataset(
    JsonlDocs(ir_datasets.util.PackageDataFile(path='datasets_in_progress/ir-anthology-processed.jsonl'), doc_cls=IrAnthologyDocument, lang='en'),
    TrecXmlQueries(ir_datasets.util.PackageDataFile(path='datasets_in_progress/topics.xml'), lang='en')
))
