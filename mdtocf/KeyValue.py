"""Key-Value Store Used for Caching

Used by ConfluencePublisher to save metadata related to the processing
of each markdown file, like: Confluence Page ID, Confluence Page Title
and XHTML Confluence Content SHA256.

"""
import json
import pickledb


class KeyValue():

    def __init__(self, db_path):
        self.db = pickledb.load(db_path, False)

    def keys(self):
        return [*self.db.getall()]

    def load(self, key):
        value = self.db.get(key)
        if value is False:
            return {'id': None, 'title': '', 'sha256': ''}
        else:
            return json.loads(value)

    def save(self, key, value):
        self.db.set(key, json.dumps(value))
        self.db.dump()

    def remove(self, key):
        self.db.rem(key)
        self.db.dump()
