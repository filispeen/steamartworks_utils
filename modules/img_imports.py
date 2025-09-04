from concurrent.futures import ThreadPoolExecutor
from modules.imports import ingore_dirs
from PIL import Image, ImageDraw, ImageFont
import shutil
import os

Image.MAX_IMAGE_PIXELS = None