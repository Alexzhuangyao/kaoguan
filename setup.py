import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {'packages': ['PyQt5','sys','time'], 'excludes': []}

setup(  name = 'kaoguan',
        version = '1.0.0',
        description = '',
        options = {'build_exe': build_exe_options},
        executables = [Executable('main1.py')])