import pytest
import geobr
from time import time
from geobr.utils import check_year
import pandas as pd
@pytest.fixture
def metadata_file():
    return geobr.utils.download_metadata()

def test_download_metadata(metadata_file):

    # Check if it fails if it doesn't find a file
    with pytest.raises(Exception):
        geobr.utils.download_metadata(
            url='http://www.ipea.gov.br/geobr/metadata/met')

    # Check if columns are the same
    assert (['geo', 'year', 'code', 'download_path', 'code_abrev'] == \
            metadata_file.columns).all()

    # Check if it has content
    assert len(metadata_file) > 0

def test_download_metadata_cache():
    
    # Check if cache works
    start_time = time()
    geobr.utils.download_metadata()
    assert time() - start_time < 1

def test_check_year(): 
    metadata = pd.DataFrame([2004,2019],columns=["year"]) 
    assert check_year(None, metadata) == 2019
    assert check_year(2004, metadata) == 2004
    with pytest.raises(Exception):
       assert check_year(2006, metadata) == 2004