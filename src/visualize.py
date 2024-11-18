import plotly.graph_objects as go
from coordinates import get_sky_coords

def visualize_sky_map(df, x, y, z):
    """
    Create an interactive 3D star map with a slider to filter by magnitude.
    """
    min_mag = int(df['phot_g_mean_mag'].min())
    max_mag = int(df['phot_g_mean_mag'].max())
    traces = []

    # Create a trace for each magnitude step
    for mag_limit in range(min_mag, max_mag + 1):
        filtered_df = df[df['phot_g_mean_mag'] <= mag_limit]
        filtered_x, filtered_y, filtered_z = get_sky_coords(filtered_df)

        traces.append(go.Scatter3d(
            x=filtered_x,
            y=filtered_y,
            z=filtered_z,
            mode='markers',
            marker=dict(
                size=2,
                color=filtered_df['phot_g_mean_mag'],
                colorscale='Viridis',
                opacity=0.8
            ),
            text=[f"RA: {ra:.2f}<br>Dec: {dec:.2f}<br>Mag: {mag:.2f}"
                  for ra, dec, mag in zip(filtered_df['ra'], filtered_df['dec'], filtered_df['phot_g_mean_mag'])],
            hoverinfo='text',
            visible=(mag_limit == min_mag)
        ))

    # Create slider steps
    slider_steps = []
    for i, mag_limit in enumerate(range(min_mag, max_mag + 1)):
        step = {
            "method": "update",
            "args": [
                {"visible": [i == idx for idx in range(len(traces))]},
                {"title": f"Stars with Magnitude <= {mag_limit}"}
            ],
            "label": str(mag_limit)
        }
        slider_steps.append(step)

    # Create the figure
    fig = go.Figure(data=traces)
    fig.update_layout(
        sliders=[{
            "active": 0,
            "currentvalue": {"prefix": "Magnitude ≤ ", "font": {"size": 20}},
            "steps": slider_steps
        }],
        title="Interactive 3D Star Map with Magnitude Slider",
        scene=dict(
            xaxis_title='X (pc)',
            yaxis_title='Y (pc)',
            zaxis_title='Z (pc)'
        )
    )

    # Show the figure
    fig.show()
