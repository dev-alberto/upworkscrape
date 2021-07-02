import os
import json
from pydantic import BaseModel

class Target(BaseModel):

    def serialize(self, file_name):
        """
        serialize object and store in pickle file
        """
        # name dir as datetime.now()
        if not os.path.exists('jsons'):
            os.makedirs('jsons')
        with open("jsons/" + file_name + '.json', 'w') as f:
            json.dump(self, f)
