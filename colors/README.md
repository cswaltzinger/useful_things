# Java Colorful Output Demo

The **Java Colorful Output Demo** is a simple Java class designed to introduce you to the exciting world of colored and styled terminal output. This class demonstrates how to use ANSI escape codes to enhance your console applications with colorful text and backgrounds.

## Getting Started

### Prerequisites

Make sure you have the following:

- Java Development Kit (JDK) installed on your system.

### Usage

1. Clone or download the repository

2. Navigate to the repository directory:

3. Compile the Java class:

    ```bash
    javac color.java
    ```

4. Run the Java class:

    ```bash
    java color
    ```

5. Observe the colorful numbers and background printed to your terminal!

## Understanding the Code

The `color` class showcases various ways to apply colors and styles to your terminal output using ANSI escape codes. 

Feel free to explore and modify the code to suit your preferences and needs. Refer to the comments within the code for a detailed explanation of each method.

## ANSI Escape Codes

This demo utilizes ANSI escape codes for text formatting. Here's a quick reference:

- **Colors:**
  - Black: `"\u001B[30m"`
  - Red: `"\u001B[31m"`
  - Green: `"\u001B[32m"`
  - Yellow: `"\u001B[33m"`
  - Blue: `"\u001B[34m"`
  - Magenta: `"\u001B[35m"`
  - Cyan: `"\u001B[36m"`
  - White: `"\u001B[37m"`

- **Background Colors:**
  - Black: `"\u001B[40m"`
  - Red: `"\u001B[41m"`
  - Green: `"\u001B[42m"`
  - Yellow: `"\u001B[43m"`
  - Blue: `"\u001B[44m"`
  - Magenta: `"\u001B[45m"`
  - Cyan: `"\u001B[46m"`
  - White: `"\u001B[47m"`

- **Styles:**
  - Reset: `"\u001B[0m"`
  - Bold: `"\u001B[1m"`
  - Italic: `"\u001B[3m"`
  - Underline: `"\u001B[4m"`
