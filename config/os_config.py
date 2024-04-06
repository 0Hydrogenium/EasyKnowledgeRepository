from pathlib import Path
import os


# 初始化全局根目录
def init_working_directory():
    file = Path(__file__).resolve()
    project_dir = os.path.dirname(os.path.dirname(file))

    os.chdir(Path(project_dir))
