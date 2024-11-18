from astroquery.gaia import Gaia

def get_star_data(query):
    """
    Fetch stellar data using the provided ADQL query and return as a pandas DataFrame.
    """
    job = Gaia.launch_job(query)
    stars = job.get_results()
    df = stars.to_pandas()
    return df
