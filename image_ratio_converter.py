#!/usr/bin/env python3
"""
High-Quality Image to 16:9 Ratio Converter
Supports multiple resize methods to maintain quality
"""

from PIL import Image, ImageFilter
import os
import argparse
from pathlib import Path


def resize_to_16_9(input_path, output_path, method='crop', quality=95):
    """
    Resize image to 16:9 aspect ratio with various methods.
    
    Args:
        input_path: Path to input image
        output_path: Path to save output image
        method: 'crop', 'fit', or 'stretch'
        quality: JPEG quality (1-100), or PNG compression level
    """
    # Open image
    img = Image.open(input_path)
    original_width, original_height = img.size
    
    print(f"Original size: {original_width}x{original_height}")
    
    # Target aspect ratio
    target_ratio = 16 / 9
    current_ratio = original_width / original_height
    
    if method == 'crop':
        # Crop to 16:9 by removing excess from edges
        if current_ratio > target_ratio:
            # Image is wider than 16:9, crop width
            new_width = int(original_height * target_ratio)
            left = (original_width - new_width) // 2
            img = img.crop((left, 0, left + new_width, original_height))
        else:
            # Image is taller than 16:9, crop height
            new_height = int(original_width / target_ratio)
            top = (original_height - new_height) // 2
            img = img.crop((0, top, original_width, top + new_height))
    
    elif method == 'fit':
        # Fit image into 16:9 canvas with padding (letterbox/pillarbox)
        if current_ratio > target_ratio:
            # Wider image - add top/bottom padding
            new_height = int(original_width / target_ratio)
            new_img = Image.new('RGB', (original_width, new_height), (0, 0, 0))
            top = (new_height - original_height) // 2
            new_img.paste(img, (0, top))
            img = new_img
        else:
            # Taller image - add left/right padding
            new_width = int(original_height * target_ratio)
            new_img = Image.new('RGB', (new_width, original_height), (0, 0, 0))
            left = (new_width - original_width) // 2
            new_img.paste(img, (left, 0))
            img = new_img
    
    elif method == 'stretch':
        # Stretch/squeeze to fit 16:9 (may distort)
        # Keep resolution high, just change aspect ratio
        new_width = original_width
        new_height = int(original_width / target_ratio)
        img = img.resize((new_width, new_height), Image.LANCZOS)
    
    final_width, final_height = img.size
    print(f"Final size: {final_width}x{final_height}")
    print(f"Aspect ratio: {final_width/final_height:.3f} (16:9 = {target_ratio:.3f})")
    
    # Save with high quality
    if output_path.lower().endswith('.png'):
        # PNG: use compression level 1 (best quality, larger file)
        img.save(output_path, 'PNG', compress_level=1, optimize=False)
    elif output_path.lower().endswith(('.jpg', '.jpeg')):
        # JPEG: use quality 95+ and no subsampling for best quality
        img.save(output_path, 'JPEG', quality=quality, subsampling=0, optimize=False)
    else:
        # Auto-detect format
        img.save(output_path, quality=quality)
    
    print(f"Saved to: {output_path}")


def batch_process(input_dir, output_dir, method='crop', quality=95):
    """Process all images in a directory."""
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Supported image extensions
    extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp'}
    
    images = [f for f in input_path.iterdir() 
              if f.suffix.lower() in extensions]
    
    print(f"Found {len(images)} images to process\n")
    
    for img_file in images:
        output_file = output_path / img_file.name
        print(f"Processing: {img_file.name}")
        try:
            resize_to_16_9(str(img_file), str(output_file), method, quality)
            print()
        except Exception as e:
            print(f"Error processing {img_file.name}: {e}\n")


def main():
    parser = argparse.ArgumentParser(
        description='Convert images to 16:9 aspect ratio with high quality'
    )
    parser.add_argument('input', help='Input image file or directory')
    parser.add_argument('-o', '--output', help='Output file or directory')
    parser.add_argument('-m', '--method', 
                       choices=['crop', 'fit', 'stretch'],
                       default='crop',
                       help='Resize method: crop (default), fit (letterbox), or stretch')
    parser.add_argument('-q', '--quality',
                       type=int,
                       default=95,
                       help='Output quality (1-100 for JPEG, default=95)')
    parser.add_argument('-b', '--batch',
                       action='store_true',
                       help='Process all images in input directory')
    
    args = parser.parse_args()
    
    if args.batch:
        output_dir = args.output or 'output_16_9'
        batch_process(args.input, output_dir, args.method, args.quality)
    else:
        if not args.output:
            # Generate output filename
            path = Path(args.input)
            output = f"{path.stem}_16_9{path.suffix}"
        else:
            output = args.output
        
        resize_to_16_9(args.input, output, args.method, args.quality)


if __name__ == '__main__':
    main()
