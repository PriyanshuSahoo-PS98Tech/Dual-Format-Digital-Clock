# ⏰ Dual Format Digital Clock - Python Tkinter

A sleek, modern digital clock application built with Python's Tkinter GUI framework that displays the current time in both 12-hour and 24-hour formats simultaneously. This elegant, dark-themed clock features real-time updates and clean typography, making it perfect for desktop use, presentations, or as a learning project for GUI development.

<div align="center"> <img src="https://github.com/PriyanshuSahoo-PS98Tech/Dual-Format-Digital-Clock/blob/main/output.png" alt="Dual Format Digital Clock" width="250"> </div>

## 📋 Table of Contents

- [Features](#-features)
- [Technologies Used](#️-technologies-used)
- [Project Structure](#-project-structure)
- [Installation & Setup](#-installation--setup)
- [Usage Instructions](#-usage-instructions)
- [Technical Implementation](#️-technical-implementation)
  - [Real-Time Updates](#real-time-updates)
  - [GUI Architecture](#gui-architecture)
  - [Time Formatting](#time-formatting)
- [Customization Guide](#-customization-guide)
- [System Requirements](#-system-requirements)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)
- [Acknowledgments](#-acknowledgments)

## ✨ Features

### **Dual Time Display**
- **🕐 12-Hour Format**: Traditional AM/PM time display with elegant formatting
- **🕓 24-Hour Format**: Military/International time format for global accessibility
- **⏱️ Real-Time Updates**: Clock updates every second with precise system time synchronization

### **Visual Design**
- **🎨 Modern Dark Theme**: Elegant black background reduces eye strain
- **🌈 Color-Coded Headers**: 
  - **Deep Sky Blue**: 12-hour format header for easy identification
  - **Lawn Green**: 24-hour format header for clear distinction
- **📱 Clean Typography**: Large, bold Arial font for maximum readability
- **✨ Professional Layout**: Centered design with optimal spacing and padding

### **Technical Excellence**
- **⚡ Lightweight**: Minimal resource usage with efficient update cycles
- **🖥️ Cross-Platform**: Runs on Windows, macOS, and Linux systems
- **🔄 Automatic Updates**: Self-refreshing display without manual intervention
- **💾 No Dependencies**: Uses only Python standard library modules

## 🛠️ Technologies Used

- **Python 3.x**: Core programming language
- **Tkinter**: Built-in GUI framework for desktop applications
- **Time Module**: System time retrieval and formatting
- **Standard Library**: No external dependencies required

## 📁 Project Structure

```
Dual-Format-Digital-Clock/
├── Dual_Format_Digital_Clock.py      # Main application file
├── output.png                        # Application screenshot
├── README.md                         # Project documentation
└── LICENSE                           # Project license
```

## 🔧 Installation & Setup

### **Prerequisites**
- Python 3.6 or higher
- Tkinter (usually pre-installed with Python)

### **Installation Steps**

**Method 1: Direct Download**
```bash
# Download the Dual_Format_Digital_Clock.py file
# No additional packages required
```

**Method 2: Clone Repository**
```bash
# Clone the repository
git clone https://github.com/PriyanshuSahoo-PS98Tech/Dual-Format-Digital-Clock.git

# Navigate to project directory
cd Dual-Format-Digital-Clock
```

### **Running the Clock**
```bash
# Execute the digital clock
python Dual_Format_Digital_Clock.py

# Alternative command for some systems
python3 Dual_Format_Digital_Clock.py
```

## 📖 Usage Instructions

### **Starting the Application**
1. **Run** the Python script using the command above
2. **View** both time formats displayed simultaneously
3. **Observe** automatic updates every second
4. **Close** the window to exit the application

### **Time Display Formats**
- **12-Hour Format**: `HH:MM:SS AM/PM` (e.g., 05:02:00 PM)
- **24-Hour Format**: `HH:MM:SS` (e.g., 17:02:00)

## 🏗️ Technical Implementation

### **Real-Time Updates**
The clock uses Tkinter's `after()` method for precise timing:

```python
def update_clock():
    format_12_hour = time.strftime("%I:%M:%S %p")  # 12-hour format
    format_24_hour = time.strftime("%H:%M:%S")     # 24-hour format
    
    # Update display labels
    lbl_12.config(text=format_12_hour)
    lbl_24.config(text=format_24_hour)
    
    # Schedule next update in 1000ms (1 second)
    window.after(1000, update_clock)
```

### **GUI Architecture**
- **Main Window**: Tkinter Tk() instance with black background
- **Label Widgets**: Four labels for headers and time displays
- **Pack Geometry**: Vertical stacking with proper padding
- **Font Configuration**: Arial font family with bold styling

### **Time Formatting**
Uses Python's `strftime()` for reliable time formatting:
- `%I`: 12-hour format hour (01-12)
- `%H`: 24-hour format hour (00-23)
- `%M`: Minutes (00-59)
- `%S`: Seconds (00-59)
- `%p`: AM/PM indicator

## 🎨 Customization Guide

### **Changing Colors**
Modify the color scheme in the label configurations:

```python
# Header colors
heading_12.config(foreground="your_color")  # Default: deepskyblue
heading_24.config(foreground="your_color")  # Default: lawngreen

# Time display colors
lbl_12.config(foreground="your_color")      # Default: white
lbl_24.config(foreground="your_color")      # Default: white

# Background color
window.configure(bg="your_color")           # Default: black
```

### **Font Customization**
Adjust font family, size, and style:

```python
# Header font
heading_12 = ui.Label(window, font=('YourFont', 20, 'bold'))

# Time display font
lbl_12 = ui.Label(window, font=('YourFont', 50, 'bold'))
```

### **Window Properties**
Customize window appearance:

```python
window.geometry("400x300")        # Set window size
window.resizable(False, False)    # Disable resizing
window.title("Your Custom Title") # Change window title
```

### **Update Frequency**
Modify the refresh rate:

```python
window.after(500, update_clock)   # Update every 0.5 seconds
window.after(2000, update_clock)  # Update every 2 seconds
```

### **Additional Time Zones**
Add multiple time zone support:

```python
import pytz  # Requires: pip install pytz

# Different time zones
utc_time = datetime.now(pytz.UTC)
est_time = utc_time.astimezone(pytz.timezone('US/Eastern'))
```

## 💻 System Requirements

- **Operating System**: Windows 7+, macOS 10.12+, or Linux
- **Python Version**: 3.6 or higher
- **Memory**: Minimal (< 30MB RAM)
- **Storage**: < 1MB
- **Dependencies**: None (uses Python standard library)

## 🔧 Troubleshooting
**Common Issues**
**"No module named 'tkinter'"**
```bash
# On Ubuntu/Debian
sudo apt-get install python3-tk

# On CentOS/RHEL
sudo yum install tkinter

# On macOS with Homebrew
brew install python-tk
```

**Clock Not Updating**
- Ensure the `update_clock()` function is being called
- Check that `window.after(1000, update_clock)` is present
- Verify system time is functioning correctly

**Display Issues**
- Adjust font size if text appears cut off
- Modify window size using `geometry()`
- Check color contrast for visibility

## 🤝 Contributing
Contributions are welcome! Here are some enhancement ideas:

**Feature Suggestions**
- **🌍 Multiple Time Zones**: Display time for different world locations
- **⏰ Alarm Functionality**: Add alarm and notification features
- **🎨 Theme Options**: Multiple color schemes and themes
- **📅 Date Display**: Show current date alongside time
- **🔊 Sound Effects**: Hourly chimes or tick sounds
- **💾 Settings**: Save user preferences and configurations

**How to Contribute**
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## 📄 License
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author
**Priyanshu Sahoo**

- GitHub: [@PriyanshuSahoo-PS98Tech](https://github.com/PriyanshuSahoo-PS98Tech)
- Portfolio: Creating practical desktop applications with clean, efficient code

## 🙏 Acknowledgments
- **Python Foundation**: For the excellent Tkinter GUI framework
- **Cross-Platform Support**: Thanks to Python's universal compatibility
- **Time Module**: Reliable system time integration
- **Open Source Community**: Contributing to accessible programming education

<div align="center"> <b>⭐ Star this repository if you found it useful!</b> <br><br> <b>🕐 Perfect for desktop productivity, presentations, or learning GUI programming! 🕐</b> <br><br> <b>#PS98Tech #Python #Tkinter #DigitalClock #GUI #Desktop</b> </div>

> **⏰ Design Philosophy**: This digital clock demonstrates the power of simplicity in software design. By focusing on clear functionality and clean aesthetics, it serves as both a practical desktop tool and an excellent learning resource for Python GUI development. The dual-format display ensures universal accessibility, whether you prefer traditional 12-hour time or international 24-hour format.
