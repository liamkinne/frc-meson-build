#!/usr/bin/env python3

import urllib.request
import re
import os.path
import wget
import subprocess

def get_full_path(name):
	return os.environ['MESON_BUILD_ROOT'] + '/' + name 

def download_package(url, name):
	if os.path.isfile(get_full_path(name)) == False:
		print('Downloading Core Plugin...')
		#wget.download(url, out='build/' + name)
		print()
	else:
		print('{} Already Downloaded'.format(name))

def extract_package(name):
	print('Extracting {}'.format(name))
	subprocess.call(['mkdir','--parents', os.environ['MESON_BUILD_ROOT'] + '/wpilib/'])
	subprocess.call(['unzip', '-qo', get_full_path(name), '-d',  os.environ['MESON_BUILD_ROOT'] + '/wpilib/' + name])

plugins_page_url = 'http://first.wpi.edu/FRC/roborio/release/eclipse/plugins/'
plugins_page = urllib.request.urlopen(plugins_page_url);
plugins_page_content = plugins_page.read().splitlines()

versions = []
for line in plugins_page_content:
	match = re.match(r'^.*wpilib.plugins.cpp_(.*).jar.*$', str(line), re.M|re.I)
	if match:
		versions.append(match.group(1))

if not versions:
	raise Exception('Failed to parse and find versions')

version_latest = versions[-1]

core_filename = 'edu.wpi.first.wpilib.plugins.core_{}.jar'.format(version_latest)
cpp_filename = 'edu.wpi.first.wpilib.plugins.cpp_{}.jar'.format(version_latest)

core_url = plugins_page_url + core_filename
cpp_url = plugins_page_url + cpp_filename

print('Found Core Plugin: {}'.format(core_url))
print('Found C++ Plugin: {}'.format(cpp_url))

download_package(core_url, core_filename)
download_package(cpp_url, cpp_filename)