# NotDotBlur

A fast and lightweight image enlargement application. NotDotBlur uses a pixel-perfect scaling algorithm to enlarge images without blurring, maintaining crisp edges and sharp details.

## Features

- **Pixel-Perfect Scaling**: Enlarges images without blurring or interpolation
- **Fast Processing**: Optimized algorithms for quick image processing
- **Lightweight**: Minimal executable size with optimized performance
- **Modern UI**: Beautiful dark-themed interface
- **Multi-language Support**: Japanese and English interface
- **Multiple Format Support**: PNG, JPG, JPEG, GIF, BMP files
- **High Scale Factors**: Support for large scale factors (16x, 32x, etc.)
- **Memory Efficient**: Optimized memory usage for large images
- **No Installation Required**: Standalone executable - just extract and run

## Screenshots

The application features a clean, modern interface with:
- Dark theme for comfortable viewing
- Intuitive controls for scale factor selection
- Real-time language switching
- Progress feedback during processing

## Quick Start

1. **Download**: Get the `NotDotBlur.zip` file
2. **Extract**: Extract the zip file to any folder on your computer
3. **Run**: Double-click `NotDotBlur.exe` to launch
4. **Set Scale Factor**: Enter your desired enlargement factor (default: 16x)
5. **Select Image**: Click "Select Image" to choose your input file
6. **Choose Output**: Select where to save the enlarged image
7. **Process**: The application will enlarge your image using pixel-perfect scaling

## System Requirements

- **OS**: Windows 10/11 (tested on Windows 10.0.22631)
- **RAM**: 4GB minimum, 8GB recommended for large images
- **Storage**: 50MB free space for the application
- **No Python Required**: Standalone executable
- **Zip Extraction**: Built-in Windows zip support or any zip utility

## File Contents

The zip file contains:
- `NotDotBlur.exe` - Main application executable
- `README.md` - This documentation file
- `favicon.ico` - Application icon (optional)

## Usage Guide

### Supported Scale Factors

- Any integer value 1 or greater
- Recommended range: 2x to 32x
- Higher factors will result in larger output files

### Supported Input Formats

- PNG (recommended for best quality)
- JPG/JPEG
- GIF
- BMP

### Output Format

- PNG (lossless, recommended for pixel art and graphics)

### Processing Tips

- **For Pixel Art**: Use scale factors of 2x, 4x, 8x, or 16x for best results
- **For Graphics**: Any scale factor works well
- **For Photos**: Consider using other tools with interpolation for smoother results
- **Large Images**: Processing time increases with image size and scale factor

## Technical Details

### Algorithm

NotDotBlur uses a nearest-neighbor scaling algorithm that:
- Preserves each pixel exactly as it appears in the original
- Creates crisp, sharp edges without anti-aliasing
- Maintains the original color values
- Works optimally for pixel art, graphics, and images with sharp edges

### Performance Features

- **Fast Startup**: Optimized loading with splash screen
- **Memory Management**: Efficient memory usage with garbage collection
- **Background Processing**: Non-blocking UI during image processing
- **Error Handling**: Comprehensive error handling for various scenarios

## Troubleshooting

### Common Issues

1. **Application Won't Start**
   - Ensure you've extracted the zip file completely
   - Make sure you're running on Windows 10/11
   - Try running as administrator if needed
   - Check if antivirus is blocking the executable
   - Ensure the exe file is in the same folder as extracted

2. **Zip Extraction Problems**
   - Use Windows built-in zip extraction or 7-Zip
   - Ensure you have sufficient disk space for extraction
   - Try extracting to a different folder if issues persist

3. **Slow Processing**
   - Large images or high scale factors take more time
   - Close other applications to free up memory
   - Consider using smaller scale factors for very large images

4. **Memory Errors**
   - Ensure you have sufficient RAM (4GB minimum)
   - Try processing smaller images first
   - Restart the application if needed

5. **File Access Issues**
   - Ensure you have write permissions in the output directory
   - Check if the input file is not corrupted
   - Try saving to a different location

### Error Messages

- **"Invalid scale factor"**: Enter a number 1 or greater
- **"Unsupported file format"**: Use PNG, JPG, JPEG, GIF, or BMP files
- **"File not found"**: Check if the selected file exists and is accessible
- **"Access denied"**: Try running as administrator or check file permissions

## Performance

### Benchmarks

- **Startup Time**: ~2-3 seconds
- **Processing Speed**: Varies by image size and scale factor
- **Memory Usage**: Optimized for minimal footprint
- **File Size**: ~15-25MB executable, ~10-15MB compressed zip

### Optimization Features

- Efficient pixel data handling
- Background library loading
- Garbage collection optimization
- Minimal resource usage

## Use Cases

### Perfect For

- **Pixel Art Enlargement**: Maintains crisp pixel boundaries
- **Game Graphics**: Scales sprites and textures perfectly
- **Digital Art**: Preserves sharp edges and details
- **Icon Scaling**: Creates clear, sharp icons at larger sizes
- **Screenshot Enhancement**: Enlarges screenshots without blur

### Not Recommended For

- **Photographic Images**: May appear blocky without interpolation
- **Smooth Graphics**: Other tools may provide better results
- **Very Large Scale Factors**: May consume significant memory

## Installation Notes

- **No Installation Required**: Simply extract and run
- **Portable**: Can be run from any folder, including USB drives
- **No Registry Changes**: Leaves no traces on your system
- **Easy Removal**: Just delete the extracted folder

## Version Information

- **Current Version**: v1.0
- **Release Date**: Latest stable release
- **File Size**: ~10-15MB compressed zip file
- **Compatibility**: Windows 10/11
- **Distribution**: Portable zip archive

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Ensure you've extracted the zip file completely
3. Verify you're using the latest version
4. Try processing a different image to isolate the issue

## License

This application is provided as-is for personal and commercial use.

---

**Note**: NotDotBlur is designed specifically for pixel-perfect image enlargement. For photographic images that require smooth scaling, consider using other tools with interpolation algorithms. 