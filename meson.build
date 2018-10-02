project(
	'frc',
	'cpp'
)

executable(
	'FRCUserProgram',
	'src/Robot.cpp',
)

run_target('download_wpilib',
	command: ['scripts/download-wpilib.py']
)

meson.add_postconf_script('scripts/download-wpilib.py')