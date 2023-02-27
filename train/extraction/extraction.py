from io import BytesIO
from pathlib import Path
import fitz
from fitz import Document, Pixmap

def convert_pixmap_to_rgb(pixmap) -> Pixmap:
    """Convert to rgb in order to write on png"""
    # check if it is already on rgb
    if pixmap.n < 4:
        return pixmap
    else:
        return fitz.Pixmap(fitz.csRGB, pixmap)

pdfs_directory_path = ".\dataset-cats-dogs-others"
images_directory_path = ".\extracted_images"

def extract_images_from_pdfs(pdfs_directory_path:str,images_directory_path:str):
    Path(images_directory_path).mkdir(parents=True, exist_ok=True)
    files = [p for p in Path(pdfs_directory_path).iterdir() if p.is_file()]
    for path in files:
        with open(path, "rb") as file_stream:
            with fitz.open(stream=file_stream.read(), filetype="pdf") as d:
                file_images = []
                nb = len(d) - 1
                for i in range(nb):
                    page = d[i]
                    imgs = d.get_page_images(i)
                    nb_imgs = len(imgs)
                    for j, img in enumerate(imgs):
                        xref = img[0]
                        pix = fitz.Pixmap(d, xref)
                        bytes = BytesIO(convert_pixmap_to_rgb(pix).tobytes())
                        filename = path.stem + "_page" + str(i) + "_index" + str(j) + ".png"
                        path_filename = "{0}\\{1}".format(images_directory_path, filename)
                        file_images.append(path_filename)
                        with open(path_filename, "wb") as f:
                            f.write(bytes.getbuffer())
                return file_images

#extract_images_from_pdfs(pdfs_directory_path,images_directory_path)
