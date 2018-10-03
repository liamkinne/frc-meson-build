project(
	'frc',
	'cpp'
)

executable(
	'FRCUserProgram',
	'src/Robot.cpp',
)

run_target('update_wpilib',
	command: ['scripts/install-wpilib.py']
)

meson.add_postconf_script('scripts/install-wpilib.py')