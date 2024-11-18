from star import get_star_data
from coordinates import get_sky_coords
from visualize import visualize_sky_map


def main():
    query = """
    SELECT TOP 5000
        ra, dec, parallax, phot_g_mean_mag
    FROM gaiadr3.gaia_source
    WHERE parallax > 1
    ORDER BY phot_g_mean_mag ASC
    """
    
    df = get_star_data(query)
    x, y, z = get_sky_coords(df)
    visualize_sky_map(df, x, y, z)

if __name__ == "__main__":
    main()
