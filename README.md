# Muscle Synergy Analysis for Low Back Pain (LBP)

This repository contains code for analyzing muscle synergies in individuals with and without low back pain (LBP) using surface electromyography (sEMG) data.

## Project Structure
Muscle-Synergy-Analysis-for-LBP/
├── data/
│   ├── raw_data/
│   │   └── (存放原始 CSV 数据文件，例如 C1_L.csv, C2_L.csv 等)
│   └── processed_data/
│       └── (存放处理后的 EMG 数据文件，例如 C1_LEMG.CSV, C2_LEMG.CSV 等)
├── figures/
│   └── nature_quality/
│       └── (存放生成的符合 Nature 期刊风格的图片，例如 C1_EMG_signals.tiff 等)
├── .gitignore
├── README.md
├── requirements.txt
├── data_loader.py
├── visualization.py
└── nature_style_plt.py

## Dependencies

The project requires the following Python libraries:

- pandas
- numpy
- matplotlib
- scipy
- scikit-learn
- filterpy
- seaborn

You can install these dependencies using pip:
bash
pip install -r requirements.txt

## Usage

1. **Data Preparation:**
    *   Place the raw sEMG data files (e.g., `C1_L.csv`, `C2_L.csv`) in the `data/raw_data` directory. The raw data files should be CSV files with a specific format (see `data_loader.py` for details).

2. **Data Loading and Processing:**
    *   The `data_loader.py` script is responsible for reading the raw data, extracting the EMG signals, and saving the processed data to the `data/processed_data` directory.
    *   Run `data_loader.py` to process the raw data:

    ```bash
    python data_loader.py
    ```

3. **Visualization:**
    *   The `visualization.py` script generates plots of the EMG signals.
    *   The `plot_emg_nature_style` function in `visualization.py` creates plots that conform to the style guidelines of the Nature journal.
    *   Figures are saved in the `figures/nature_quality` directory.

4. **Nature Style Settings:**
    *   The `nature_style_plt.py` script contains the `setup_nature_style` function, which configures Matplotlib to produce plots that adhere to Nature's style requirements.

## Data Source

The raw sEMG data used in this project is assumed to be located in the `D:\SEMG-EEG\SEMG-EEG raw\` directory. You may need to modify the `folder_pattern` variable in `data_loader.py` to match the location of your data.

## Notes

- The code currently processes data for subject "C1". You can modify the `counter` variable in `data_loader.py` to process data for other subjects.
- The Jupyter Notebook file (`sub-emg analysis.ipynb`) is not included in this project structure, as it was used for development and experimentation. The relevant code from the notebook has been extracted and organized into the Python files.

## Contributing

Contributions to this project are welcome. Please feel free to submit pull requests or open issues to suggest improvements or report bugs.

## License

This project is licensed under the [MIT License](LICENSE) (you can add a LICENSE file later if you choose to).
