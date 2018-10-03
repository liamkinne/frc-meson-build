# FRC Meson Build

## Building
	meson build --cross-file cross_file.txt

## Updating WPILib
After installing, you can also update the WPILib

	cd build
	ninja update_wpilib

## Requirements
- meson
- frc-toolchain

### Installing the FRC Toolchain (Linux)
	sudo add-apt-repository ppa:wpilib/toolchain

	sudo apt-get update

	sudo apt-get install frc-toolchain
