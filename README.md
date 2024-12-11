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
