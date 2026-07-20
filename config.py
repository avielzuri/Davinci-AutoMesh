# --- Directories ---
# Folder containing the STEP/IGES files to process
INPUT_DIR = "CAD_INPUTS"
# Folder where successful Pointwise projects will be saved
OUTPUT_DIR = "MESH_OUTPUTS"

# --- Pointwise Connection ---
# The port your Glyph Server is actively listening on
PW_PORT = 2807

# --- Meshing Parameters ---
# The exact name of the CAD boundary/surface to extract and mesh
TARGET_ENTITY = "Combine2"
# The default isotropic grid spacing for the domain
DEFAULT_SPACING = 0.3