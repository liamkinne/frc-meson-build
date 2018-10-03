#!/usr/bin/env python3

import urllib.request
import re
import os.path
import wget
import subprocess

wpilib_folder = os.environ['MESON_BUILD_ROOT'] + '/wpilib/'
plugins_page_url = 'http://first.wpi.edu/FRC/roborio/release/eclipse/plugins/'

def get_full_path(name):
	return os.environ['MESON_BUILD_ROOT'] + '/' + name 

def download_package(url, name):
	if os.path.isfile(get_full_path(name)) == False:
		print('Downloading Core Plugin...')
		wget.download(url, out='build/' + name)
		print()
	else:
		print('Already Downloaded: {} '.format(name))

def extract_package(name):
	print('Extracting {}'.format(name))
	subprocess.call(['mkdir','--parents', wpilib_folder])
	subprocess.call(['unzip', '-qo', get_full_path(name), '-d',  wpilib_folder + name])

def get_latest_version():
	plugins_page = urllib.request.urlopen(plugins_page_url);
	plugins_page_content = plugins_page.read().splitlines()

	versions = []
	for line in plugins_page_content:
		match = re.match(r'^.*wpilib.plugins.cpp_(.*).jar.*$', str(line), re.M|re.I)
		if match:
			versions.append(match.group(1))

	if not versions:
		raise Exception('Failed to parse and find any versions')

	return versions[-1]


version_latest = get_latest_version();

core_filename = 'edu.wpi.first.wpilib.plugins.core_{}.jar'.format(version_latest)
cpp_filename = 'edu.wpi.first.wpilib.plugins.cpp_{}.jar'.format(version_latest)

print('Found Core Plugin: {}'.format(core_filename))
print('Found C++ Plugin: {}'.format(cpp_filename))

download_package(plugins_page_url + core_filename, core_filename)
extract_package(core_filename)

subprocess.call(['unzip', '-qo', wpilib_folder + core_filename + '/resources/common.zip', '-d', wpilib_folder])
subprocess.call(['rm', '-r', wpilib_folder + core_filename])

download_package(plugins_page_url + cpp_filename, cpp_filename)
extract_package(cpp_filename)

subprocess.call(['unzip', '-qo', wpilib_folder + cpp_filename + '/resources/cpp.zip', '-d', wpilib_folder])
subprocess.call(['rm', '-r', wpilib_folder + cpp_filename])
