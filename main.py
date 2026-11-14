import shutil, os
src = os.path.join(os.path.dirname(__file__), 'happy.png')
dst = '/output/entry.png'
# Create the destination directory before copying the image.
os.makedirs('/output', exist_ok=True)
shutil.copyfile(src, dst)
print('wrote', dst)

