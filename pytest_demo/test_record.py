import records
from collections import namedtuple
IdRecord = namedtuple('IdRecord', 'id')
def check_id(i, row):
    assert row.id == i
class TestRecordCollection():
    def test_iter(self):
        rows = records.RecordCollection(IdRecord(i) for i in range(10))
        for i, row in enumerate(rows):
            check_id(i, row)
