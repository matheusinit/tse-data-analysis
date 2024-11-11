import unittest

import pipelines.ingestion as f


class TestDataIngestionExtraction(unittest.TestCase):
    def test_ingestion_extraction(self):
        csv_file = 'votacao_candidato_munzona_2022_BRASIL.csv'
        EXTRACTION_FOLDER_PATH = './work/'

        csv_file_path = f.get_path_for_csv_file(
            csv_file, EXTRACTION_FOLDER_PATH)

        f.check_if_extraction_folder_is_created(EXTRACTION_FOLDER_PATH)

        f.download_csv_if_not_exists(csv_file_path, EXTRACTION_FOLDER_PATH)
