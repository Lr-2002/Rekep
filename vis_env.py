import argparse
import yaml
from environment import ReKepOGEnv
from utils import get_config
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--scene",
        type=str,
        default="./configs/og_scene_file_cabinet.json",
        help="Path to the scene configuration file",
    )
    return parser.parse_args()

def main():
    args = parse_args()
    
    # Load base config
    global_config = get_config(config_path="./configs/config.yaml")
    # Create environment
    env = ReKepOGEnv(global_config["env"], args.scene)
    
    # Keep the environment visualization running
    while True:
        env._step()
        
if __name__ == "__main__":
    main()
