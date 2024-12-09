import subprocess
import os


def clip_geotiff_with_geojson(input_tif, geojson_path, output_tif):
    """
    Clips a GeoTIFF using a GeoJSON file as the clipping boundary.

    Args:
        input_tif (str): Path to the input GeoTIFF file.
        geojson_path (str): Path to the GeoJSON file containing the clipping boundary.
        output_tif (str): Path to save the clipped GeoTIFF.

    Returns:
        None
    """
    try:
        # Ensure the input files exist
        if not os.path.exists(input_tif):
            raise FileNotFoundError(f"Input GeoTIFF not found: {input_tif}")
        if not os.path.exists(geojson_path):
            raise FileNotFoundError(f"GeoJSON file not found: {geojson_path}")

        # Clip the GeoTIFF using the GeoJSON
        clip_command = [
            "gdalwarp",
            "-cutline", geojson_path,  # Use the GeoJSON for clipping
            "-crop_to_cutline",  # Crop the output to the clipping boundary
            "-dstnodata", "0",  # Define no-data value
            input_tif,  # Input GeoTIFF
            output_tif  # Output clipped GeoTIFF
        ]
        subprocess.run(clip_command, check=True)

        print(f"Successfully clipped GeoTIFF. Output saved to {output_tif}")

    except subprocess.CalledProcessError as e:
        print(f"Error during clipping: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage
if __name__ == "__main__":
    # Paths
    input_tif = "merged_data/merged_data.tif"  # Replace with the path to your merged GeoTIFF
    geojson_path = "clipping.geojson"  # Replace with the path to your GeoJSON file
    output_tif = "merged_data/clipped_output.tif"  # Replace with the desired output path

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_tif), exist_ok=True)

    # Clip the GeoTIFF
    clip_geotiff_with_geojson(input_tif, geojson_path, output_tif)
