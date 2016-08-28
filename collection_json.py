# -*- coding: utf-8 -*-

# base = {
#       "collection":
#       {
#         "version": "1.0",
#         "href": URI,
#         "links": [ARRAY],
#         "items": [ARRAY],
#         "queries": [ARRAY],
#         "template": {OBJECT},
#         "error": {OBJECT}
#       }
#     }

class Collections:

    def __init__(self):
        self.domain = {
              "collection":
              {
                "version": "1.0",
                "href": "/json/domain.json",
                "items": [],
                "queries": [],
                "template": {
                    "data": [
                        {"name": "id", "value": ""},
                        {"name": "domain", "value": ""},
                        {"name": "tranceport", "value": "virtual"},
                        {"name": "active", "value": True},
                        {"name": "description", "value": ""},
                    ]
                },
                "error": {
                    "title": "",
                    "code": "",
                    "message": ""
                }
              }
            }


        self.alias = {
              "collection":
              {
                "version": "1.0",
                "href": "/json/alias.json",
                "items": [],
                "queries": [],
                "template": {
                    "data": [
                        {"name": "id", "value": ""},
                        {"name": "email", "value": ""},
                        {"name": "goto", "value": ""},
                        {"name": "active", "value": True},
                        {"name": "description", "value": ""},
                    ]
                },
                "error": {
                    "title": "",
                    "code": "",
                    "message": ""
                }
              }
            }

        self.mailbox = {
              "collection":
              {
                "version": "1.0",
                "href": "/json/mailbox.json",
                "items": [],
                "queries": [],
                "template": {
                    "data": [
                        {"name": "id", "value": ""},
                        {"name": "username", "value": ""},
                        {"name": "password", "value": ""},
                        {"name": "maildir", "value": ""},
                        {"name": "active", "value": True},
                        {"name": "local_part", "value": ""},
                        {"name": "domain_part", "value": ""},
                        {"name": "description", "value": ""},
                    ]
                },
                "error": {
                    "title": "",
                    "code": "",
                    "message": ""
                }
              }
            }

        self.error_data = {
              "collection":
              {
                "version": "1.0",
                "href": "/json/error_data.json",
                "items": [],
                "queries": [],
                "template": {
                    "data": [
                    ]
                },
                "error": {
                    "title": "",
                    "code": "",
                    "message": ""
                }
              }
            }

        self.formats_dict = {'domain': self.domain, 'alias': self.alias, 'mailbox': self.mailbox}


    def get_format(self, format_type):
        return self.formats_dict[format_type]


    def get_template(self, format_type):
        return self.formats_dict[format_type]['collection']['template']['data']
