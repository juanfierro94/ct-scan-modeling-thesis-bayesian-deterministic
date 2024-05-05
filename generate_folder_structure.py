import os

def generate_folder_structure(root_dir):
    # Define folder structure
    folders = {
        'data': 'Directory for storing CT scan data',
        'models': 'Directory for storing trained models',
        'notebooks': 'Jupyter notebooks for experimentation and analysis',
        'scripts': 'Python scripts for model training, evaluation, and visualization',
        'utils': 'Utility functions and helper scripts\nThis folder stores images and other results generated during the analysis.'
    }
    
    # Create folders and README files
    for folder, description in folders.items():
        folder_path = os.path.join(root_dir, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        with open(os.path.join(folder_path, 'README.md'), 'w') as readme_file:
            readme_file.write(f'# {folder.capitalize()}\n\n{description}\n')

if __name__ == '__main__':
    generate_folder_structure(os.getcwd())  # Use current working directory as the root directory
