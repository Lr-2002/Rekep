import argparse
import yaml
from environment import ReKepOGEnv
from utils import get_config
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--scene",
        type=str,
        default="./configs/og_scene_file_only_cube.json",
        help="Path to the scene configuration file",
    )
    return parser.parse_args()

def main():
    args = parse_args()
    
    # Load base config
    global_config = get_config(config_path="./configs/config.yaml")
    # Create environment
    env = ReKepOGEnv(global_config["env"], args.scene)
    env.print_object_info('cube_1')   
    env.change_obj_mass('cube_1', mass=0.5)
    # Keep the environment visualization running
    while True:
        env._step()
        
if __name__ == "__main__":
    main()
