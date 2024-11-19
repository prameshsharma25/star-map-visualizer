from star import get_star_data
from coordinates import project_to_sky
from visualize import plot_star_map

def main():
    query = """
    SELECT TOP 5000
        ra, dec, parallax, phot_g_mean_mag
    FROM gaiadr3.gaia_source
    WHERE parallax > 1
    ORDER BY phot_g_mean_mag ASC
    """
    
    df = get_star_data(query)
    plot_star_map(df, max_star_size=50, zoom_factor=1.5)

if __name__ == "__main__":
    main()
