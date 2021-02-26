class HttpErrors:
    """ Class to define error in http calls """

    @staticmethod
    def error_422():
        """ HTTP 422 """

        return {"status_code": 422, "body": {"error": "Unprossessable Entity"}}

    @staticmethod
    def error_400():
        """ HTTP 400 """
        return {"status_code": 400, "body": {"error": "Bad Request"}}

    @staticmethod
    def error_409():
        """ HTTP 409 """
        return {"status_code": 409, "body": {"error": "Conflict"}}
