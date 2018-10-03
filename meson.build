project(
	'frc',
	'cpp'
)

# Project Subdirectories
commands = include_directories('src/Commands')
subsystems = include_directories('src/Subsystems')

# WPILib
include = include_directories('wpilib/include')
wpi_inc = include_directories('wpilib/lib/linux/athena/shared/')
wpi_ref_inc = include_directories('wpilib/reflib/linux/athena/shared/')
wpi_lib = static_library('wpi', include_directories: wpi_inc)
wpi_dep = declare_dependency(
	include_directories: [
		wpi_inc,
		wpi_ref_inc,
	],
	link_with: wpi_lib
)

executable(
	'FRCUserProgram',
	'src/Robot.cpp',
	include_directories: [
		commands,
		subsystems,
		include
	],
	dependencies: [
		wpi_dep
	]
)

run_target('update_wpilib',
	command: ['scripts/install-wpilib.py']
)

meson.add_postconf_script('scripts/install-wpilib.py')