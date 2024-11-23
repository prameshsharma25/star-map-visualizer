import io
import matplotlib.pyplot as plt

from star import get_star_data
from visualize import plot_star_map
from flask import Flask, send_file, render_template


plt.switch_backend('Agg')

app = Flask(__name__)

def main():
    query = """
    SELECT TOP 5000
        ra, dec, parallax, phot_g_mean_mag
    FROM gaiadr3.gaia_source
    WHERE parallax > 1
    ORDER BY phot_g_mean_mag ASC
    """
    return get_star_data(query)

@app.route('/')
def home():
    return """
    <h1>3D Sky Map Generator</h1>
    <p>Click below to generate and download the sky map:</p>
    <a href="/download-sky-map" download="sky_map.png">
        <button>Download Sky Map</button>
    </a>
    """

@app.route('/download-sky-map')
def generate_image():
    df = main()

    fig, ax = plot_star_map(df, chart_size=10, max_star_size=50, zoom_factor=1.5)

    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', dpi=300)
    buf.seek(0)
    plt.close(fig)

    return send_file(
        buf,
        mimetype='image/png',
        as_attachment=True,
        download_name='sky_map.png'
    )

if __name__ == "__main__":
    app.run(debug=True)
