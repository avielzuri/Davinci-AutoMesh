import os
import glob
import config
from pointwise import GlyphClient

# Ensure our directories exist before we start
os.makedirs(config.INPUT_DIR, exist_ok=True)
os.makedirs(config.OUTPUT_DIR, exist_ok=True)

print(f"Connecting to Pointwise Glyph Server on port {config.PW_PORT}...")
glf = GlyphClient(port=config.PW_PORT) 
pw = glf.get_glyphapi()

# Grab ALL files from the input directory (STEP, IGES, Parasolid, etc.)
cad_files = [f for f in glob.glob(f"{config.INPUT_DIR}/*") if os.path.isfile(f)]

if not cad_files:
    print(f"No files found in '{config.INPUT_DIR}'. Exiting.")
    exit()

print(f"Found {len(cad_files)} files to process.")

for file_path in cad_files:
    filename = os.path.basename(file_path)
    base_name = os.path.splitext(filename)[0]
    
    print(f"\n--- Processing: {filename} ---")
    
    # Reset Pointwise session for a clean slate per file
    pw.Application.reset()
    
    try:
        abs_file_path = os.path.abspath(file_path)
        with pw.Application.begin("DatabaseImport") as importer:
            importer.initialize(abs_file_path, strict=True, type="Automatic")
            importer.read()
            importer.convert()
            
        pw.Connector.setCalculateDimensionMethod("Spacing")
        pw.Connector.setCalculateDimensionSpacing(config.DEFAULT_SPACING)
        pw.Application.setGridPreference("Unstructured")
        
        # Extract the target entity defined in the config.py file
        db_entity = pw.DatabaseEntity.getByName(config.TARGET_ENTITY) 
        
        domains = pw.DomainUnstructured.createOnDatabase(
            [db_entity], 
            parametricConnectors="Aligned", 
            merge=0
        )
        
        print(f"Generated {len(domains)} unstructured domains on '{config.TARGET_ENTITY}'.")
        
        # Save the successful meshing setup to the output folder
        output_pw_path = os.path.abspath(os.path.join(config.OUTPUT_DIR, f"{base_name}.pw"))
        pw.Application.save(output_pw_path)
        print(f"Saved mesh project to: {output_pw_path}")

    except Exception as e:
        # If the target entity is missing or the mesh fails, catch it and move on
        print(f"ERROR on {filename}: {e}")
        print("Skipping to the next file...")

print("\nBatch run complete!")