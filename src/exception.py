import sys

def error_message_detail(error, error_detail:sys):
    _,_,error_tb = error_detail.exc_info()
    file_name = error_tb.tb_frame.f_code.co_filename
    line_no = error_tb.tb_lineno
    error_message = f"Error occured in python script named {file_name} line number {line_no} error message {str(error)} "
    return error_message

class custom_exception(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message, error_detail=error_detail)
    def __str__(self):
        return self.error_message