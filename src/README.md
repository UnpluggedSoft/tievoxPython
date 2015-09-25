# shutdown.py

## Introduction

## Usage

## Installing into Crontab
To install TIEVox Python scripts, you simply add on line to root's crontab.
	sudo crontab -e

At the bottom of the file, add this line:
	@reboot				%PATH_TO_tievoxPython%/src/startup.sh

