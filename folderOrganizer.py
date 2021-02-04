import os
import shutil

## Aqui hay que poner tu ruta de descargas
downloads = 'C:\\Users\\Usuario\\Downloads\\'

text_ext = ('.txt', '.doc', '.docx', '.pptx', '.odf', '.docm', '.pdf', '.ppt', '.xlsx', '.ods', '.odt')
video_ext = ('.mov', '.mp4', '.avi', '.mkv', '.mkv', '.flv', '.wmv', '.mpeg')
audio_ext = ('.mp3', '.wma', '.wav', '.flac')
photo_ext = ('.jpg', '.png', '.jpeg', '.gif', '.tiff', '.psd', '.bmp', '.ico', '.svg', '.JPG', '.tif')
compressed_ext = ('.zip', '.rar', '.rar5', '.7z', '.ace', '.gz')
executable_ext = ('.exe', '.msi')
programming_ext = ('.py' , '.cpp' , '.js', '.html', '.css', '.c', '.ino', '.sql')

def order(file, extension):

    for etx in text_ext:

        if extension == etx:
            shutil.move(downloads + file, downloads + 'Texto')

    for etx in video_ext:

        if extension == etx:
            shutil.move(downloads + file, downloads + 'Videos')

    for etx in audio_ext:

        if extension == etx:
            shutil.move(downloads + file, downloads + 'Audios')

    for etx in photo_ext:

        if extension == etx:
            shutil.move(downloads + file, downloads + 'Imagenes')

    for etx in compressed_ext:

        if extension == etx:
            shutil.move(downloads + file, downloads + 'Comprimidos')

    for etx in executable_ext:

        if extension == etx:
            shutil.move(downloads + file, downloads + 'Ejecutables')

    for etx in programming_ext:

        if extension == etx:
            shutil.move(downloads + file, downloads + 'Programacion')

    if extension != '':
        try:
            shutil.move(downloads + file, downloads + 'Otros')

        except:
            pass


def main():

    print('Iniciando\n')

    for file in os.listdir(downloads):

        try:
            etx = os.path.splitext(file)[1]

            order(file, etx)

        except:
            print('No se pudo mover el archivo: {}\n'.format(file))

    print('Proceso finalizado')


if __name__ == '__main__':
    main()