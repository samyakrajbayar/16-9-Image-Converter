# 16:9 Image Converter 🖼️

A high-quality Python tool for converting images to 16:9 aspect ratio with multiple resize methods and optimal quality preservation.

## ✨ Features

- **Three Resize Methods**
  - 🔲 **Crop**: Smart center-crop to 16:9 (preserves quality)
  - 📺 **Fit**: Letterbox/pillarbox with black bars (no cropping)
  - 🔄 **Stretch**: Stretch/squeeze to 16:9 (may distort)

- **High Quality Output**
  - LANCZOS resampling for best quality
  - JPEG quality 95+ with zero subsampling
  - PNG compression level 1 (minimal compression)
  - Maximum resolution preservation

- **Batch Processing**
  - Process entire folders at once
  - Maintains directory structure

- **Multiple Format Support**
  - JPG/JPEG, PNG, BMP, TIFF, WEBP

## 🚀 Installation

### Requirements
- Python 3.6+
- Pillow library

### Install Dependencies

```bash
pip install Pillow
```

Or use requirements.txt:
```bash
pip install -r requirements.txt
```

## 📖 Usage

### Basic Usage

Convert a single image (crop method by default):
```bash
python image_converter.py input.jpg -o output.jpg
```

### Resize Methods

**Crop Method** (recommended for quality):
```bash
python image_converter.py banana.jpg -o banana_16_9.jpg -m crop
```

**Fit Method** (adds black bars, no content loss):
```bash
python image_converter.py photo.png -o photo_16_9.png -m fit
```

**Stretch Method** (may distort):
```bash
python image_converter.py image.jpg -o stretched.jpg -m stretch
```

### Batch Processing

Process all images in a folder:
```bash
python image_converter.py input_folder/ -o output_folder/ -b
```

### Quality Settings

Set custom JPEG quality (1-100):
```bash
python image_converter.py input.jpg -o output.jpg -q 100
```

## 🎯 Command Line Arguments

```
positional arguments:
  input                 Input image file or directory

optional arguments:
  -h, --help            Show help message
  -o, --output         Output file or directory
  -m, --method         Resize method: crop (default), fit, or stretch
  -q, --quality        Output quality (1-100 for JPEG, default=95)
  -b, --batch          Process all images in input directory
```

## 📊 Resize Method Comparison

| Method | Pros | Cons | Best For |
|--------|------|------|----------|
| **Crop** | • No distortion<br>• Max quality<br>• Clean result | • Loses edge content | Photography, wallpapers |
| **Fit** | • No content loss<br>• No distortion | • Black bars<br>• Smaller effective area | Preserving full images |
| **Stretch** | • Uses full canvas<br>• No content loss | • Distorts image<br>• May look unnatural | Graphics, logos |

## 💡 Examples

### Example 1: Single Image Conversion
```bash
python image_converter.py vacation_photo.jpg -o vacation_16_9.jpg
```
Output:
```
Original size: 4000x3000
Final size: 4000x2250
Aspect ratio: 1.778 (16:9 = 1.778)
Saved to: vacation_16_9.jpg
```

### Example 2: Batch Processing
```bash
python image_converter.py photos/ -o output/ -b -m fit
```

### Example 3: Maximum Quality PNG
```bash
python image_converter.py banner.png -o banner_16_9.png -q 100
```

## 🔧 How It Works

### Crop Method
- Calculates target 16:9 dimensions
- Removes excess width or height from edges
- Centers the crop area automatically

### Fit Method
- Creates a 16:9 canvas
- Pastes original image centered
- Fills remaining space with black

### Stretch Method
- Resizes to 16:9 using high-quality resampling
- May change proportions

## 📁 Project Structure

```
├── image_converter.py    # Main script
├── README.md            # This file
├── requirements.txt     # Dependencies
├── LICENSE             # License file
└── examples/           # Example images (optional)
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Known Issues

- Very large images (>100MP) may require significant memory
- Transparent PNGs will have black bars when using fit method

## 🗺️ Roadmap

- [ ] Custom background colors for fit method
- [ ] Smart crop with face/object detection
- [ ] GUI interface
- [ ] Support for video files
- [ ] Batch progress bar
- [ ] Custom aspect ratios (21:9, 4:3, etc.)

## ❓ FAQ

**Q: Which method should I use?**  
A: Use `crop` for most cases - it maintains quality and looks natural. Use `fit` when you can't lose any content.

**Q: Why are my JPEGs so large?**  
A: Quality 95+ with no subsampling creates larger but better files. Lower `-q` value if needed.

**Q: Can I process RAW files?**  
A: No, convert RAW files to JPEG/PNG first using your camera software.

**Q: Does this work with transparent PNGs?**  
A: Yes, but fit method will add black bars. Crop and stretch methods preserve transparency.


## 🙏 Acknowledgments

- [Pillow](https://python-pillow.org/) - Python Imaging Library
- Inspired by the need for high-quality batch image processing

---

⭐ If this project helped you, please star it on GitHub!
