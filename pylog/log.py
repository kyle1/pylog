import pandas as pd
from datetime import datetime


class LogMessage:
    def __init__(self, message, message_type):
        self._date_time = None
        self._message = None
        self._message_type = None

        setattr(self, '_date_time', datetime.now().strftime('%b %d %Y %H:%M'))
        self._set_message(message, message_type)

    def _set_message(self, message, message_type):
        setattr(self, '_message', message)
        setattr(self, '_message_type', message_type)

    def print_message(self):
        print(f'{self._date_time} - {self._message_type} - {self._message}')

    @property
    def dataframe(self):
        fields_to_include = {
            'DateTime': self._date_time,
            'Message': self._message,
            'MessageType': self._message_type
        }
        return pd.DataFrame([fields_to_include], index=[self._date_time])


class Log:
    def __init__(self):
        self._log_messages = []

    def __repr__(self):
        return self._log_messages

    def __iter__(self):
        return iter(self.__repr__())

    def _get_message_font_color(self, message_type):
        if message_type == 'info':
            return 'green'
        elif message_type == 'warning':
            return 'orange'
        else:
            return 'red'

    def add_info(self, message):
        log_message = LogMessage(message, 'info')
        self._log_messages.append(log_message)

    def add_warning(self, message):
        log_message = LogMessage(message, 'warning')
        self._log_messages.append(log_message)

    def add_error(self, message):
        log_message = LogMessage(message, 'error')
        self._log_messages.append(log_message)

    @property
    def warning_count(self):
        warning_count = 0
        for log_message in self._log_messages:
            if log_message._message_type == 'warning':
                warning_count += 1
        return warning_count

    @property
    def error_count(self):
        error_count = 0
        for log_message in self._log_messages:
            if log_message._message_type == 'error':
                error_count += 1
        return error_count

    @property
    def html_email_body(self):
        email_body = '<html>\n'
        for log_message in self._log_messages:
            font_color = self._get_message_font_color(log_message._message_type)
            email_body += f'<span style="font-size: 8px; color: {font_color}">\n'
            email_body += f'{log_message._date_time} {log_message._message}\n'
            email_body += f'</span>\n'
            email_body += f'<br>\n'
        email_body += '</html>'
        return email_body

    @property
    def dataframes(self):
        frames = []
        for log_message in self.__iter__():
            frames.append(log_message.dataframe)
        return pd.concat(frames)

