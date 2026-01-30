import sys
from src.airbnbproject.logger import logging
     

def error_message_detail(error: Exception, error_details: sys) -> str:
        """Generate detailed error message."""
        _, _, exc_tb = error_details.exc_info()
        line_number = exc_tb.tb_lineno
        file_name = exc_tb.tb_frame.f_code.co_filename
        error_message = f"Error occurred in script: {file_name} at line number: {line_number} with message: {str(error)}"
        return error_message
    

class CustomException(Exception):
    """
    Custom exception class for the Airbnb project.
    """

    def __init__(self, error: Exception, error_details: sys):
        self.error_message = error_message_detail(error, error_details)
        super().__init__(self.error_message)

    def __str__(self) -> str:
        return self.error_message