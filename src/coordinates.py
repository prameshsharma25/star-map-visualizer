import astropy.units as u
from astropy.coordinates import SkyCoord

def get_sky_coords(df):
    """
    Convert RA, Dec, and parallax from the DataFrame into Cartesian coordinates.
    """
    coords = SkyCoord(
        ra=df['ra'].values * u.degree,
        dec=df['dec'].values * u.degree,
        distance=(1000 / df['parallax'].values) * u.pc
    )
    return coords.cartesian.x.value, coords.cartesian.y.value, coords.cartesian.z.value
