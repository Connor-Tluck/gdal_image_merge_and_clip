import os
import subprocess


def merge_geotiffs(input_folder, output_file):
    """
    Merges all GeoTIFF files in a folder into a single GeoTIFF.

    Args:
        input_folder (str): Path to the folder containing GeoTIFF files.
        output_file (str): Path to save the merged GeoTIFF file.

    Returns:
        None
    """
    try:
        # Get all .tif files in the folder
        tif_files = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.endswith(".tif")]

        if not tif_files:
            raise FileNotFoundError("No GeoTIFF files found in the specified folder.")

        # Merge the GeoTIFF files
        merge_command = ["gdal_merge.py", "-o", output_file, "-of", "GTiff"] + tif_files
        subprocess.run(merge_command, check=True)

        print(f"Successfully merged GeoTIFF files into {output_file}")

    except subprocess.CalledProcessError as e:
        print(f"Error during merging: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage
if __name__ == "__main__":
    input_folder = "unmerged_data"  # Replace with the path to your folder containing GeoTIFFs
    output_file = "merged_data/merged_data.tif"  # Replace with the desired output file path

    # Ensure the output folder exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    merge_geotiffs(input_folder, output_file)
