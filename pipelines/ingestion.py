import os
from urllib import request


def get_path_for_csv_file(file: str, base_path: str):
    source_csv_filename = file
    extracted_file = os.path.join(
        base_path, 'extracted', source_csv_filename)

    return extracted_file


def check_if_extraction_folder_is_created(folder_path: str):
    folder_is_created = os.path.exists(folder_path)

    if not folder_is_created:
        os.mkdir(folder_path)


def download_csv_if_not_exists(csv_path: str, path: str):
    work_dir = path
    destination_file = "votacao_candidato_munzona_2022.zip"
    url = '''
    https://cdn.tse.jus.br/estatistica/sead/odsele/votacao_candidato_munzona/votacao_candidato_munzona_2022.zip
    '''
    destination_zip_path = os.path.join(work_dir, destination_file)

    zip_already_downloaded = os.path.exists(destination_zip_path)

    if not zip_already_downloaded:
        download_zip_file(url, destination_zip_path)

    file_is_extracted = os.path.exists(csv_path)

    if not file_is_extracted:
        source_csv_filename = 'votacao_candidato_munzona_2022_BRASIL.csv'

        csv_extracted_path = os.path.join(work_dir, 'extracted')

        unzip_file(source_csv_filename,
                   destination_zip_path, csv_extracted_path)


def download_zip_file(url: str, destination_path: str):
    request.urlretrieve(url, destination_path)


def unzip_file(file: str, source_path: str, extract_path):
    from zipfile import ZipFile

    with ZipFile(source_path, 'r') as zip_file:
        zip_file.extract(file, extract_path)
