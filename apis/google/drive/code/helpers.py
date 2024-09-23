import os

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def client(service_name: str, version: str):
    token = os.getenv('GOOGLE_OAUTH_TOKEN')
    if token is None:
        raise ValueError("GOOGLE_OAUTH_TOKEN environment variable is not set")

    creds = Credentials(token=token)
    try:
        service = build(serviceName=service_name, version=version, credentials=creds)
        return service
    except HttpError as err:
        print(err)
        exit(1)


MIME_TYPE_MAP = {
    # Text Files
    'text/plain': 'Plain Text Document',
    'text/html': 'HTML Document',
    'text/css': 'CSS Stylesheet',
    'text/csv': 'CSV Document',
    'text/javascript': 'JavaScript File',

    # Image Files
    'image/jpeg': 'JPEG Image',
    'image/png': 'PNG Image',
    'image/gif': 'GIF Image',
    'image/bmp': 'BMP Image',
    'image/tiff': 'TIFF Image',
    'image/webp': 'WebP Image',
    'image/svg+xml': 'SVG Vector Image',
    'image/x-icon': 'Icon File',

    # Audio Files
    'audio/mpeg': 'MP3 Audio',
    'audio/wav': 'WAV Audio',
    'audio/ogg': 'OGG Audio',
    'audio/flac': 'FLAC Audio',
    'audio/aac': 'AAC Audio',
    'audio/webm': 'WebM Audio',

    # Video Files
    'video/mp4': 'MP4 Video',
    'video/x-msvideo': 'AVI Video',
    'video/mpeg': 'MPEG Video',
    'video/ogg': 'OGG Video',
    'video/webm': 'WebM Video',
    'video/quicktime': 'QuickTime Video',
    'video/x-matroska': 'Matroska Video',

    # Document Files
    'application/pdf': 'PDF Document',
    'application/msword': 'Word Document',
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document': 'Word Document',
    'application/vnd.ms-excel': 'Excel Spreadsheet',
    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': 'Excel Spreadsheet',
    'application/vnd.ms-powerpoint': 'PowerPoint Presentation',
    'application/vnd.openxmlformats-officedocument.presentationml.presentation': 'PowerPoint Presentation',
    'application/rtf': 'Rich Text Document',
    'application/vnd.oasis.opendocument.text': 'OpenDocument Text',
    'application/vnd.oasis.opendocument.spreadsheet': 'OpenDocument Spreadsheet',
    'application/vnd.oasis.opendocument.presentation': 'OpenDocument Presentation',

    # Google Workspace File Types
    'application/vnd.google-apps.document': 'Google Docs Document',
    'application/vnd.google-apps.spreadsheet': 'Google Sheets Spreadsheet',
    'application/vnd.google-apps.presentation': 'Google Slides Presentation',
    'application/vnd.google-apps.form': 'Google Forms Form',
    'application/vnd.google-apps.drawing': 'Google Drawing',
    'application/vnd.google-apps.script': 'Google Apps Script',
    'application/vnd.google-apps.folder': 'Google Drive Folder',

    # Archive Files
    'application/zip': 'ZIP Archive',
    'application/x-tar': 'TAR Archive',
    'application/x-rar-compressed': 'RAR Archive',
    'application/gzip': 'GZIP Archive',
    'application/x-7z-compressed': '7z Archive',

    # JSON, XML, and YAML Files
    'application/json': 'JSON File',
    'application/xml': 'XML File',
    'application/x-yaml': 'YAML File',

    # Font Files
    'font/ttf': 'TrueType Font',
    'font/woff': 'WOFF Font',
    'font/woff2': 'WOFF2 Font',
    'application/font-woff': 'WOFF Font',
    'application/font-woff2': 'WOFF2 Font',

    # Script Files
    'application/x-sh': 'Shell Script',
    'application/x-python': 'Python Script',
    'application/x-ruby': 'Ruby Script',
    'application/x-perl': 'Perl Script',
    'application/x-php': 'PHP Script',
    'application/vnd.apple.installer+xml': 'Apple Installer Package',

    # Executable Files
    'application/x-msdownload': 'Windows Executable File',
    'application/vnd.debian.binary-package': 'Debian Package',
    'application/x-iso9660-image': 'ISO Disk Image',
    'application/x-disk-image': 'Disk Image',

    # eBook Files
    'application/epub+zip': 'EPUB eBook',
    'application/vnd.amazon.ebook': 'Amazon Kindle eBook',

    # CAD Files
    'application/vnd.autodesk.dwg': 'AutoCAD DWG File',
    'application/vnd.autodesk.dxf': 'AutoCAD DXF File',

    # Markdown and LaTeX Files
    'text/markdown': 'Markdown File',
    'application/x-latex': 'LaTeX File',

    # Other File Types
    'application/octet-stream': 'Binary File',
    'application/x-httpd-php': 'PHP File',
    'application/x-java-archive': 'Java Archive (JAR)',
    'application/java-archive': 'Java Archive (JAR)',
    'application/x-iso9660-image': 'ISO Disk Image',
    'application/x-shockwave-flash': 'Adobe Flash File',
    'application/x-sql': 'SQL File',
    'application/x-java-jnlp-file': 'Java Web Start File',
    'application/x-tex': 'TeX File',

    # 3D Model Files
    'model/obj': 'Wavefront OBJ Model',
    'model/stl': 'STL 3D Model',

    # CSV and TSV
    'text/csv': 'CSV File',
    'text/tab-separated-values': 'TSV File',

    # Apple File Types
    'application/x-apple-diskimage': 'Apple Disk Image (DMG)',
    'application/vnd.apple.keynote': 'Apple Keynote Presentation',
    'application/vnd.apple.numbers': 'Apple Numbers Spreadsheet',
    'application/vnd.apple.pages': 'Apple Pages Document',

    # Adobe Files
    'application/vnd.adobe.photoshop': 'Adobe Photoshop Document (PSD)',
    'application/x-director': 'Adobe Director File',
    'application/vnd.adobe.flash.movie': 'Adobe Flash File',
    'application/vnd.adobe.xdp+xml': 'Adobe XML Data Package',

    # Miscellaneous
    'application/vnd.mozilla.xul+xml': 'Mozilla XUL Document',
    'application/x-bittorrent': 'BitTorrent File',
    'application/x-msdownload': 'Windows Executable File (EXE)',
}


def get_friendly_file_type(mime_type):
    return MIME_TYPE_MAP.get(mime_type, mime_type)
