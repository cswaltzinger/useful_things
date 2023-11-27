# Bash Scripts Repository

Welcome to the Bash Scripts Repository! This collection of scripts aims to provide handy tools and utilities to streamline various tasks in a Unix-like environment. Feel free to explore and use these scripts to enhance your workflow.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Scripts Overview](#scripts-overview)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

Make sure you have the following prerequisites installed:

- Bash (GNU Bash recommended)
- Unix-like operating system (Linux, macOS, WSL on Windows)

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/bash-scripts.git
   ```

2. **Navigate to the Repository:**
   ```bash
   cd bash-scripts
   ```

3. **Explore and Use:**
   Browse through the scripts and use them as needed.

## Scripts Overview

- **Script 1: `assembleAndLink.sh`**
  - uses builtin `as` and `ld` functions to assemble and link an executable, then run if successful.
  - EX:
  ```bash
  /home/user: asembleAndLink.sh hello_world
  Hello World
  /home/user: ls 
  hello_world
  hello_world.s
  hello_world.o
  /home/user: 
  ```

- **Script 2: `bashrc`**
  - This script is my own .bashrc files that contain aliases and functions I have found useful.
  - To use it as your own, you need to add everything in the file to your `~/.bashrc` file 

- **Script 2: `gu`**
  - This script is a git util file to execute multiple git commands across a folder of repositories
  - To run this file:
     1) simply move it into the folder of repositories
     2) execute the following code to ensure you can run the `gu` file:
     ```bash 
     chmod u+x gu
     ```
     3) run the following command where $YOUR_COMMAND is the corresponding git command you wish to run.  
     ```bash
     ./gu $YOUR_COMMAND
     ```
     NOTE: if there is not a git command defined that you want to run, simply use the it function similar to the following code 
     ```bash
     ./gu it $YOUR_COMMAND
     ```
     For example, to get the remote repository URL for each repository, you could run:
     ```bash
     ./gu it git remote -v 
     ```

...
