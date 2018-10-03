project(
	'frc',
	'cpp'
)

# Project Subdirectories
commands = include_directories('src/Commands')
subsystems = include_directories('src/Subsystems')

executable(
	'FRCUserProgram',
	'src/Robot.cpp',
	include_directories: [
		commands,
		subsystems
	]
)

run_target('update_wpilib',
	command: ['scripts/install-wpilib.py']
)

meson.add_postconf_script('scripts/install-wpilib.py')