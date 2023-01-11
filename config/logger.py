import os, sys
import logging
from src.constants.constants import TIMESTAMP

LOG_DIR = "logs"
LOG_FILE_NAME = f"log_{TIMESTAMP}.log"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE_NAME)

logger.basicConfig(filename=LOG_FILE_PATH,
                    filemode="w",
                    format='[%(asctime)s] \t%(levelname)s \t%(lineno)d \t%(filename)s \t%(funcName)s() \t%(message)s',
                    level=logging.INFO
                    )


class DetailedException(Exception):

    def __init__(self, error_message: Exception, error_detail: sys):
        super().__init__(error_message)
        self.error_message = DetailedException.get_detailed_error_message(error_message=error_message,
                                                                         error_detail=error_detail
                                                                         )

    @staticmethod
    def get_detailed_error_message(error_message: Exception, error_detail: sys) -> str:
        """
        error_message: Exception object
        error_detail: object of sys module
        """
        _, _, exec_tb = error_detail.exc_info()
        try_block_line_number = exec_tb.tb_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename
        error_message = f"Error occurred in script: [ {file_name} ] at line number: [{try_block_line_number}] error " \
                        f"message: [{error_message}] "

        return error_message

    def __str__(self):
        return self.error_message

    def __repr__(self) -> str:
        return str(DetailedException.__name__)