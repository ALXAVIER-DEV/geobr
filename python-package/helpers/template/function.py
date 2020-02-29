
from geobr.utils import select_metadata, download_gpkg


def {{ name }}(year={{ default_year }}, tp='simplified', verbose=False):
    """{{ first_liner }}
    
    {{ documentation }}

    Parameters
    ----------
    year : int, optional
        Year of the data, by default {{ default_year }}
    tp : str, optional
        Data 'type', indicating whether the function returns the 'original' dataset 
        with high resolution or a dataset with 'simplified' borders (Default)
    verbose : bool, optional
        by default False
    
    Returns
    -------
    gpd.GeoDataFrame
        Metadata and geopackage of selected states
    
    Raises
    ------
    Exception
        If parameters are not found or not well defined

    Example
    -------
    >>> from geobr import {{ name }}

    # Read specific state at a given year
    >>> df = {{ name }}(year={{ default_year }})
    """

    metadata = select_metadata('{{ metadata_key }}', year=year, data_type=tp)

    gdf = download_gpkg(metadata)

    return gdf
