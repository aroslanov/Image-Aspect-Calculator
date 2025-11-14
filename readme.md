# Image Aspect Ratio Calculator

This is a simple PyQt6 application to calculate and visualize aspect ratios. It allows you to input dimensions, select common aspect ratios, and drag-and-drop images to auto-fill dimensions. This project was inspired by [Andrew Hedges' Aspect Ratio Calculator](https://andrew.hedges.name/experiments/aspect_ratio/).

## Features

- Input custom dimensions to calculate aspect ratios.
- Select from a list of common aspect ratios.
- Drag and drop images to auto-fill dimensions.
- Option to round results to the nearest whole number.
- Visualize the aspect ratio result.

## Installation

### Using `requirements.txt`

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/aspect-ratio-calculator.git
    ```
2. Navigate to the project directory:
    ```bash
    cd aspect-ratio-calculator
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Without `requirements.txt`

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/aspect-ratio-calculator.git
    ```
2. Navigate to the project directory:
    ```bash
    cd aspect-ratio-calculator
    ```
3. Install the dependencies individually:
    ```bash
    pip install PyQt6 Pillow
    ```

## Usage

Run the application using the following command:
```bash
python aspect_ratio_calculator.py
```

### Run on Windows without console window
If you prefer to launch the GUI without a console window on Windows, use the provided batch file:

1. Make sure the project's virtual environment is created and dependencies are installed (or ensure `pythonw` is on your PATH).
2. Double-click `run_calculator_no_console.bat` in the repository root to start the GUI without opening a console window.
3. The batch attempts to use `.venv\Scripts\pythonw.exe` by default and falls back to a `pythonw` executable on the PATH if it's not available.

If you want to use the console for logging or debugging, run `python calc.py` instead.

## Dependencies

- Python 3.x
- PyQt6
- Pillow

## How to Use

1. **Input Dimensions:**
   - Enter the width (W1) and height (H1) to calculate their aspect ratio.
   - Optionally, enter the width (W2) or height (H2) to calculate the missing dimension based on the aspect ratio of W1 and H1.
   
2. **Select Common Ratios:**
   - Use the dropdown to select a common aspect ratio. This will auto-fill W1 and H1 with the selected ratio.

3. **Drag and Drop Images:**
   - Drag an image file into the designated area to auto-fill W1 and H1 with the image's dimensions.
   - A thumbnail of the image will be displayed.

4. **Rounding Option:**
   - Check the "Round results to the nearest whole number" checkbox if you prefer rounded results.

5. **Calculate Button:**
   - Click the "Calculate" button to compute the aspect ratio based on the provided dimensions.

## Example

1. Enter `1920` for W1 and `1080` for H1.
2. Click "Calculate" to see the aspect ratio `16:9`.
3. Optionally, enter a value for W2 or H2 to compute the missing dimension based on the aspect ratio.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.

## Acknowledgements

This project was inspired by [Andrew Hedges' Aspect Ratio Calculator](https://andrew.hedges.name/experiments/aspect_ratio/). Thank you for providing the original idea and calculations.
