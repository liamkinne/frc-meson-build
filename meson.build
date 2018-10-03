project(
	'frc',
	'cpp'
)

# Project Subdirectories
commands = include_directories('src/Commands')
subsystems = include_directories('src/Subsystems')

# WPILib Directories
include = include_directories('build/wpilib/include')
lib = include_directories('build/wpilib/lib/linux/athena/shared/')
reflib = include_directories('build/wpilib/reflib/linux/athena/shared/')

executable(
	'FRCUserProgram',
	'src/Robot.cpp',
	include_directories: [
		commands,
		subsystems,
		include,
		lib,
		reflib
	]
)

run_target('update_wpilib',
	command: ['scripts/install-wpilib.py']
)

meson.add_postconf_script('scripts/install-wpilib.py')