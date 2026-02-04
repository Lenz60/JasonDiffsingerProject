import os
import shutil

def rename_and_duplicate_files():
    """
    Creates duplicates of .lab files with _+1 and _norm suffixes, keeping .lab extension.
    Special case: ballade01 uses _-1 instead of _+1
    """
    
    # List of source files (with .lab extension)
    source_files = [
        "ballade01.lab",
        "desperate1.lab",
        "desperate2.lab",
        "desperate3.lab",
        "desperate4.lab",
        "desperate5.lab",
        "desperate6.lab",  # Note: This has a Cyrillic 'б' character
        "divergence1.lab",
        "divergence2.lab",
        "divergence3.lab",
        "divergence4.lab",
        "itoshi1.lab",
        "itoshi2.lab",
        "itoshi3.lab",
        "itoshi4.lab",
        "itoshi5.lab",
        "itoshi6.lab",
        "sumire1.lab",
        "sumire2.lab",
        "sumire3.lab",
        "sumire4.lab",
        "toika1.lab",
        "troika2.lab",
        "troika3.lab",
        "tsubasa1.lab",
        "tsubasa2.lab",
        "tsubasa3.lab",
        "tsubasa4.lab",
        "tsubasa5.lab"
    ]
    
    # Track successful and failed operations
    success_count = 0
    failed_files = []
    
    for source_file in source_files:
        try:
            # Check if source file exists
            if not os.path.exists(source_file):
                print(f"Warning: {source_file} not found, skipping...")
                failed_files.append(source_file)
                continue
            
            # Get base name without extension
            base_name = os.path.splitext(source_file)[0]
            
            # Determine the prefix for the first duplicate
            # Special case for ballade01
            if base_name == "ballade01":
                prefix1 = "_-1"
            else:
                prefix1 = "_+1"
            
            # Define target filenames (keeping .lab extension)
            file1 = f"{base_name}{prefix1}.lab"
            file2 = f"{base_name}_norm.lab"
            
            # Copy source file to create duplicates with new names
            shutil.copy2(source_file, file1)
            shutil.copy2(source_file, file2)
            
            # Delete the original file
            os.remove(source_file)
            
            print(f"✓ {source_file} -> {file1}")
            print(f"✓ {source_file} -> {file2}")
            print(f"✓ Deleted: {source_file}")
            success_count += 2
            
        except Exception as e:
            print(f"Error processing {source_file}: {str(e)}")
            failed_files.append(source_file)
    
    # Summary
    print("\n" + "="*50)
    print(f"Summary:")
    print(f"  Successfully created: {success_count} files")
    if failed_files:
        print(f"  Failed files: {len(failed_files)}")
        for f in failed_files:
            print(f"    - {f}")
    print("="*50)

if __name__ == "__main__":
    print("Starting file duplication process...\n")
    rename_and_duplicate_files()
    print("\nProcess completed!")