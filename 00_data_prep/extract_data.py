import os
import pprint

from dotenv import load_dotenv
from netCDF4 import Dataset

# Set local data path (if applicable)
load_dotenv()
DATA_PATH = os.environ.get('DATA_PATH')

# Create netCDF4 Dataset from file
d = Dataset(DATA_PATH + 'precip_pentad_mean.nc', 'r')
print(d)
pprint.pprint(d.dimensions.values())
pprint.pprint(d.variables.values())
