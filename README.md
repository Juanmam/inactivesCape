# InactivesCape

## About

This is a small program to help find inactive listings from Airbnb, Vrbo and Homeaway in a given spreadsheet. To be able to run the program, you will need to set up the web drivers as described in the installation section of this program, plus use some python package manager to install Selenium. For instructions on how to use the program, refer to the Usage section in this document.

## Installation

In order to use InactiveCape, you will need to install Selenium, download the drivers and set the path for those drivers.

### Selenium

In order to install Selenium, you will need a python package manager, pip or anaconda will do, but you can always go and install it manually by downloading the project from the official git page [here](https://github.com/SeleniumHQ/selenium). If you want to do it via console commands, the following will do and will take much less time and effort. For those using pip or pip3 (We highly recommend using pip3).

    pip3 install -U selenium

For Anaconda fans, you can always use the GUI or the following command.

    conda install -c conda-forge selenium

For those that are going the manual route, open your terminal, go to the projects folder, there will be a py folder. Go inside and run the following command.

	python setup.py install

We discourage the use of this method, as it can cause troubles with paths later on.

### Drivers

Selenium works with multiple drivers, you will download a driver depending on your PC architecture, what browser you use and what version you have. There are multiple drivers, you can check them out in the subsection 1.3 [here](https://selenium-python.readthedocs.io/installation.html). Currently, the program uses Chrome as default, but there are some commented lines showing how to use Firefox and PhantomJS (A distribution based on Firefox that won't trigger headers).

### Path

After downloading a driver, move it inside the project into the folder named src/drivers. Make sure you don't change the name of the driver, as the library will try to find the driver by its name. Now we need to add the src/drivers folder to the path. The following links will help you understand how to add paths for [Windows](https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/), [Mac](https://www.architectryan.com/2012/10/02/add-to-the-path-on-mac-os-x-mountain-lion/) and [Linux](https://stackabuse.com/how-to-permanently-set-path-in-linux/) in case you are not sure of how to do so. At this point you should be able to run everything fine! If you find a problem, check your drivers version or post a issue on our git page [here](https://github.com/Juanmam/inactivesCape/issues).

## Usage

The program runs via terminal. If you are using Windows, execute the run.bat file. It will run the program for you. The following subsections will explain how to input data and get the output from the system.

### Input

- File name: is the name of the file you are going to analyze. Before running the program, make sure to add the input file (the spreadsheet) into the folder /io/input.

> Note: Just pass the name, not the file extension, so if you have file.xlsx, you just have to input file.

- Title Row: Is the row number where the titles are located. For example, if you have a spreadsheet and there is a header at row 1 and the column titles at row 2, you will input 2.

- Sheet Name: is the spreadsheet you have the data on.

> Note: Case-sensitive.

### Output

The program give three different outputs. The terminal will display when an inactive is found, with the row number and url. After the program finishes its execution, it will output two different files, a spreadsheet with the active/inactive listings and a report showing the same info from the terminal plus the modification date.
