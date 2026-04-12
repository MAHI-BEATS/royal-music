import sys
import traceback
from functools import wraps
from pyrogram.errors.exceptions.forbidden_403 import ChatWriteForbidden

def capture_err(func):
    @wraps(func)
    async def capture(client, message, *args, **kwargs):
        try:
            return await func(client, message, *args, **kwargs)
        except ChatWriteForbidden:
            return
        except Exception as err:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            errors = traceback.format_exception(
                exc_type, value=exc_obj, tb=exc_tb
            )
            error_feedback = "".join(errors)
            print(error_feedback)
    return capture

def capture_callback_err(func):
    @wraps(func)
    async def capture(client, callback_query, *args, **kwargs):
        try:
            return await func(client, callback_query, *args, **kwargs)
        except ChatWriteForbidden:
            return
        except Exception as err:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            errors = traceback.format_exception(
                exc_type, value=exc_obj, tb=exc_tb
            )
            error_feedback = "".join(errors)
            print(error_feedback)
    return capture
