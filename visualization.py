# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from nature_style_plt import setup_nature_style

def plot_emg_signals(emg_data, file_counter):
    """
    绘制EMG信号图。

    Args:
        emg_data (pd.DataFrame): 提取并处理后的EMG数据。
        file_counter (int): 文件编号计数器，用于图表标题。
    """
    # 设置Nature期刊样式
    setup_nature_style()
    
    # 选择需要绘制的EMG信号列
    emg_columns_to_plot = ['LDe', 'RDe', 'LTA', 'RTA', 'LRA', 'RRA', 'LTi', 'RTi', 
                          'LGa', 'RGa', 'LRF', 'RRF', 'LES', 'RES', 'LMu', 'RMu']

    # 创建一个图形和多个子图
    fig, axes = plt.subplots(len(emg_columns_to_plot), 1, 
                            figsize=(3.5, 2.625 * len(emg_columns_to_plot)))

    # 遍历每个需要绘制的EMG信号列
    for i, column in enumerate(emg_columns_to_plot):
        axes[i].plot(emg_data['time'], emg_data[column])
        axes[i].set_title(f'C{file_counter} - {column}')
        axes[i].set_xlabel('Time (s)')
        axes[i].set_ylabel('EMG Amplitude')

    # 调整子图之间的间距
    plt.tight_layout()

    # 显示图形
    plt.show()

def plot_emg_nature_style(emg_data, subject_id, save_path=None):
    """
    Plot EMG signals in Nature journal style with individual y-axis scaling
    """
    # Set up style
    setup_nature_style()
    
    # Create figure
    fig, axes = plt.subplots(8, 2, figsize=(7.2, 10))
    
    # Muscle pairs and their full names
    muscle_pairs = [
        ('LDe', 'RDe', 'Deltoid'),
        ('LTA', 'RTA', 'Tibialis Anterior'),
        ('LRA', 'RRA', 'Rectus Abdominis'),
        ('LTi', 'RTi', 'Tibialis'),
        ('LGa', 'RGa', 'Gastrocnemius'),
        ('LRF', 'RRF', 'Rectus Femoris'),
        ('LES', 'RES', 'Erector Spinae'),
        ('LMu', 'RMu', 'Multifidus')
    ]
    
    from matplotlib.ticker import ScalarFormatter
    class CustomScalarFormatter(ScalarFormatter):
        def _set_format(self):
            self.format = "%1.1e"
    
    # Plot each muscle pair
    for i, (left, right, muscle_name) in enumerate(muscle_pairs):
        # Calculate y-axis limits for this muscle pair
        left_data = emg_data[left]
        right_data = emg_data[right]
        
        # Get min and max for this pair
        pair_min = min(left_data.min(), right_data.min())
        pair_max = max(left_data.max(), right_data.max())
        
        # Add margin to y-axis limits (5% of data range)
        y_range = pair_max - pair_min
        y_margin = y_range * 0.05
        y_limits = (pair_min - y_margin, pair_max + y_margin)
        
        # Left muscle
        ax_left = axes[i, 0]
        ax_left.plot(emg_data['time'], left_data,
                    color='#2F5597',
                    linewidth=0.5)
        ax_left.set_title(f'Left {muscle_name}', pad=5)
        ax_left.set_ylim(y_limits)
        
        # Add amplitude scale
        scale_text = f'{y_range:.1e} mV'
        ax_left.text(0.02, 0.95, scale_text,
                    transform=ax_left.transAxes,
                    verticalalignment='top',
                    fontsize=7)
        
        # Right muscle
        ax_right = axes[i, 1]
        ax_right.plot(emg_data['time'], right_data,
                     color='#2F5597',
                     linewidth=0.5)
        ax_right.set_title(f'Right {muscle_name}', pad=5)
        ax_right.set_ylim(y_limits)
        
        # Add amplitude scale
        ax_right.text(0.02, 0.95, scale_text,
                     transform=ax_right.transAxes,
                     verticalalignment='top',
                     fontsize=7)
        
        # Set common properties for both axes
        for ax in [ax_left, ax_right]:
            ax.set_xlabel('Time (s)')
            ax.set_ylabel('EMG (mV)')
            ax.tick_params(direction='out', length=2, width=0.5)
            ax.grid(True, linestyle='--', alpha=0.5, linewidth=0.5)
            
            # Format y-axis ticks using scientific notation
            formatter = CustomScalarFormatter()
            formatter.set_scientific(True)
            formatter.set_powerlimits((-3, 4))
            ax.yaxis.set_major_formatter(formatter)
            
            # Add zero line
            ax.axhline(y=0, color='k', linestyle='-', linewidth=0.3, alpha=0.3)
    
    # Add main title
    fig.suptitle(f'Subject {subject_id} - Raw EMG Signals',
                 fontsize=9, y=0.98)
    
    # Adjust layout
    plt.tight_layout(rect=[0, 0, 1, 0.98])
    
    # Save figure
    if save_path:
        plt.savefig(save_path,
                   format='tiff',
                   dpi=300,
                   bbox_inches='tight',
                   pad_inches=0.1)
        print(f"Figure saved: {save_path}")
    
    plt.show()

