import yaml

verbose = 2
with open(r'/home/your_name/Desktop/Multi-View-Foams/config_paths.yaml') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)
    data_dir = config['data_dir']
    full_groups_dir = config['full_groups_dir']
    preprocess_dir = config['preprocess_dir']
    models2_dir = config['models2_dir']
